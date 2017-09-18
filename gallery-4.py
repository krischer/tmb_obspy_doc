from obspy import read_inventory
inv = read_inventory()
inv.plot_response(0.001, station="RJOB")