import matplotlib.pyplot as plt

plt.figure(figsize=(10, 12))
from obspy.signal.interpolation import plot_lanczos_windows
plot_lanczos_windows(a=20)