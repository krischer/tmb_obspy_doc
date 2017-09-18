from obspy import read
st = read()
st.plot(color='gray', tick_format='%I:%M %p',
        starttime=st[0].stats.starttime,
        endtime=st[0].stats.starttime+20)