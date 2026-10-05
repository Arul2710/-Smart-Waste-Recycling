/* ===========================================================
   EcoScrap — Shared demo data source
   Single place for scrap rates, categories, locations, blog
   posts and testimonials so every page stays consistent.
   All values are DEMO data and are intentionally front-end only.
   =========================================================== */
(function () {
  'use strict';

  var CATEGORIES = [
    {
      id: 'paper',
      name: 'Paper & Cardboard',
      icon: 'fa-newspaper',
      blurb: 'Newspapers, books, cartons, corrugated boxes, office paper and files.',
      items: 'Newspapers, Magazines, Books, Cartons, Office Paper, Corrugated Boxes',
      rate: 12,
      img: 'assets/images/paper.jpg',
      alt: 'Stack of bundled cardboard boxes and newspapers ready for recycling'
    },
    {
      id: 'metal',
      name: 'Metal & Aluminum',
      icon: 'fa-cubes-stacked',
      blurb: 'Iron, steel, brass, copper and aluminum — the highest paying recyclables.',
      items: 'Iron Scrap, Steel, Copper Wire, Brass, Aluminum Cans, Utensils',
      rate: 42,
      img: 'assets/images/metal.jpg',
      alt: 'Pile of shiny metal scrap pieces including aluminum and steel'
    },
    {
      id: 'plastic',
      name: 'Plastic & Packaging',
      icon: 'fa-bottle-water',
      blurb: 'PET bottles, HDPE containers, PVC pipes and flexible packaging.',
      items: 'PET Bottles, HDPE Containers, PVC Pipes, Plastic Jugs, Carry Bags',
      rate: 8,
      img: 'assets/images/plastic.jpg',
      alt: 'Plastic bottles and packaging containers collected for recycling'
    },
    {
      id: 'ewaste',
      name: 'E-Waste',
      icon: 'fa-microchip',
      blurb: 'Old laptops, monitors, mobile handsets, cables and circuit boards.',
      items: 'Laptops, Monitors, Mobile Handsets, Cables, Printers, PC Parts',
      rate: 25,
      img: 'assets/images/laptop-recycling.jpg',
      alt: 'Old laptops and electronic devices being dismantled for recycling'
    },
    {
      id: 'appliance',
      name: 'Old Appliances',
      icon: 'fa-blender',
      blurb: 'Refrigerators, washing machines, air conditioners and microwaves.',
      items: 'Refrigerators, Washing Machines, Air Conditioners, Mixers, Televisions',
      rate: 30,
      img: 'assets/images/appliance-fridge.jpg',
      alt: 'Old refrigerator and large household appliances waiting to be recycled'
    },
    {
      id: 'battery',
      name: 'Batteries & Recyclables',
      icon: 'fa-car-battery',
      blurb: 'Inverter batteries, lithium cells, toner cartridges and used oil.',
      items: 'Inverter Batteries, Lithium Cells, Laptop Batteries, Toner, Used Oil',
      rate: 55,
      img: 'assets/images/battery.jpg',
      alt: 'Collection of used batteries and small recyclable electronic items'
    }
  ];

  var RATES = [
    { material: 'Newspaper (White)', category: 'Paper', unit: 'Kg', price: 14 },
    { material: 'Corrugated Cardboard', category: 'Paper', unit: 'Kg', price: 16 },
    { material: 'Old Books / Mixed Paper', category: 'Paper', unit: 'Kg', price: 11 },
    { material: 'Iron Scrap (Clean)', category: 'Metal', unit: 'Kg', price: 28 },
    { material: 'Steel / HMS', category: 'Metal', unit: 'Kg', price: 32 },
    { material: 'Copper Scrap', category: 'Metal', unit: 'Kg', price: 385 },
    { material: 'Brass Scrap', category: 'Metal', unit: 'Kg', price: 310 },
    { material: 'Aluminum Cans', category: 'Metal', unit: 'Kg', price: 128 },
    { material: 'PET Bottles (Clear)', category: 'Plastic', unit: 'Kg', price: 15 },
    { material: 'HDPE / Plastic Jugs', category: 'Plastic', unit: 'Kg', price: 9 },
    { material: 'PVC Pipes', category: 'Plastic', unit: 'Kg', price: 12 },
    { material: 'Laptop / Desktop E-Waste', category: 'E-Waste', unit: 'Kg', price: 45 },
    { material: 'Mobile Handsets', category: 'E-Waste', unit: 'Piece', price: 150 },
    { material: 'Television (Working)', category: 'E-Waste', unit: 'Piece', price: 120 },
    { material: 'Washing Machine', category: 'Appliance', unit: 'Piece', price: 650 },
    { material: 'Refrigerator', category: 'Appliance', unit: 'Piece', price: 900 },
    { material: 'Air Conditioner (1 Ton)', category: 'Appliance', unit: 'Piece', price: 750 },
    { material: 'Inverter Battery', category: 'Battery', unit: 'Each', price: 550 },
    { material: 'Lithium Cell / Laptop Battery', category: 'Battery', unit: 'Kg', price: 180 },
    { material: 'Toner Cartridge', category: 'Battery', unit: 'Each', price: 80 }
  ];

  var RATE_CATEGORIES = ['All', 'Paper', 'Metal', 'Plastic', 'E-Waste', 'Appliance', 'Battery'];

  var LOCATIONS = [
    {
      id: 'delhi-ncr',
      name: 'Delhi NCR',
      regions: 'Delhi, Noida, Greater Noida, Ghaziabad, Gurugram, Faridabad',
      coverage: 'Full Coverage',
      slots: '6 pickup slots per day',
      phone: '+91 98100 11223',
      hours: '7:00 AM – 8:00 PM',
      cats: ['paper', 'metal', 'plastic', 'ewaste', 'appliance', 'battery'],
      img: 'assets/images/delhi-ncr.jpg',
      alt: 'Delhi NCR cityscape representing the service region'
    },
    {
      id: 'mumbai',
      name: 'Mumbai',
      regions: 'Andheri, Bandra, Dadar, Powai, Thane, Navi Mumbai',
      coverage: 'Selected Zones',
      slots: '5 pickup slots per day',
      phone: '+91 98200 55678',
      hours: '8:00 AM – 9:00 PM',
      cats: ['paper', 'metal', 'plastic', 'ewaste', 'appliance'],
      img: 'assets/images/mumbai.jpg',
      alt: 'Mumbai coastal city skyline showing the serviced neighbourhood'
    },
    {
      id: 'bangalore',
      name: 'Bangalore',
      regions: 'Whitefield, Koramangala, Indiranagar, HSR Layout, Electronic City',
      coverage: 'Full Coverage',
      slots: '6 pickup slots per day',
      phone: '+91 99000 33445',
      hours: '7:30 AM – 8:30 PM',
      cats: ['paper', 'metal', 'plastic', 'ewaste', 'appliance', 'battery'],
      img: 'assets/images/bangalore.jpg',
      alt: 'Modern tech district skyline representing Bangalore service coverage'
    },
    {
      id: 'pune',
      name: 'Pune',
      regions: 'Kothrud, Viman Nagar, Aundh, Hadapsar, Baner',
      coverage: 'Partial Coverage',
      slots: '4 pickup slots per day',
      phone: '+91 98800 77889',
      hours: '8:00 AM – 7:00 PM',
      cats: ['paper', 'metal', 'plastic', 'ewaste'],
      img: 'assets/images/pune.jpg',
      alt: 'Green residential neighbourhood representing Pune service areas'
    },
    {
      id: 'hyderabad',
      name: 'Hyderabad',
      regions: 'Gachibowli, Kondapur, Madhapur, Kukatpally, Secunderabad',
      coverage: 'Full Coverage',
      slots: '5 pickup slots per day',
      phone: '+91 98765 22334',
      hours: '7:00 AM – 8:00 PM',
      cats: ['paper', 'metal', 'plastic', 'ewaste', 'battery'],
      img: 'assets/images/hyderabad.jpg',
      alt: 'Hyderabad city skyline at dusk representing the pickup zone'
    },
    {
      id: 'chennai',
      name: 'Chennai',
      regions: 'Anna Nagar, Adyar, Velachery, Guindy, T. Nagar',
      coverage: 'Selected Zones',
      slots: '4 pickup slots per day',
      phone: '+91 98400 44556',
      hours: '8:00 AM – 7:30 PM',
      cats: ['paper', 'metal', 'plastic', 'appliance'],
      img: 'assets/images/chennai.jpg',
      alt: 'Chennai coastal city view representing the covered neighbourhoods'
    }
  ];

  var TESTIMONIALS = [
    {
      name: 'Rohit Mehra',
      role: 'Flat owner, Whitefield',
      rating: 5,
      initials: 'RM',
      text: 'I booked a pickup on a Sunday morning and the collector reached my gate within 40 minutes. The weighing was on a calibrated scale in front of me, and the payment hit my UPI immediately.'
    },
    {
      name: 'Fatima Sheikh',
      role: 'Society secretary, Powai',
      rating: 5,
      initials: 'FS',
      text: 'We ran a society-wide scrap drive with EcoScrap. Around 380 kg was collected in a single morning and the payout summary was in our hands the same day. Very well organised.'
    },
    {
      name: 'Arjun Nair',
      role: 'IT professional, Kothrud',
      rating: 4,
      initials: 'AN',
      text: 'The E-Waste pickup is what sold me. Two old laptops and a desktop went to a certified recycler instead of a scrap bin, and I got a fair rate for the working parts.'
    },
    {
      name: 'Priya Deshmukh',
      role: 'Apartment manager, HSR Layout',
      rating: 5,
      initials: 'PD',
      text: 'What I appreciate most is the transparency. The rate card in the app matched the payment I received, with no last-minute deductions. That rarely happens in this business.'
    },
    {
      name: 'Sandeep Yadav',
      role: 'Store owner, Karol Bagh',
      rating: 5,
      initials: 'SY',
      text: 'We generate a lot of cardboard every week. EcoScrap schedules a recurring pickup slot, and I no longer have to store it in the back of the shop.'
    },
    {
      name: 'Meera Iyer',
      role: 'Homeowner, Adyar',
      rating: 5,
      initials: 'MI',
      text: 'The status tracker is genuinely useful. I could see when the collector was en route, the verified weight, and the payout status without calling anyone.'
    }
  ];

  var POSTS = [
    {
      slug: 'scrap-rates-india-2026',
      title: 'Understanding Scrap Rates in India: A Complete 2026 Guide',
      category: 'Rates & Pricing',
      date: '2026-08-28',
      read: '7 min read',
      author: 'Rohit Mehra',
      initials: 'RM',
      img: 'assets/images/paper-hero.jpg',
      alt: 'Scrap metal pieces and weighing scale used to calculate material rates',
      excerpt: 'Why metal rates move every month, how paper and plastic prices are decided, and what actually changes the final number on your payout receipt.'
    },
    {
      slug: 'ewaste-recycling-india',
      title: 'Why E-Waste Recycling in India Is Finally Getting Serious',
      category: 'E-Waste',
      date: '2026-08-14',
      read: '6 min read',
      author: 'Anita Kulkarni',
      initials: 'AK',
      img: 'assets/images/ewaste.jpg',
      alt: 'Circuit boards and electronic components being sorted for recycling',
      excerpt: 'From the E-Waste Management Rules to certified collection centres — what happens to your old laptop after it leaves your doorstep.'
    },
    {
      slug: 'cardboard-recycling-tips',
      title: '7 Simple Ways to Cut the Cardboard in Your Kitchen Today',
      category: 'Home & Hacks',
      date: '2026-07-30',
      read: '5 min read',
      author: 'Priya Deshmukh',
      initials: 'PD',
      img: 'assets/images/boxes.jpg',
      alt: 'Flattened cardboard sheets stacked for recycling collection',
      excerpt: 'Cardboard is the highest-volume recyclable most Indian homes throw away. Small habits add up to surprisingly large monthly payouts.'
    },
    {
      slug: 'weighing-scales-explained',
      title: 'How Scrap Is Actually Weighed: A Transparent Scale Guide',
      category: 'How It Works',
      date: '2026-07-16',
      read: '8 min read',
      author: 'Vikram Shah',
      initials: 'VS',
      img: 'assets/images/blog-weighed.jpg',
      alt: 'Scrap metal being weighed on a calibrated scale',
      excerpt: 'Calibrated scales, tare weight, moisture loss and contamination — a collector-grade explainer you can use to check any measurement.'
    },
    {
      slug: 'corporate-scrap-clearance',
      title: 'Corporate Scrap Clearance: A Compliance Checklist',
      category: 'Business',
      date: '2026-06-29',
      read: '6 min read',
      author: 'Neha Bansal',
      initials: 'NB',
      img: 'assets/images/blog-corporate.jpg',
      alt: 'Corporate office scrap clearance and compliance documentation',
      excerpt: 'GST invoicing, e-waste handover certificates, and the documentation every facility manager should demand from a scrap partner.'
    },
    {
      slug: 'battery-disposal-safety',
      title: 'Battery Disposal: What You Should Never Put in a Regular Bin',
      category: 'Safety',
      date: '2026-06-11',
      read: '5 min read',
      author: 'Arjun Nair',
      initials: 'AN',
      img: 'assets/images/battery.jpg',
      alt: 'Used batteries being carefully separated for safe recycling',
      excerpt: 'Inverter batteries and lithium cells carry a real fire risk. Here is the safe handling routine every household should follow.'
    }
  ];

  var FAQ = [
    {
      q: 'How is my scrap actually weighed?',
      a: 'Every collector carries a government-verified, tamper-proof digital scale calibrated to the nearest 100 grams. The weight is displayed in front of you, recorded in the app, and printed on your receipt — so you always know exactly what was measured.'
    },
    {
      q: 'Can I see the rate before the pickup happens?',
      a: 'Yes. The published rate card in the app shows the indicative price for every material. The final payout is calculated from the published rate multiplied by the verified weight, with no hidden collection charges.'
    },
    {
      q: 'What materials do you refuse to take?',
      a: 'We do not accept hazardous or biomedical waste such as chemicals, medical sharps, pressurised containers, sealed fuel tanks or expired paint. E-waste and batteries are accepted but routed through a separate certified stream.'
    },
    {
      q: 'How quickly do I receive payment?',
      a: 'Payments are released within 30 minutes of a completed verification. UPI is instant, bank transfers settle the same working day, and cash payouts are handed over on the spot by the collector.'
    },
    {
      q: 'Is there a minimum quantity for a pickup?',
      a: 'There is no minimum. We collect anything from a single cardboard box upward. For bulk or society-level clear-outs we recommend scheduling a dedicated slot so a larger vehicle can be assigned.'
    },
    {
      q: 'What happens to the material after collection?',
      a: 'Sorted material is dispatched to certified recyclers and authorised re-rollers within 48 hours. Every consignment carries a handover manifest, and registered users can request the summary from their dashboard.'
    }
  ];

  window.ECOSCRAP = {
    categories: CATEGORIES,
    rates: RATES,
    rateCategories: RATE_CATEGORIES,
    locations: LOCATIONS,
    testimonials: TESTIMONIALS,
    posts: POSTS,
    faq: FAQ,
    currency: function (n) {
      var num = Number(n) || 0;
      return '₹' + num.toLocaleString('en-IN', { maximumFractionDigits: 2 });
    }
  };
})();
