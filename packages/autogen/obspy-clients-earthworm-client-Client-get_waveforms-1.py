from obspy.clients.earthworm import Client
from obspy import UTCDateTime
client = Client("pubavo1.wr.usgs.gov", 16022, timeout=5)
dt = UTCDateTime() - 2000  # now - 2000 seconds
st = client.get_waveforms('AV', 'ACH', '', 'EHE', dt, dt + 10)
st.plot()
st = client.get_waveforms('AV', 'ACH', '', 'EH*', dt, dt + 10)
st.plot()