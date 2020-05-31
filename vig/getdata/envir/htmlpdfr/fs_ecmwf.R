## ----global_options, include = FALSE------------------------------------------------------------------------------------------------
try(source("../../../.Rprofile"))


## # Inside anaconda prompt

## where python

## where anaconda

## # C:/ProgramData/Anaconda3/Scripts/anaconda.exe

## # C:/ProgramData/Anaconda3/python.exe


## conda config --add channels conda-forge

## conda install -c conda-forge eccodes -y


## url: https://cds.climate.copernicus.eu/api/v2

## key: 4XXXX:4XXXfXXX-XXXf-4XXX-9XXX-7XXXebXXfdXX


## import cdsapi

## import urllib.request

## # download folder

## spt_root = "C:/Users/fan/downloads/_data/"

## spn_dl_test_grib = spt_root + "test_china_temp.grib"

## # request

## c = cdsapi.Client()

## res = c.retrieve("reanalysis-era5-pressure-levels",

##   {

##     'product_type': 'reanalysis',

##     'variable': 'temperature',

##     'pressure_level': '1000',

##     'year': '2008',

##     'month': '01',

##     'day': '01',

##     'time': '12:00',

##     'format': 'netcdf',

##     'area'          : [53.31, 73, 4.15, 135],

##     'grid'          : [1.0, 1.0],

##     "format": "grib"

##   },

##   spn_dl_test_grib

## )

## # show results

## print('print results')

## print(res)

## print(type(res))


## cd "C:/Users/fan/downloads/_data/"

## grib_ls test_china_temp.grib

## grib_get_data test_china_temp.grib > test_china_temp_raw.csv


## # Set up

## conda deactivate

## conda list env

## conda env remove -n wk_ecmwf

## conda create -n wk_ecmwf -y

## conda activate wk_ecmwf

## 
## # Add conda-forge to channel in env

## conda config --env --add channels conda-forge

## conda config --get channels

## conda config --get channels --env

## 
## # Install

## conda install cdsapi -y

## conda install -c conda-forge eccodes -y


## stf_cds_cdsapirc = """\

## url: https://cds.climate.copernicus.eu/api/v2

## key: 46756:4000fe9a-498f-4ce8-9caf-7796eb64fd9d\

## """

## print(stf_cds_cdsapirc)


## # Relative file name

## spt_file_cds = "C:/Users/fan/"

## snm_file_cds = ".cdsapirc"

## spn_file_cds = spt_file_cds + snm_file_cds

## # Open new file

## fl_cdsapirc_contents = open(spn_file_cds, 'w')

## # Write to File

## fl_cdsapirc_contents.write(stf_cds_cdsapirc)

## # Close

## fl_cdsapirc_contents.close()


## # Open the config file to check

## code "C:/Users/fan/.cdsapirc"


## # import module in conda env wk_ecmwf

## import cdsapi

## import urllib.request

## 
## # download folder

## spt_root = "C:/Users/fan/pyfan/vig/getdata/envir/"

## spn_dl_test_grib = spt_root + "_data/test/test_china_temp.grib"

## 
## # request

## c = cdsapi.Client()

## res = c.retrieve("reanalysis-era5-pressure-levels",

##   {

##     'product_type': 'reanalysis',

##     'variable': 'temperature',

##     'pressure_level': '1000',

##     'year': '2008',

##     'month': '01',

##     'day': '01',

##     'time': '12:00',

##     'format': 'netcdf',

##     'area'          : [53.31, 73, 4.15, 135],

##     'grid'          : [1.0, 1.0],

##     "format": "grib"

##   },

##   spn_dl_test_grib

## )

## # show results

## print('print results')

## print(res)

## print(type(res))

## 
## # download

## # response = urllib.request.urlopen('http://www.example.com/')

## # html = response.read()


## cd "C:/Users/fan/pyfan/vig/getdata/envir/_data/test/"

## grib_ls test_china_temp.grib

## grib_get_data test_china_temp.grib > test_china_temp_raw.csv


## spt_root = "C:/Users/fan/pyfan/vig/getdata/envir/_data/test/"

## spn_csv_raw = spt_root + "test_china_temp_raw.csv"

## spn_csv_edi = spt_root + "test_china_temp.csv"

## 
## with open(spn_csv_raw, 'r') as f_in, open(spn_csv_edi, 'w') as f_out:

##     f_out.write(next(f_in))

##     [f_out.write(','.join(line.split()) + '\n') for line in f_in]


## -----------------------------------------------------------------------------------------------------------------------------------
# Path and Read
spt_root = "C:/Users/fan/pyfan/vig/getdata/envir/"
spn_dl_test_csv = paste0(spt_root, "_data/test/test_china_temp.csv")
china_weather_data <- read.csv(spn_dl_test_csv)

# Top 50 rows
kable(head(china_weather_data, 50), 
      caption="Chinese Long and Lat, Temperature Pressure, 2008 Jan 1st at 12 noon?") %>%
  kable_styling_fc()

