from obspy import read
from obspy.signal.invsim import corn_freq_2_paz
st = read()
paz_sts2 = {'poles': [-0.037004+0.037016j, -0.037004-0.037016j,
                      -251.33+0j,
                      -131.04-467.29j, -131.04+467.29j],
            'zeros': [0j, 0j],
            'gain': 60077000.0,
            'sensitivity': 2516778400.0}
paz_1hz = corn_freq_2_paz(1.0, damp=0.707)
paz_1hz['sensitivity'] = 1.0
st.simulate(paz_remove=paz_sts2, paz_simulate=paz_1hz)
st.plot()