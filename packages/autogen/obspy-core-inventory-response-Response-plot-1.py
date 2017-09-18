from obspy import read_inventory
resp = read_inventory()[0][0][0].response
resp.plot(0.001, output="VEL")