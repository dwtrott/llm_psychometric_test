// Run test_battery_v3.py first. These data are synthetic contract fixtures.
const assert=require('assert'),fs=require('fs'),path=require('path'),c=require('../viewer/src/app.js');
const graph=JSON.parse(fs.readFileSync(path.join(__dirname,'v3-format-fixture.graph.json'),'utf8'));
const p=c.normalize(graph),catalog=c.profileCatalog(graph);
assert.equal(catalog.domains.length,12);assert.equal(Object.keys(catalog.modules).length,39);
assert.equal(p.rows.length,194);assert.equal(p.quality.valid,194);
assert(c.matchCells(p,p).every(r=>r.delta===0));
assert(c.graphUnion(p,null,'evokes','neutral').length>0);
assert(c.graphUnion(p,null,'evokes','garden').length>0);
assert.equal(Object.keys(catalog.primary).length,0);
console.log('v0.3: 12 regions, 39 families, 194 sessions, self-comparison, contextual associations, no trait totals: passed.');
