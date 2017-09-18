from obspy.clients.syngine import Client
client = Client()
st = client.get_waveforms(model="ak135f_5s", network="IU", station="A*",
                          eventid="GCMT:C201002270634A",
                          starttime="P-10", endtime="P+20")
st.plot()