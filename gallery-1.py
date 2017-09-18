from obspy import read_inventory
inv = read_inventory()
inv.plot(projection="local", color_per_network={'GR': 'blue', 'BW': 'green'})