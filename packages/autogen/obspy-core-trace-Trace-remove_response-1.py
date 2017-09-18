from obspy import read, read_inventory
st = read()
tr = st[0]
inv = read_inventory()
tr.remove_response(inventory=inv)
tr.plot()