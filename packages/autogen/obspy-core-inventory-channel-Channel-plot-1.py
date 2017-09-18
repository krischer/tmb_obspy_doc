from obspy import read_inventory
cha = read_inventory()[0][0][0]
cha.plot(0.001, output="VEL")