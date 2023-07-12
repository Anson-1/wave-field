import matlab.engine
import numpy as np
import netCDF4 as nc
# from json import JSONEncoder
# import json
import math
import time

# class NumpyArrayEncoder(JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, np.ndarray):
#             return obj.tolist()
#         return JSONEncoder.default(self, obj)

path = "D:\Wave team research\wavm-inner_wave.nc"
data = nc.Dataset(path)
param_type = 'hsign'

x = np.array(data['x'])
y = np.array(data['y'])
depth = np.array(data['depth'][0, :, :])
param = np.array(data[param_type][0, :, :])
fac = 8

def avg(val, data_type):  
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
        # avg_deg = np.rad2deg(math.atan2(ysum, xsum))
        # return avg_deg
        return [xsum, ysum]
    
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
    # print(arr_shape)
    arr_mod_shape = [math.ceil(s/mult) for s in arr_shape]

    arr_mod1 = []
    arr_mod2 = []

    if (data_type == 1):
        arr_mod1 = np.zeros(arr_mod_shape)
        arr_mod2 = np.zeros(arr_mod_shape)
    else:
        arr_mod1 = np.zeros(arr_mod_shape)

    if (data_type > 0):
        for i in range(arr_mod_shape[0]):
            for j in range(arr_mod_shape[1]):
                val_list = []    
                for x in range(mult):
                    if (i*mult+x < arr_shape[0]):
                        for y in range(mult):
                            if (j*mult+y < arr_shape[1]):
                                # Implement screening function here
                                if (depth[i*mult+x][j*mult+y] > 0.):
                                    val_list.append(arr[i*mult+x][j*mult+y])
                if (data_type == 2):
                    arr_mod1[i][j] = avg(val_list, data_type)   
                elif (data_type == 1):
                    a = avg(val_list, data_type)
                    arr_mod1[i][j] = a[0]
                    arr_mod2[i][j] = a[1] 
    else:
        for i in range(arr_mod_shape[0]):
            for j in range(arr_mod_shape[1]):
                val_list = []    
                for x in range(mult):
                    if (i*mult+x < arr_shape[0]):
                        for y in range(mult):
                            if (j*mult+y < arr_shape[1]):
                                val_list.append(arr[i*mult+x][j*mult+y])
                arr_mod1[i][j] = avg(val_list, data_type)   

    if (data_type == 1):
        return (arr_mod1, arr_mod2)
    else:
        return arr_mod1

eng = matlab.engine.start_matlab()

if (param_type == "dir"):
    p_type = 1
else:
    p_type = 2
    
x_mod = zoom(x, fac, 0)
y_mod = zoom(y, fac, 0)
param_mod = zoom(param, fac, p_type)

disp = 0
if (p_type == 1):
    disp = eng.quiver(x_mod, y_mod, param_mod[0], param_mod[1])
elif (p_type == 2):
    disp = eng.pcolor(x_mod, y_mod, param_mod)

t = time.time()
while (time.time()-t) < 20:
    a = 1

eng.quit()