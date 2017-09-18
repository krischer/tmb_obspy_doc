from obspy import read
st = read()
st.filter("highpass", freq=1.0)
st.plot()
st.trigger('recstalta', sta=1, lta=4)
st.plot()