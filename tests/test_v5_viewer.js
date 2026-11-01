// Compatibility with the existing viewer, not new analyzer implementation.
const assert=require('assert'),fs=require('fs'),path=require('path'),c=require('../viewer/src/app.js');
const profiles=[];
for(const split of ['development','heldout']) {
  const g=JSON.parse(fs.readFileSync(path.join(__dirname,`v5-${split}-fixture.graph.json`),'utf8'));
  const p=c.normalize(g),catalog=c.profileCatalog(g);profiles.push(p);
  assert.equal(catalog.domains.length,11);assert.equal(Object.keys(catalog.modules).length,14);
  assert(c.matchCells(p,p).every(r=>r.delta===0));
  assert(c.graphUnion(p,null,'evokes',split+'|private').length>0);
  assert(p.rows.every(r=>r.conditions.split===split && r.conditions.stratum));
  assert.equal(g.nodes.filter(n=>n.kind==='design_pair').length,42);
}
assert.equal(c.matchCells(...profiles).length,0);
console.log('v0.5 viewer import, self-comparison, strata, design pairs and split separation passed.');
