/* ===========================================================
   EcoScrap — shared dashboard demo data
   One source of truth for pickup requests, collectors, payments
   and audit entries used by both the customer and admin dashboards.
   Everything is persisted in localStorage (front-end only).
   =========================================================== */
(function () {
  'use strict';

  var Store = window.EcoStore || {
    get: function (k, f) { try { var r = localStorage.getItem('ecoscrap-' + k); return r === null ? f : JSON.parse(r); } catch (e) { return f; } },
    set: function (k, v) { try { localStorage.setItem('ecoscrap-' + k, JSON.stringify(v)); } catch (e) { /* ignore */ } }
  };

  function iso(offsetDays) {
    var d = new Date(Date.now() - offsetDays * 86400000);
    return d.toISOString().slice(0, 10);
  }

  function seedPickups() {
    var existing = Store.get('pickups', null);
    if (existing && existing.length) return existing;
    var data = [
      { id: 'REQ-1050', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'Batteries & Recyclables', material: 'Inverter Battery', date: iso(-2), slot: 'Morning', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 2, verified: 0, rate: 550, amount: 0, status: 'Scheduled', method: 'UPI' },
      { id: 'REQ-1049', customer: 'Rohan Verma', email: 'rohan@example.com', category: 'Metal & Aluminum', material: 'Copper Wire', date: iso(-1), slot: 'Afternoon', city: 'Mumbai', address: '12, Sea View Society, Bandra', notes: '', weight: 7, verified: 0, rate: 385, amount: 0, status: 'Scheduled', method: 'Bank' },
      { id: 'REQ-1048', customer: 'Fatima Sheikh', email: 'fatima@example.com', category: 'Paper & Cardboard', material: 'Corrugated Boxes', date: iso(0), slot: 'Evening', city: 'Pune', address: 'Society Gate 2, Powai', notes: 'Large bulk', weight: 240, verified: 0, rate: 16, amount: 0, status: 'En Route', method: 'UPI' },
      { id: 'REQ-1047', customer: 'Arjun Nair', email: 'arjun@example.com', category: 'E-Waste', material: 'Laptop, Desktop', date: iso(0), slot: 'Morning', city: 'Bangalore', address: '404, HSR Layout Sector 3', notes: '', weight: 9, verified: 8.6, rate: 45, amount: 387, status: 'Completed', method: 'UPI' },
      { id: 'REQ-1046', customer: 'Priya Deshmukh', email: 'priya@example.com', category: 'Plastic & Packaging', material: 'PET Bottles', date: iso(1), slot: 'Afternoon', city: 'Hyderabad', address: 'Plot 8, Madhapur', notes: '', weight: 14, verified: 0, rate: 15, amount: 0, status: 'Scheduled', method: 'UPI' },
      { id: 'REQ-1045', customer: 'Sandeep Yadav', email: 'sandeep@example.com', category: 'Old Appliances', material: 'Washing Machine', date: iso(1), slot: 'Evening', city: 'Delhi NCR', address: 'Shop 4, Karol Bagh Market', notes: '', weight: 1, verified: 1, rate: 650, amount: 650, status: 'Completed', method: 'Cash' },
      { id: 'REQ-1042', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'Paper & Cardboard', material: 'Newspaper, Cardboard', date: iso(1), slot: 'Evening', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 18, verified: 0, rate: 14, amount: 0, status: 'En Route', method: 'UPI' },
      { id: 'REQ-1039', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'Metal & Aluminum', material: 'Iron, Aluminum', date: iso(4), slot: 'Morning', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 12, verified: 11.6, rate: 28, amount: 325, status: 'Completed', method: 'UPI' },
      { id: 'REQ-1036', customer: 'Rohan Verma', email: 'rohan@example.com', category: 'Metal & Aluminum', material: 'Brass Scrap', date: iso(6), slot: 'Afternoon', city: 'Mumbai', address: '12, Sea View Society, Bandra', notes: '', weight: 5, verified: 4.8, rate: 310, amount: 1488, status: 'Completed', method: 'Bank' },
      { id: 'REQ-1034', customer: 'Arjun Nair', email: 'arjun@example.com', category: 'E-Waste', material: 'Mobile Handsets', date: iso(8), slot: 'Morning', city: 'Bangalore', address: '404, HSR Layout Sector 3', notes: '', weight: 6, verified: 6, rate: 150, amount: 900, status: 'Completed', method: 'UPI' },
      { id: 'REQ-1031', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'E-Waste', material: 'Laptop, Cables', date: iso(12), slot: 'Afternoon', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 6, verified: 5.8, rate: 45, amount: 261, status: 'Completed', method: 'Bank' },
      { id: 'REQ-1028', customer: 'Fatima Sheikh', email: 'fatima@example.com', category: 'Paper & Cardboard', material: 'Mixed Paper', date: iso(15), slot: 'Evening', city: 'Pune', address: 'Society Gate 2, Powai', notes: '', weight: 120, verified: 118, rate: 11, amount: 1298, status: 'Completed', method: 'UPI' },
      { id: 'REQ-1024', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'Plastic & Packaging', material: 'PET Bottles', date: iso(20), slot: 'Evening', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 9, verified: 8.7, rate: 15, amount: 130, status: 'Completed', method: 'UPI' },
      { id: 'REQ-1017', customer: 'Green User', email: 'demo@ecoscrap.in', category: 'Old Appliances', material: 'Refrigerator', date: iso(33), slot: 'Afternoon', city: 'Delhi NCR', address: 'B-42, Green Apartments, Okhla', notes: '', weight: 1, verified: 1, rate: 900, amount: 900, status: 'Completed', method: 'Cash' }
    ];
    Store.set('pickups', data);
    return data;
  }

  function seedCollectors() {
    var c = Store.get('collectors', null);
    if (c && c.length) return c;
    c = [
      { id: 'COL-01', name: 'David Mehta', city: 'Delhi NCR', vehicle: 'DL-8C-2201', currentCity: 'Delhi NCR', assignments: 14, rating: 4.9, status: 'On Route' },
      { id: 'COL-02', name: 'Imran Khan', city: 'Mumbai', vehicle: 'MH-02-AB-3390', currentCity: 'Mumbai', assignments: 11, rating: 4.7, status: 'Available' },
      { id: 'COL-03', name: 'Suresh Rao', city: 'Bangalore', vehicle: 'KA-05-MN-7788', currentCity: 'Bangalore', assignments: 16, rating: 4.8, status: 'On Route' },
      { id: 'COL-04', name: 'Vikram Singh', city: 'Pune', vehicle: 'MH-12-PQ-4521', currentCity: 'Pune', assignments: 9, rating: 4.6, status: 'Available' },
      { id: 'COL-05', name: 'Anil Kumar', city: 'Hyderabad', vehicle: 'TS-09-EF-1122', currentCity: 'Hyderabad', assignments: 12, rating: 4.7, status: 'Off Duty' },
      { id: 'COL-06', name: 'Ravi Iyer', city: 'Chennai', vehicle: 'TN-10-CD-9090', currentCity: 'Chennai', assignments: 8, rating: 4.5, status: 'Available' }
    ];
    Store.set('collectors', c);
    return c;
  }

  function seedAudit() {
    var a = Store.get('audit', null);
    if (a && a.length) return a;
    a = [
      { icon: 'fa-scale-balanced', text: 'Verified weight for REQ-1047 at 8.6 kg', time: '10 min ago' },
      { icon: 'fa-money-bill-transfer', text: 'Released payout of ₹1,488 for REQ-1036', time: '2 hours ago' },
      { icon: 'fa-tags', text: 'Updated copper rate to ₹385/kg', time: 'Today, 9:15 AM' },
      { icon: 'fa-user-plus', text: 'New collector Rahul added to Pune fleet', time: 'Yesterday' },
      { icon: 'fa-truck-fast', text: 'Assigned REQ-1048 to Suresh Rao', time: 'Yesterday' }
    ];
    Store.set('audit', a);
    return a;
  }

  function logAudit(icon, text) {
    var list = Store.get('audit', []);
    list.unshift({ icon: icon, text: text, time: 'Just now' });
    Store.set('audit', list.slice(0, 12));
  }

  // Edited rate overrides (admin) layered on top of js/data.js rates.
  function effectiveRates(base) {
    var edits = Store.get('rate-edits', {});
    return base.map(function (r) {
      if (Object.prototype.hasOwnProperty.call(edits, r.material)) {
        var e = edits[r.material];
        return { material: r.material, category: e.category || r.category, unit: e.unit || r.unit, price: e.price };
      }
      return r;
    }).concat(Store.get('rate-added', []));
  }

  window.EcoDashData = {
    seedPickups: seedPickups,
    seedCollectors: seedCollectors,
    seedAudit: seedAudit,
    logAudit: logAudit,
    effectiveRates: effectiveRates
  };
})();
