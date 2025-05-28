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
> In particular, their names should end my `100A.mat`, `101A.mat`, `100B.mat`, `101B.mat` depending on the 
> orientation and whether they are amplitude or phase data


