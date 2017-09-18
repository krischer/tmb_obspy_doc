from obspy.taup import TauPyModel
TauPyModel().get_ray_paths(
    500, 130, phase_list=["ttbasic"]).plot(plot_type="cartesian")