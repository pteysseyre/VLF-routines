# VLF-routines
This repository contains short functions that can be used to do basic operations on VLF data

## Reading files

To read Narrowband, the `read_Narrowband` function can be called. To do so, you need:

1. The date, in the correct format (e.g. '2023_11_05')
2. The call-sign of the function (e.g. 'GVT')
3. The path to the files. It is assumed that the files are organised in a file folder 
    and in subfolders named `year/month/date/`. If this is not the case, it can be changed 
    in the fonction (see the relevant line, indicated at the start of the function)
4. (Optional) The calibration factors for the station and each orientation

> [!NOTE]
> It is assumed that the files being read have the same naming convention as the ones from the AWESOME antennas. 
> In particular, their names should end by `100A.mat`, `101A.mat`, `100B.mat`, `101B.mat` depending on the 
> orientation and whether they are amplitude or phase data

Reading Broadbands works much in the same way, by calling the `read_Broadband` function. In addition to
the previous inputs, we need to specify the start hour and minute (and in option, second). The function only returns the 
amplitude in the E/W and N/S directions. The path inputted for this function is the entire path (not assuming specific
subfolders as the `read_Narrowband` function.)

### Example 

Calling the two functions should be done as below:

```ruby
la_date = '2025_05_25'
la_station = 'NSY'

# Reading narrowband files
amp_NS, amp_EW, phase_NS, phase_EW, the_time = read_Narrowband(la_date,
    la_station, '/path_to_mat_files/', Cal_NS = 4, Cal_EW = 5)

# Reading broadband files
broadband_NS, broadband_EW = read_Broadband(la_date, '09', '12', '/complete_path_to_broadbandfiles/')
```




