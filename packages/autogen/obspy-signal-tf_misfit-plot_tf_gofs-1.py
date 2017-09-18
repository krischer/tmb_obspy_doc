import numpy as np
from obspy.signal.tf_misfit import plot_tf_gofs
tmax = 6.
dt = 0.01
npts = int(tmax / dt + 1)
t = np.linspace(0., tmax, npts)
A1 = 4.
t1 = 2.
f1 = 2.
phi1 = 0.
phase_shift = 0.1
H1 = (np.sign(t - t1) + 1)/ 2
st1 = (A1 * (t - t1) * np.exp(-2*(t - t1)) *
      np.cos(2. * np.pi * f1 * (t - t1) + phi1 * np.pi) * H1)
# Reference signal
st2 = st1.copy()
# Distorted signal:
st1 = st1 * 3.
plot_tf_gofs(st1, st2, dt=dt, fmin=1., fmax=10.)