from obspy import read
from obspy.signal.trigger import recursive_sta_lta, plot_trigger
st = read()
tr = st.select(component="Z")[0]
tr.filter("bandpass", freqmin=1, freqmax=20)
sta = 0.5
lta = 4
cft = recursive_sta_lta(tr.data, int(sta * tr.stats.sampling_rate),
                int(lta * tr.stats.sampling_rate))
thr_on = 4
thr_off = 0.7
plot_trigger(tr, cft, thr_on, thr_off)