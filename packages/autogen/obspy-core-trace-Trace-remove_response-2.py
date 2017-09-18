from obspy import read, read_inventory
st = read("/path/to/IU_ULN_00_LH1_2015-07-18T02.mseed", "MSEED")
tr = st[0]
inv = read_inventory("/path/to/IU_ULN_00_LH1.xml", "STATIONXML")
pre_filt = [0.001, 0.005, 45, 50]
output = "DISP"
tr.remove_response(inventory=inv, pre_filt=pre_filt, output=output,
                   water_level=60, plot=True)