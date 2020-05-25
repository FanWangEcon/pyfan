## ----global_options, include = FALSE------------------------------------------------------------------------------------------------
try(source("../../../.Rprofile"))


## import datetime

## import pprint

## ls_dc_exa =  [

##     {"file": "mat_matlab",

##      "title": "One Variable Graphs and Tables",

##      "description": "Frequency table, bar chart and histogram",

##      "val": 1,

##      "date": datetime.date(2020, 5, 2)},

##     {"file": "mat_two",

##      "title": "Second file",

##      "description": "Second file.",

##      "val": [1, 2, 3],

##      "date": datetime.date(2020, 5, 2)},

##     {"file": "mat_algebra_rules",

##      "title": "Opening a Dataset",

##      "description": "Opening a Dataset.",

##      "val": 1.1,

##      "date": datetime.date(2018, 12, 1)}

## ]

## pprint.pprint(ls_dc_exa, width=1)


## # string to search through

## ls_str_file_ids = ['mat_matlab', 'mat_algebra_rules']

## # select subset

## ls_dc_selected = [dc_exa

##                   for dc_exa in ls_dc_exa

##                   if dc_exa['file'] in ls_str_file_ids]

## # print

## pprint.pprint(ls_dc_selected, width=1)


## # string to search through

## ls_str_file_ids = ['mat_matlab', 'mat_algebra_rules']

## # select subset

## ls_dc_selected = [dc_exa

##                   for dc_exa in ls_dc_exa

##                   if ((dc_exa['file'] in ls_str_file_ids)

##                       and

##                       (dc_exa['val']== 1))]

## # print

## pprint.pprint(ls_dc_selected, width=1)

