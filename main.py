from src.ncfile_read_store import read_nc_data
from src.shapefile_read_store import read_shp_file
from src.plot_data import plot_data

def main():
    lat, lon, temp = read_nc_data()
    map = read_shp_file()
    plot_data(lat, lon, temp, map)



if __name__ == "__main__":
    main()