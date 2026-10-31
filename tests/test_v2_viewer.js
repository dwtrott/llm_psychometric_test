// First run: python tests/test_battery_v2.py --export-fixture
const assert=require('assert'),fs=require('fs'),path=require('path');
const c=require('../viewer/src/app.js');
const graph=JSON.parse(fs.readFileSync(path.join(__dirname,'v2-format-fixture.graph.json'),'utf8'));
const p=c.normalize(graph),catalog=c.profileCatalog(graph);
assert.equal(catalog.domains.length,12);assert.equal(Object.keys(catalog.modules).length,48);
assert.equal(new Set(p.rows.map(r=>r.module)).size,48);
assert(c.matchCells(p,p).every(row=>row.delta===0));
assert(c.graphUnion(p,null,'evokes','private').length>0);
const bad=structuredClone(graph);bad.profile_catalog.domains[0].modules.push('unknown');assert.throws(()=>c.normalize(bad));
console.log('v0.2 viewer catalog, all families, self-comparison, associations and invalid catalog rejection passed.');
