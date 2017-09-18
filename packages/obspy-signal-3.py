from obspy import read
from obspy.signal.invsim import simulate_seismometer, corn_freq_2_paz
inst2hz = corn_freq_2_paz(2.0)
st = read()
tr = st[0]
sts2 = {'gain': 60077000.0,
        'poles': [(-0.037004+0.037016j),
                  (-0.037004-0.037016j),
                  (-251.33+0j),
                  (-131.04-467.29j),
                  (-131.04+467.29j)],
        'sensitivity': 2516778400.0,
        'zeros': [0j, 0j]}
for tr in st:
    df = tr.stats.sampling_rate
    tr.data = simulate_seismometer(tr.data, df, paz_remove=sts2,
                                   paz_simulate=inst2hz, water_level=60.0)
st.plot()