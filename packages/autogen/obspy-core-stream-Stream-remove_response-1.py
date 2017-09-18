from obspy import read, read_inventory
st = read()
inv = read_inventory()
st.remove_response(inventory=inv)
st.plot()