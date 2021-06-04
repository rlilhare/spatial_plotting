import os

from mpl_toolkits.basemap import Basemap


def read_shp_file():
    base_path = os.getcwd()
    ws_bound_path = os.path.join(base_path, "./data/sub-basin_shp_for_plots/")
    ws_bound_files = [
        (os.path.join(ws_bound_path, "Stuart"), "Stuart"),
        (os.path.join(ws_bound_path, "Middle_Nech"), "Middle_Nech"),
        (os.path.join(ws_bound_path, "Chilako"), "Chilako"),
        (os.path.join(ws_bound_path, "Lower_Nech"), "Lower_Nech"),
        (os.path.join(ws_bound_path, "Regulated_for_sp_plot"), "Regulated_for_sp_plot"),
        (os.path.join(ws_bound_path, "Nautley"), "Nautley"),
    ]
    map = Basemap(
        projection="merc",
        llcrnrlon=-128.0,
        llcrnrlat=52.6,
        urcrnrlon=-122.3,
        urcrnrlat=56.4,
        resolution="i",
    )  # projection, lat/lon extents and resolution of polygons to draw
    map.drawlsmask(
        land_color="w", ocean_color="w"
    )  # can use HTML names or codes for colors
    map.drawcounties()  # you can even add counties (and other shapefiles!)

    for file_path, river_name in ws_bound_files:
        map.readshapefile(file_path, river_name, drawbounds=True)

    return map
