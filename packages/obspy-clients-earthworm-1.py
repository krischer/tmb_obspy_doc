from obspy.clients.earthworm import Client
from obspy import UTCDateTime
client = Client("pubavo1.wr.usgs.gov", 16022, timeout=5)
response = client.get_availability('AV', 'ACH', channel='EHE')
t = response[0][4]
st = client.get_waveforms('AV', 'ACH', '', 'EH*', t + 100, t + 130)
st.plot()