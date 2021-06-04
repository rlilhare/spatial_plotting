import matplotlib.pyplot as plt
import numpy as np

plt.style.use("seaborn-white")


def plot_data(lat, lon, temp, map):
    parallels = np.arange(
        50, 57, 2.0
    )  # make latitude lines ever 5 degrees from 30N-50N
    meridians = np.arange(
        -128, -118, 2.0
    )  # make longitude lines every 5 degrees from 95W to 70W
    map.drawparallels(
        parallels, labels=[1, 0, 0, 0], dashes=[4, 500], color="k", fontsize=6
    )
    map.drawmeridians(
        meridians, labels=[0, 0, 0, 1], dashes=[4, 500], color="k", fontsize=6
    )  # meridians,labels=[0,0,0,1],fontsize=6)

    lons, lats = np.meshgrid(
        lon, lat
    )  # for this dataset, lon is 0 to 360, subtract 180 to display on the map
    x, y = map(lons, lats)
    temp = map.contourf(x, y, temp[0, :, :], range(-2, 6, 1), cmap="Reds")
    # pad takes label down
    cb = map.colorbar(temp, "bottom", size="4%", pad="8%")

    plt.title("Mean annual air temperature", fontsize=10)  # Plot title
    cb.set_label("(\u00B0C)", fontsize=6)

    font_size = 6  # Adjust as appropriate.

    cb.ax.tick_params(labelsize=font_size)  # define label font size

    plt.savefig(
        "NRB_spatial_avg_ann_temp_single.png", format="png", dpi=300
    )  # save plot in a .png format at 300 DPI
