from obspy import read
st = read()
tr = st.select(component="Z")[0]
tr.filter("bandpass", freqmin=1, freqmax=20)
tr.trigger("recstalta", sta=0.5, lta=4)
tr.plot()