from obspy.signal.tf_misfit import plot_tfr
from obspy import read
tr = read("https://examples.obspy.org/a02i.2008.240.mseed")[0]
plot_tfr(tr.data, dt=tr.stats.delta, fmin=.01,
        fmax=50., w0=8., nf=64, fft_zero_pad_fac=4)