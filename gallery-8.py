import obspy
from obspy.signal.detrend import polynomial

tr = obspy.read()[0].filter("highpass", freq=2)
tr.data += 6000 + 4 * tr.times() ** 2 - 0.1 * tr.times() ** 3 - \
    0.00001 * tr.times() ** 5

polynomial(tr.data, order=3, plot=True)