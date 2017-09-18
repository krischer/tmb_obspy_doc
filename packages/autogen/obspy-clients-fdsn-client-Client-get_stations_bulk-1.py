from obspy import UTCDateTime
from obspy.clients.fdsn import Client

client = Client("IRIS")
t1 = UTCDateTime("2010-02-27T06:30:00.000")
t2 = t1 + 1
t3 = t1 + 3
bulk = [("IU", "ANMO", "*", "BHZ", t1, t2),
        ("IU", "AFI", "1?", "BHE", t1, t3),
        ("GR", "GRA1", "*", "BH*", t2, t3)]
inv = client.get_stations_bulk(bulk)
inv.plot()