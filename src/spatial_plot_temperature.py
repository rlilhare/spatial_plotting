# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 09:13:37 2020

@author: rlilhare
"""
from mpl_toolkits.basemap import Basemap
from netCDF4 import Dataset as NetCDFFile 
import matplotlib.pyplot as plt
import numpy as np
import os
plt.style.use('seaborn-white')

base_path = os.getcwd()
air_temp_path = os.path.join(base_path, './data/ERA_Land_mn_ann_air_temp_NRB_1981_2019.nc')
ws_bound_path=os.path.join(base_path, './data/sub-basin_shp_for_plots/')


nc = NetCDFFile(air_temp_path) # Input your file in a netcdf format
nc.variables


lat = nc.variables['lat'][:]
lon = nc.variables['lon'][:]
time = nc.variables['time'][:]
temp = nc.variables['temp'][:] # We are plotting this variable in the current plot (avg ann air temperature)



map = Basemap(projection='merc',llcrnrlon=-128.,llcrnrlat=52.6,urcrnrlon=-122.3,urcrnrlat=56.4,resolution='i') # projection, lat/lon extents and resolution of polygons to draw
# resolutions: c - crude, l - low, i - intermediate, h - high, f - full


#map.drawcoastlines()
#map.drawstates()
#map.drawcountries()
map.drawlsmask(land_color='w', ocean_color='w') # can use HTML names or codes for colors
#map.drawlsmask(land_color='Linen', ocean_color='#CCFFFF') # can use HTML names or codes for colors
map.drawcounties() # you can even add counties (and other shapefiles!)
map.readshapefile(os.path.join(ws_bound_path, "Stuart"), "Stuart", drawbounds = True)
map.readshapefile(os.path.join(ws_bound_path,"Middle_Nech"), "Middle_Nech", drawbounds = True)
map.readshapefile(os.path.join(ws_bound_path,"Chilako"), "Chilako", drawbounds = True)
map.readshapefile(os.path.join(ws_bound_path,"Lower_Nech"), "Lower_Nech", drawbounds = True)
map.readshapefile(os.path.join(ws_bound_path,"Regulated_for_sp_plot"), "Regulated_for_sp_plot", drawbounds = True)
map.readshapefile(os.path.join(ws_bound_path,"Nautley"), "Nautley", drawbounds = True)

parallels = np.arange(50,57,2.) # make latitude lines ever 5 degrees from 30N-50N
meridians = np.arange(-128,-118,2.) # make longitude lines every 5 degrees from 95W to 70W
map.drawparallels(parallels,labels=[1,0,0,0],dashes=[4,500], color='k',fontsize=6)
map.drawmeridians(meridians,labels=[0,0,0,1], dashes=[4,500], color='k',fontsize=6) #meridians,labels=[0,0,0,1],fontsize=6)



lons,lats= np.meshgrid(lon,lat) # for this dataset, longitude is 0 through 360, so you need to subtract 180 to properly display on map
x,y = map(lons,lats)


temp = map.contourf(x,y,temp[0,:,:],range(-2, 6,1), cmap='Reds')
cb = map.colorbar(temp,"bottom", size="4%", pad="8%") #pad takes label down
#cb = plt.colorbar(temp) #pad takes label down
#plt.clim(450, 2400)

plt.title('Mean annual air temperature',fontsize=10) #Plot title
cb.set_label('(\u00B0C)',fontsize=6)

clevs1 =np.arange(-2,6,1) #clevs1 =np.arange(479,2396,200)
font_size = 6 # Adjust as appropriate.

cb.ax.tick_params(labelsize=font_size)
#cb.ax.set_xticklabels(clevs1[::1],rotation=45)

#cb.set_ticks(np.linspace(0, 2500))
#cb.set_ticklabels(range(2500))
#cb.colorbar(extend='both')
#plt.clim(-1, 1);



plt.savefig('NRB_spatial_avg_ann_temp_single.png', format='png', dpi=300) #save plot in a .png format at 300 DPI





