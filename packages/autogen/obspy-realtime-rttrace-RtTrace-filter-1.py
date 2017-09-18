from obspy import read
st = read()
tr = st[0]
tr.filter("highpass", freq=1.0)
tr.plot()