from obspy import read
import obspy.signal
st = read()
tr = st[0]
tr.data = obspy.signal.filter.highpass(tr.data, 1.0,
        df=tr.stats.sampling_rate, corners=1, zerophase=True)
st.plot()