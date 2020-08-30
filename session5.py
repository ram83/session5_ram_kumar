# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 09:22:52 2020

@author: Dell
"""
import pandas as pd
import timeit
import time
import numpy as np
import math
from math import tan, pi

def squared_power_list(*args,**kwargs):
    if args[0] == -1.0*abs(args[0]):
        raise ValueError("Only positive numbers accepted")
    else:
        for j in range(kwargs['start'],kwargs['end']):
            squared=math.pow(j,args[0])
        return squared


def polygon_area(*args,**kwargs):    
    if (args[0]==0 and kwargs['sides']<3) or (args[0]==0 and kwargs['sides']>6):
        pass
    else:       
        p_area = kwargs['sides'] * (args[0] ** 2) / (4 * tan(pi / kwargs['sides']))   
        print(p_area)
        return p_area


def temp_converter(*args,**kwargs):    
    if kwargs['temp_given_in']=='f':
        celsius = (args[0] -32) *(5/9) 
        print(celsius)
        return celsius
    else:
        fahrenheit = (args[0] * (9/5)) + 32 
        print(fahrenheit)
        return fahrenheit


def speed_converter(*args,**kwargs):    
    try:        
        if kwargs['dist']=='km' and kwargs['time']== 'min':           
            speed_converted=args[0]*0.0166666667
        elif kwargs['dist']=='km' and kwargs['time']=='s':
            speed_converted=args[0]*0.0002777778
        elif kwargs['dist']=='km' and kwargs['time']=='ms':
            speed_converted=args[0]*3.6e+6
        elif kwargs['dist']=='km' and kwargs['time']=='day':
            speed_converted=args[0]*24
        elif kwargs['dist']=='km' and kwargs['time']=='hr':
            speed_converted=args[0]*1
        elif kwargs['dist']=='m' and kwargs['time']=='s':
            speed_converted=args[0]*0.2777778
        elif kwargs['dist']=='m' and kwargs['time']=='min':
            speed_converted=args[0]*16.667
        elif kwargs['dist']=='m' and kwargs['time']=='ms':
            speed_converted=args[0]*0.000277778
        elif kwargs['dist']=='m' and kwargs['time']=='hr':
            speed_converted=args[0]*1000
        elif kwargs['dist']=='m' and kwargs['time']=='day':
            speed_converted=args[0]*24000
        elif kwargs['dist']=='ft' and kwargs['time']=='s':
            speed_converted=args[0]*0.911344
        elif kwargs['dist']=='ft' and kwargs['time']=='ms':
            speed_converted=args[0]*0.000911344
        elif kwargs['dist']=='ft' and kwargs['time']=='min':
            speed_converted=args[0]*54.6807
        elif kwargs['dist']=='ft' and kwargs['time']=='hr':
            speed_converted=args[0]*3280.84
        elif kwargs['dist']=='ft' and kwargs['time']=='day':
            speed_converted=args[0]*78740.2
        elif kwargs['dist']=='yrd' and kwargs['time']=='s':
            speed_converted=args[0]*0.303781
        elif kwargs['dist']=='yrd' and kwargs['time']=='ms':
            speed_converted=args[0]*0.000303781
        elif kwargs['dist']=='yrd' and kwargs['time']=='min':
            speed_converted=args[0]*18.2269
        elif kwargs['dist']=='yrd' and kwargs['time']=='hr':
            speed_converted=args[0]*1093.61
        elif kwargs['dist']=='yrd' and kwargs['time']=='day':
            speed_converted=args[0]*26246.7            
    except:
        raise ValueError("check conversion")
    return speed_converted

def time_it(fn, *args, repetitons= 1, **kwargs):  
    if repetitons==-1*abs(repetitons):
        raise ValueError("Repetitions cannot be negative")
    else:
        start=time.time()   
        for i in range(repetitons):
            fn(*args,**kwargs)      
        end=time.time()    
        return {"Average time taken for:":(end-start)/repetitons}


time_it(print, 1, 2, 3, sep='-', end= ' ***\n', repetitons=5)
time_it(squared_power_list, 2, start=0, end=5, repetitons=50) 
time_it(polygon_area, 15, sides = 3, repetitons=10)
time_it(temp_converter, 100, temp_given_in = 'f', repetitons=100)
time_it(speed_converter, 100, dist='km', time='min', repetitons=2000)