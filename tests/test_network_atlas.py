"""Packaging/integrity checks for the illustrative atlas, not psychometric validation."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

ROOT=pathlib.Path(__file__).resolve().parents[1]
SVG='{http://www.w3.org/2000/svg}'

class Links(HTMLParser):
 def __init__(self):
  super().__init__();self.ids=[];self.hrefs=[];self.scripts=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  if tag=='a' and 'href' in a:self.hrefs.append(a['href'])
  if tag=='script':self.scripts.append(a)

class NetworkAtlas(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.temp=tempfile.TemporaryDirectory();cls.out=pathlib.Path(cls.temp.name)
  for script in ['build.py','compare.py']:
   shutil.copy2(ROOT/'network_atlas'/script,cls.out/script)
   subprocess.run([sys.executable,str(cls.out/script)],check=True,capture_output=True,text=True)
  cls.data=json.loads((cls.out/'network-comparison.json').read_text(encoding='utf-8'))
 @classmethod
 def tearDownClass(cls):cls.temp.cleanup()
 def test_comparison_sets_and_explicit_illustrative_status(self):
  d=self.data;nodes={n['id'] for n in d['nodes']}
  self.assertEqual(d['status'],'illustrative_design_only');self.assertEqual(len(nodes),66)
  sets=[]
  for field in ['graph_a','graph_b']:
   edges=d[field];pairs={tuple(sorted([e['source'],e['target']])) for e in edges}
   self.assertEqual(len(pairs),len(edges));self.assertEqual(len(pairs),140)
   self.assertTrue(all(set(p)<=nodes for p in pairs))
   self.assertTrue(all(e['status']=='illustrative_only' and e['weight'] is None for e in edges))
   sets.append(pairs)
  a,b=sets
  self.assertEqual(set(map(tuple,d['shared'])),a&b)
  self.assertEqual(set(map(tuple,d['only_a'])),a-b)
  self.assertEqual(set(map(tuple,d['only_b'])),b-a)
  self.assertEqual((len(a&b),len(a-b),len(b-a)),(134,6,6))
  self.assertEqual(set(d['changed_neighborhoods']),{n for pair in a^b for n in pair})
 def test_fixed_geometry_and_difference_marks(self):
  layouts=[]
  for name in ['a','b','difference']:
   root=ET.fromstring((self.out/f'comparison-{name}.svg').read_text(encoding='utf-8'))
   nodes=[e for e in root.iter(SVG+'a') if 'node' in e.attrib.get('class','').split()]
   layouts.append({n.attrib['href']:tuple(n.findall(SVG+'circle')[-1].attrib[k] for k in ['cx','cy']) for n in nodes})
   self.assertEqual(len(nodes),66)
   if name=='difference':
    counts={kind:sum('e-'+kind in e.attrib.get('class','').split() for e in root.iter(SVG+'line')) for kind in ['shared','only-a','only-b']}
    self.assertEqual(counts,{'shared':134,'only-a':6,'only-b':6})
    rings=[e for e in root.iter(SVG+'circle') if e.attrib.get('class')=='change-ring']
    self.assertEqual(len(rings),len(self.data['changed_neighborhoods']))
  self.assertTrue(all(p==layouts[0] for p in layouts))
 def test_self_contained_html_and_local_links(self):
  for filename in ['network-concept.html','network-comparison.html']:
   parser=Links();parser.feed((self.out/filename).read_text(encoding='utf-8'))
   self.assertFalse(parser.scripts);self.assertEqual(len(parser.ids),len(set(parser.ids)))
   for href in parser.hrefs:
    if href.startswith(('https://','http://')):continue
    path,_,fragment=href.partition('#')
    if path:self.assertTrue((self.out/path).is_file(),href)
    elif fragment:self.assertIn(fragment,parser.ids,href)
 def test_committed_outputs_match_generators_and_screenshots_exist(self):
  for output in self.out.iterdir():
   if output.suffix not in ['.html','.svg','.json']:continue
   self.assertEqual(output.read_bytes(),(ROOT/'network_atlas'/output.name).read_bytes(),output.name)
  for name in ['single-network.jpg','differences-only.jpg']:
   content=(ROOT/'network_atlas/screenshots'/name).read_bytes()
   self.assertTrue(content.startswith(b'\xff\xd8'));self.assertGreater(len(content),10000)

if __name__=='__main__':unittest.main()
