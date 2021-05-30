import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-white')

def plot_data(lat, lon, temp, map):
    parallels = np.arange(50,57,2.) # make latitude lines ever 5 degrees from 30N-50N
    meridians = np.arange(-128,-118,2.) # make longitude lines every 5 degrees from 95W to 70W
    map.drawparallels(parallels,labels=[1,0,0,0],dashes=[4,500], color='k',fontsize=6)
    map.drawmeridians(meridians,labels=[0,0,0,1], dashes=[4,500], color='k',fontsize=6) #meridians,labels=[0,0,0,1],fontsize=6)

    lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
    x,y = map(lons,lats)
    temp = map.contourf(x,y,temp[0,:,:],range(-2, 6,1), cmap='Reds')
    cb = map.colorbar(temp,"bottom", size="4%", pad="8%") #pad takes label down

    plt.title('Mean annual air temperature',fontsize=10) #Plot title
    cb.set_label('(\u00B0C)',fontsize=6)

    clevs1 =np.arange(-2,6,1) #clevs1 =np.arange(479,2396,200)
    font_size = 6 # Adjust as appropriate.

    cb.ax.tick_params(labelsize=font_size) #define label font size

    plt.savefig('NRB_spatial_avg_ann_temp_single.png', format='png', dpi=300) #save plot in a .png format at 300 DPI