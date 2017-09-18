import matplotlib.pyplot as plt
from obspy.imaging.beachball import beach
np1 = [150, 87, 1]
mt = [-2.39, 1.04, 1.35, 0.57, -2.94, -0.94]
beach1 = beach(np1, xy=(-70, 80), width=30)
beach2 = beach(mt, xy=(50, 50), width=50)
plt.plot([-100, 100], [0, 100], "rv", ms=20)
ax = plt.gca()
ax.add_collection(beach1)
ax.add_collection(beach2)
ax.set_aspect("equal")
ax.set_xlim((-120, 120))
ax.set_ylim((-20, 120))