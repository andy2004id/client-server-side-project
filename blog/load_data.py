csv_filepathname = "/Users/sungkaho/Desktop/zipcode.csv"

your_djangoproject_home = "/Users/sungkaho/djangogirls"


import sys, os


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from blog.models import ZipCode
import csv

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    if row[0] != 'ZIPCODE':
        zipcode = ZipCode()
        zipcode.zipcode = row[0]
        zipcode.city = row[1]
        zipcode.statecode = row[2]
        zipcode.statename = row[3]
        zipcode.save()