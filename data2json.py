import numpy as np
import netCDF4 as nc
from json import JSONEncoder
import json
import math

## Definition of numpy array encoder class for serialization of ndnumpy array into json string ##
class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)
## ------------------------------------------------------------------------------------------- ##

## Extraction of wave data parameters from .nc file ##
path = "D:\Wave team research\wavm-inner_wave.nc"
data = nc.Dataset(path)
json_filename = "numpyData.json"

x = np.array(data['x'])
y = np.array(data['y'])
depth = np.array(data['depth'][0, :, :])
wave_ht = np.array(data['hsign'][0, :, :])
wave_dir = np.array(data['dir'][0, :, :])
## ------------------------------------------------ ##

## Customizable user settings for rasterizing wave data ##
fac = 1
## ---------------------------------------------------- ##

## Definition of functions ##
def avg(val, data_type):  
    # data_type - 0: x,y; 1: direction, 2: others
    if (data_type == 1):
        xsum = 0
        ysum = 0
        len = 0

        for v in val:
            # if v != -1.:
            xsum += math.sin(np.deg2rad(v))
            ysum += math.cos(np.deg2rad(v))
            len += 1

        if (len > 0):
            xsum /= len
            ysum /= len
            
        avg_deg = np.rad2deg(math.atan2(ysum, xsum))
        return avg_deg
    
    else:
        sum = 0
        len = 0
        for v in val:
            # if v != -1.:
            sum += v
            len += 1
        if (len > 0):
            sum /= len
        return sum

def zoom(arr, mult, data_type):
    # data_type - 0: x,y; 1: direction, 2: others
    arr_shape = np.shape(arr)
    arr_mod_shape = [math.ceil(s/mult) for s in arr_shape]

    arr_mod = np.zeros(arr_mod_shape)
    for i in range(arr_mod_shape[0]):
        for j in range(arr_mod_shape[1]):
            val_list = []    
            for x in range(mult):
                if (i*mult+x < arr_shape[0]):
                    for y in range(mult):
                        if (j*mult+y < arr_shape[1]):
                            val_list.append(arr[i*mult+x][j*mult+y])
            arr_mod[i][j] = avg(val_list, data_type)   

    return arr_mod
## ----------------------- ##

## Modification of data according to a multiplication factor ##
x_mod = zoom(x, fac, 0)
y_mod = zoom(y, fac, 0)
wave_ht_mod = zoom(wave_ht, fac, 2)
wave_dir_mod = zoom(wave_dir, fac, 1)
## --------------------------------------------------------- ##

## Publishing of wave data into JSON file ##
wave_data = {"waveHeight": wave_ht_mod, "waveDirection": wave_dir_mod}
print(f"Serializing wave data into JSON string and writing into {json_filename}")
with open(json_filename, "w") as write_file:
    json.dump(wave_data, write_file, cls=NumpyArrayEncoder)
print(f"Done writing serialized wave data into {json_filename}")
## -------------------------------------- ##

## Extraction of wave data from JSON file as test ##
print("Started Reading JSON file")
with open(json_filename, "r") as read_file:
    print("Converting JSON encoded data into Numpy array")
    decodedArray = json.load(read_file)

    finalNumpyArrayOne = np.asarray(decodedArray["waveHeight"])
    print("Wave height")
    print(finalNumpyArrayOne)
    finalNumpyArrayTwo = np.asarray(decodedArray["waveDirection"])
    print("Wave direction")
    print(finalNumpyArrayTwo)
## ----------------------------------------------- ##