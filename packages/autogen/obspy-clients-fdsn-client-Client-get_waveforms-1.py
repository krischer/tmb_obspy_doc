from obspy import UTCDateTime
from obspy.clients.fdsn import Client
client = Client("IRIS")
t = UTCDateTime("2012-12-14T10:36:01.6Z")
st = client.get_waveforms("TA", "E42A", "*", "BH?", t+300, t+400,
                          attach_response=True)
st.remove_response(output="VEL")
st.plot()