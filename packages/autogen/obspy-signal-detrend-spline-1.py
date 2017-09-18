import obspy
from obspy.signal.detrend import spline

tr = obspy.read()[0].filter("highpass", freq=2)
tr.data += 6000 + 4 * tr.times() ** 2 - 0.1 * tr.times() ** 3 -             0.00001 * tr.times() ** 5

spline(tr.data, order=2, dspline=1000, plot=True)