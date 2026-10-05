const fs = require('fs');
const path = require('path');

const store = {};
global.localStorage = {
  getItem: (k) => (k in store ? store[k] : null),
  setItem: (k, v) => { store[k] = String(v); },
  removeItem: (k) => { delete store[k]; }
};
global.window = {};

const code = fs.readFileSync(path.join(__dirname, '..', 'js', 'dash-data.js'), 'utf8');
// eslint-disable-next-line no-eval
eval(code);

const DD = global.window.EcoDashData;
const pk = DD.seedPickups();
const col = DD.seedCollectors();
const audit = DD.seedAudit();
const rates = DD.effectiveRates([
  { material: 'Iron Scrap (Clean)', category: 'Metal', unit: 'Kg', price: 28 },
  { material: 'PET Bottles (Clear)', category: 'Plastic', unit: 'Kg', price: 15 }
]);

console.log('pickups:', pk.length);
console.log('collectors:', col.length);
console.log('audit:', audit.length);
console.log('rates(base):', rates.length);

if (pk.length !== 14) throw new Error('expected 14 pickups, got ' + pk.length);
if (col.length !== 6) throw new Error('expected 6 collectors');
if (audit.length !== 5) throw new Error('expected 5 audit entries');

// idempotent seeding
const pk2 = DD.seedPickups();
if (pk2.length !== 14) throw new Error('seeding not idempotent');

// audit logging caps/stores
DD.logAudit('fa-test', 'hello');
if (DD.seedAudit()[0].text !== 'hello') throw new Error('logAudit failed');

// rate override layering
localStorage.setItem('ecoscrap-rate-edits', JSON.stringify({ 'Iron Scrap (Clean)': { price: 99 } }));
localStorage.setItem('ecoscrap-rate-added', JSON.stringify([{ material: 'Gold Scrap', category: 'Metal', unit: 'Kg', price: 9999 }]));
const rates2 = DD.effectiveRates([
  { material: 'Iron Scrap (Clean)', category: 'Metal', unit: 'Kg', price: 28 },
  { material: 'PET Bottles (Clear)', category: 'Plastic', unit: 'Kg', price: 15 }
]);
const iron = rates2.find((r) => r.material === 'Iron Scrap (Clean)');
if (iron.price !== 99) throw new Error('rate override failed');
if (rates2.length !== 3) throw new Error('rate added failed');

console.log('ALL DATA TESTS PASSED');
