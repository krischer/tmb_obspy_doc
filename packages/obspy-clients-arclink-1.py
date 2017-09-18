from obspy import UTCDateTime
from obspy.clients.arclink.client import Client
client = Client(user='test@obspy.org')
t = UTCDateTime("2009-08-20 04:03:12")
st = client.get_waveforms("BW", "RJOB", "", "EH*", t - 3, t + 15)
st.plot()  # doctest: +SKIP