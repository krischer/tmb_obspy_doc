from obspy import UTCDateTime
from obspy.clients.iris import Client
client = Client()
dt = UTCDateTime("2005-01-01")
client.evalresp("IU", "ANMO", "00", "BHZ", dt)