#######################################################################
# Program Filename: Homework 3
# Author:  Ceiba Cummings
# Date: 05/11/22
# Description: This program calculates the settling sediment velocity time
#              water retnetion times, and energy savings for the use of a dry pond
#              storage management system.
# Input: gravity, sediment density, water density, dynamic viscosity of the fluid,
#        surface area of the pond, area of the drain outlet, water height, orifice discharge,
#        all provided in the assignment.
# Output: settling velocity, time to settle in a 2 m pond, orifice size, and the energy savings.
#######################################################################



import pandas as pd
import matplotlib as plt
import numpy as np
import library as lib

file_path = "C:/Users/ceiba/Downloads/46248h2021.csv"
buoy_data = pd.read_csv(file_path)
print(buoy_data)


sig_wave_h = buoy_data.loc[:, "WVHT"]
peak_period = buoy_data.loc[:, "PERIOD"]
month = buoy_data.loc[:, "MON"]
day = buoy_data.loc[:, "DAY"]
period = buoy_data.loc[:, "PERIOD"]

#PART 2a
pinc = lib.calc_inc_power(sig_wave_h, peak_period)
print(pinc)


#PART 2b Find monthly data
wave_h_array = []
period_array = []
pinc_array = []
for x in range(12):
    wave_h_array.append(lib.find_monthly_data(sig_wave_h, month, x + 1))
    period_array.append(lib.find_monthly_data(period, month, x+1))
    pinc_array.append(lib.find_monthly_data(pinc, month, x+1))
print(wave_h_array)
print(period_array)
print(pinc_array)

#PART 2c
avg_h = []
max_h = []
avg_pwr = []
max_pwr = []
avg_prd = []
max_prd = []
for x in range(12):
    wave_h_array.append(lib.find_monthly_data(sig_wave_h, month, x + 1))
    period_array.append(lib.find_monthly_data(period, month, x + 1))
    pinc_array.append(lib.find_monthly_data(pinc, month, x + 1))

print(wave_h)
#
# month_int = [1,2,3,4,5,6,7,8,9,10,11,12]
# avg_max_hgt = lib.find_monthly_data(buoy_data)
# print(avg_max_hgt)
#PART 2c









