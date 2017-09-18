from obspy import read_inventory
inv = read_inventory()
inv.plot(projection="ortho", label=False, color_per_network=True)