// Compatibility only: the analyzer and collection code remain standard-library Python.
const assert=require('assert'),fs=require('fs'),path=require('path'),c=require('../viewer/src/app.js');
for(const split of ['development','heldout']) {
  const g=JSON.parse(fs.readFileSync(path.join(__dirname,`v4-${split}-fixture.graph.json`),'utf8'));
  const p=c.normalize(g),catalog=c.profileCatalog(g);
  assert.equal(catalog.domains.length,12);assert.equal(Object.keys(catalog.modules).length,16);
  assert(c.matchCells(p,p).every(r=>r.delta===0));
  assert(c.graphUnion(p,null,'evokes',split+'|private').length>0);
  assert(p.rows.every(r=>r.conditions.split===split && ['P1','P2'].includes(r.conditions.paraphrase)));
}
const dev=c.normalize(JSON.parse(fs.readFileSync(path.join(__dirname,'v4-development-fixture.graph.json'))));
const held=c.normalize(JSON.parse(fs.readFileSync(path.join(__dirname,'v4-heldout-fixture.graph.json'))));
assert.equal(c.matchCells(dev,held).length,0);
console.log('v0.4 legacy-viewer import, design labels, self-comparison, split association layers and no cross-partition numeric matching: passed.');
