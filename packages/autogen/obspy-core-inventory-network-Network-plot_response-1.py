from obspy import read_inventory
net = read_inventory()[0]
net.plot_response(0.001, station="FUR")