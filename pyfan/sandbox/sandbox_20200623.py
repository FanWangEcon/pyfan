import cdsapi
import urllib.request

# download folder
spt_root = "C:/Users/fan/Downloads/_data/"
spn_dl_test_grib = spt_root + "derived_utci_2010_2.zip"
# request
c = cdsapi.Client()

res = c.retrieve(
    'derived-utci-historical',
    {
        'format': 'zip',
        'variable': 'Universal thermal climate index',
        'product_type': 'Consolidated dataset',
        'year': '2010',
        'month': [
            '07',
        ],
        'day': [
            '01', '02'
        ],
        'area': [53.31, 73, 4.15, 135],
        'grid': [0.25, 0.25],
    },
    spn_dl_test_grib)

# show results
print('print results')
print(res)
print(type(res))
