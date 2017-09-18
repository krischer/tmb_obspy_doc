from obspy import UTCDateTime
from obspy.clients.fdsn import Client
client = Client()
starttime = UTCDateTime("2002-01-01")
endtime = UTCDateTime("2002-01-02")
cat = client.get_events(starttime=starttime, endtime=endtime,
                        minmagnitude=6, catalog="ISC")
cat.plot()