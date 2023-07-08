# sensor.py

import random, time
n = 0

import xarray as xr 
import json
import sys

data = xr.open_dataset("wavm-inner_wave.nc")
var = data['hsign'].isel(time=3).values
long = data['x'][0, :].values
lat = data['y'][:, 0].values

print(data['hsign'].isel(time=3), flush=True, end='')


# while n<5:
#     time.sleep(random.random() * 5)  # wait 0 to 5 seconds
#     temperature = (random.random() * 20) - 5  # -5 to 15
#     print(temperature, flush=True, end='')
#     n += 1