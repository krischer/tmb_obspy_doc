from obspy import UTCDateTime
from obspy.clients.fdsn import Client
client = Client("IRIS")
t = UTCDateTime("2012-12-14T10:36:01.6Z")
t1 = t + 300
t2 = t + 400
bulk = [("TA", "S42A", "*", "BHZ", t1, t2),
        ("TA", "W42A", "*", "BHZ", t1, t2),
        ("TA", "Z42A", "*", "BHZ", t1, t2)]
st = client.get_waveforms_bulk(bulk, attach_response=True)
st.remove_response(output="VEL")
st.plot()