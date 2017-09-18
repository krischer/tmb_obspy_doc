from obspy import UTCDateTime
from obspy.clients.fdsn import Client
client = Client()
starttime = UTCDateTime("2001-01-01")
endtime = UTCDateTime("2001-01-02")
inventory = client.get_stations(
    starttime=starttime, endtime=endtime,
    network="IU", sta="ANMO", loc="00", channel="*Z",
    level="response")
inventory[0].plot_response(min_freq=1E-4)