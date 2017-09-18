from obspy import read
st = read()
st[0].spectrogram(log=True)