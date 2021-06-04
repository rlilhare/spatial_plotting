import os

from netCDF4 import Dataset as NetCDFFile


def read_nc_data():
    base_path = os.getcwd()
    air_temp_path = os.path.join(
        base_path, "./data/ERA_Land_mn_ann_air_temp_NRB_1981_2019.nc"
    )
    nc = NetCDFFile(air_temp_path)  # Input your file in a netcdf format
    lat = nc.variables["lat"][:]
    lon = nc.variables["lon"][:]
    # Plotting variable in the plot (avg ann air temp)
    temp = nc.variables["temp"][:]
    return lat, lon, temp
