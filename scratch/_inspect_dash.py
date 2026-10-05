import io, re
for f in ['customer-dashboard.html', 'admin-dashboard.html']:
    s = io.open(f, encoding='utf-8').read()
    print(f)
    print('  stats :', sorted(set(re.findall(r'data-stat="([^"]+)"', s))))
    print('  views :', len(re.findall(r'data-dash-view="', s)))
    print('  ids   :', [i for i in re.findall(r'id="([^"]+)"', s) if i.startswith(('cust-', 'admin-', 'dash', 'schedule', 'payment', 'address', 'profile', 'settings'))][:40])
