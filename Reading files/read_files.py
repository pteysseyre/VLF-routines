#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 11:47:33 2024

@author: pteysseyre
"""

from pymatreader import read_mat # To read the .mat files
import os.path # Useful to determine if a file exist or not (to write headers in a new file)
import glob
import numpy as np

#======================== Read mat files ======================================

def read_Narrowband(la_date, la_station, path, Cal_NS = 1, Cal_EW = 1): 
    """
    Reads the data for the station and the day asked and stores them in the output arrays
    NOTE: This code reads the latest created file (in case several files are present)

    Inputs
    ------------------
    - la_date: Date, in the format 'yyyy_mm_dd'.
    - la_station: Station call-sign (e.g. 'NSY')
    - path: Path to the files (without their names, e.g. 'Users/example/Documents/FileFolder/')
        NOTE: It is assumed that in FileFolder, files are organised by year, month and day:
        e.g. FileFolder/2023/11/2023_11_05/
        If this is not the case, please delete, change or comment the line below the comment "------- To change if needed -------"
    - Cal_NS/Cal_EW: Calibration factor to apply on the NS and EW orientation (default: 1)

    Outputs
    -----------------
    - amp_NS, amp_EW: Amplitude time series (in pT)
    - phase_NS, phase_EW = Phase time series (in °)
    - the_time: time-array

    History
    --------------------
    Written by C. Briand on 16//10/2022
    Modified and converted to Python on 18/03/2024"""
    
    the_year, the_month, the_day = la_date.split('_')
    start_time = 0
    
    # -------------------- To change if needed -------------------------
    path = path + str(the_year) + '/' + str(the_month) + '/' + la_date + '/'
    # ------------------------------------------------------------------

    # amp_NS
    list_of_files = glob.glob(path+'*'+la_station+'_100A.mat')
    try :
        latest_file = max(list_of_files, key=os.path.getctime)
    except ValueError: # If the path is wrong
        print('Check the path to .mat files (read_Narrowband)')
        amp_NS = np.nan
        amp_EW = np.nan
        phase_EW = np.nan
        phase_NS = np.nan
        the_time = np.nan
        return (amp_NS, amp_EW, phase_NS, phase_EW, the_time)

    try :
        data = read_mat(latest_file)
        amp_NS = data['data']*Cal_NS
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - amp_NS')
        amp_NS = np.nan

    
    # phase_EW
    list_of_files = glob.glob(path+'*'+la_station+'_101B.mat')
    latest_file = max(list_of_files, key=os.path.getctime)

    try :
        data = read_mat(latest_file)
        phase_EW = data['data']
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - phase_EW')
        phase_EW = np.nan
    
    
    # amp_EW
    list_of_files = glob.glob(path+'*'+la_station+'_101A.mat')
    latest_file = max(list_of_files, key=os.path.getctime)
    try :
        data = read_mat(latest_file)
        amp_EW = data['data']*Cal_EW
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - amp_EW')
        amp_EW = np.nan

    # phase_NS
    list_of_files = glob.glob(path+'*'+la_station+'_100B.mat')
    latest_file = max(list_of_files, key=os.path.getctime)
    try :
        data = read_mat(latest_file)
        phase_NS = data['data']
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - phase_NS')
        phase_NS = np.nan
    
    # Time array
    Fs = data['Fs']
    tstep = 1/Fs/3600
    data_length = np.max([np.size(phase_NS), np.size(phase_EW), np.size(amp_NS), np.size(amp_EW)])
    the_time = np.linspace(start_time, tstep*data_length, data_length)
    
    return (amp_NS, amp_EW, phase_NS, phase_EW, the_time)

def read_Broadband(la_date, hour_file, minute_file, path, Cal_NS = 1, Cal_EW = 1, second_file = '00',): 
    """
    Reads the data for the station and the day asked and stores them in the output arrays
    NOTE: This code reads the latest created file (in case several files are present)

    Inputs
    ------------------
    - la_date: Date, in the format 'yyyy_mm_dd'.
    - hour/minute: Hour and minute (in UT) of the file we want to read
        They should be strings (e.g. hour = '05', and minute  = '30')
    - la_station: Station call-sign (e.g. 'NSY')
    - path: Path to the files (without their names, e.g. 'Users/example/Documents/FileFolder/')
    - Cal_NS/Cal_EW: Calibration factor to apply on the NS and EW orientation (default: 1)

    Outputs
    -----------------
    - amp_NS, amp_EW = Amplitude in the NS and EW direction
    - the_time: time-array

    History
    --------------------
    Written by P. Teysseyre on 28/05/2025 """
    
    the_year, the_month, the_day = la_date.split('_')
    start_time = 0
    
    # amp_NS
    list_of_files = glob.glob(path+'*'+ the_year[2:] + the_month + the_day + hour_file + minute_file + second_file + '_100.mat')
    try :
        latest_file = max(list_of_files, key=os.path.getctime)
    except ValueError: # If the path is wrong
        print('Check the path to .mat files (read_Broadband)')
        amp_NS = np.nan
        amp_EW = np.nan
        the_time = np.nan
        return (amp_NS, amp_EW, the_time)

    try :
        data = read_mat(latest_file)
        amp_NS = data['data']*Cal_NS
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - amp_NS')
        amp_NS = np.nan

    
    # amp_EW
    list_of_files = glob.glob(path+'*'+ the_year[2:] + the_month + the_day + hour_file + minute_file + second_file + '_101.mat')
    latest_file = max(list_of_files, key=os.path.getctime)

    try :
        data = read_mat(latest_file)
        amp_EW = data['data']*Cal_EW
        start_time = data['start_hour'] + data['start_minute']/60 + data['start_second']/3600
    except (TypeError, ValueError):
        print('TypeError - phase_EW')
        amp_EW = np.nan

    # Time array
    Fs = data['Fs']
    tstep = 1/Fs/3600
    data_length = np.max([np.size(amp_NS), np.size(amp_EW)])
    the_time = np.linspace(start_time, tstep*data_length, data_length)
    
    return (amp_NS, amp_EW, the_time)


