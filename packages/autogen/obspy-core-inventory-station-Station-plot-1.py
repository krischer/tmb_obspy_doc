from obspy import read_inventory
sta = read_inventory()[0][0]
sta.plot(0.001, output="VEL", channel="*Z")