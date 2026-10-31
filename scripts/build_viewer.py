import pathlib,json,sys
root=pathlib.Path(__file__).resolve().parents[1]
v=root/'viewer'
js=(v/'src/app.js').read_text(encoding='utf-8-sig')
shell=(v/'src/shell.html').read_text(encoding='utf-8-sig')
document=shell.replace('/*APP_CODE*/',js)
(v/'viewer.html').write_text(document,encoding='utf-8')
sys.path.insert(0,str(v))
from viewer import build_viewer
build_viewer([v/'synthetic-A.graph.json',v/'synthetic-B.graph.json'],v/'demo.html')
path=v/'Psychometric_KG_Viewer.ipynb'
nb=json.loads(path.read_text(encoding='utf-8'))
source='from pathlib import Path\nPath("viewer.html").write_text('+repr(document)+', encoding="utf-8")\nPath("viewer.py").write_text('+repr((v/'viewer.py').read_text())+', encoding="utf-8")\nprint("Viewer ready. No installation or model calls required.")'
nb['cells'][1]['source']=source.splitlines(True)
path.write_text(json.dumps(nb,indent=1),encoding='utf-8')
print('Built HTML, synthetic demo and self-contained notebook.')
