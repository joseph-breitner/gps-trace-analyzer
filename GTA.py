# -*- coding: utf-8 -*-
"""
~ PROJECT  1: GPS Trace Analyzer (GTA) ~
==============================================
This application reads information from
.csv and .nmea files to determine a vehicle's
minimum speed, maximum speed, average speed,
average heading, minimum heading, maximum 
heading, and total distance traveled. Then 
prints the results in the command prompt.
===============================================
Created by: Joseph Breitner (fo8040)
Date: 16 June 2018
"""

import sys
from gps_pkg import gps
import pandas as pd
from pandas import DataFrame

input_file = str(sys.argv[1])
df_a = pd.read_csv(input_file)



def averageSpeed(timeDiff, distanceTraveled):
    speed = distanceTraveled / timeDiff
    return speed





