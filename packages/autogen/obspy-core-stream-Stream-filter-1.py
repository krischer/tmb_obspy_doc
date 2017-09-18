from obspy import read
st = read()
st.filter("highpass", freq=1.0)
st.plot()