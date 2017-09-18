import obspy
cat = obspy.read_events("https://www.ldeo.columbia.edu/~gcmt/projects/CMT/"
                        "catalog/NEW_MONTHLY/2011/feb11.ndk")
cat.plot()