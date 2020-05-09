## ----global_options, include = FALSE-----------------------------------------------------------------------------------------------------------------------------------
try(source("../../../.Rprofile"))


## # define string

## st_full = """

## abc is a great efg, probably xyz. Yes, xyz is great, like efg.

## eft good, EFG capitalized, efg good again.

## A B C or abc or ABC. Interesting xyz.

## """

## 
## # define new and old

## ls_st_old = ['abc', 'efg', 'xyz']

## ls_st_new = ['123', '456', '789']

## 
## # zip and loop and replace

## for old, new in zip(ls_st_old, ls_st_new):

##   st_full = st_full.replace(old, new)

## 
## # print

## print(st_full)

