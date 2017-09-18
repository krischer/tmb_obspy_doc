from obspy import read_inventory
inv = read_inventory()
resp = inv[0][0][0].response
resp.plot(0.001, output="VEL")