from ts_metadata_reader import TSRead

def pack_to_str(p):
    s = ''
    for key in dir(p):
        if key.startswith('__'): continue
        s += key + ': ' + str(getattr(p, key)) + '\n'
    return s


filepath = 'c:\\Users\\tot\\Downloads\\shifted_bus_000.ts'
ts = TSRead(filepath)
print('ts.totalpackets', ts.totalpackets)
num_packs_with_pts = 0
num_packs_with_dts = 0
for i in range(1, int(ts.totalpackets)):
    p = ts.goto(i)
    # print('packet #' + str(i))
    # print(pack_to_str(p))
    if p.decodedpts: num_packs_with_pts += 1
    if p.decodeddts: num_packs_with_dts += 1
    if not p.decodedpts and not p.decodeddts: continue
    print('packet #' + str(i).rjust(4), str(p.pid).rjust(4), p.av, p.adapt, p.decodedpts, p.decodeddts)

print('num_packs_with_pts', num_packs_with_pts)
print('num_packs_with_dts', num_packs_with_dts)