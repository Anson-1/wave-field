# %%
from datetime import datetime

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage as ndimage
import xarray as xr 
import pandas as pd
from mpl_toolkits.basemap import Basemap
from scipy import interpolate

import json
import sys

json_obj = open(sys.argv[0])
# var1 = json.load(json_obj)

data_all = xr.open_dataset("wavm-inner_wave.nc")

xmin = 114.1919; xmax = 114.283 # 5, 233
ymin = 22.1794; ymax = 22.2478

# data = pd.DataFrame(data)
# data['hsign'].isel(time=3)
# lon = data.x.values; lat = data.y.values 
var = data_all['hsign'].isel(time=3).values
var2 = data_all['pdir'].isel(time=3).values

lng = data_all['x'][0, :].values
lat = data_all['y'][:, 0].values
f = interpolate.interp2d(lng, lat, var, kind='cubic')
xnew = np.arange(xmin, xmax, 0.001)
ynew = np.arange(ymin, ymax, 0.001)
znew = f(xnew, ynew)

f2 = interpolate.interp2d(lng, lat, var2, kind='cubic')
xnew2 = np.arange(xmin, xmax, 0.005)
ynew2 = np.arange(ymin, ymax, 0.005)
znew2 = f(xnew2, ynew2)

# create map using BASEMAP
m = Basemap(llcrnrlon = xmin,
            llcrnrlat = ymin,
            urcrnrlon = xmax,
            urcrnrlat = ymax,
            # lat_0=(ymax - ymin)/2,
            # lon_0=(xmax - xmin)/2,
            # projection='merc',
            resolution = 'h',
            # area_thresh=10000.,
            )
m.drawcoastlines()
m.fillcontinents(color = 'white',lake_color='white')

my_cmap = plt.get_cmap('jet')
my_cmap.set_under('white')
cs = m.pcolormesh(xnew, ynew, znew,cmap = my_cmap)
widths = np.linspace(0, 1000, lng.size)
cs2 = m.quiver(xnew2, ynew2, np.cos(znew2),  np.sin(znew2), scale = 7)#, latlon=True, lscale=10, scale_units='inches')
m.colorbar(cs)# , extend = 'min')
plt.show()

# df = pd.DataFrame(var)
# df.to_csv('var.csv')



 # %%
##data.isel(nmax = slice(30, 50), mmax = slice(40,50))