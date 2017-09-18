from obspy.clients.syngine import Client
client = Client()
st = client.get_waveforms(model="ak135f_5s", network="IU", station="ANMO",
                          eventid="GCMT:C201002270634A")
st.plot()