#!/usr/bin/env python3
""" Testing out the different 'version' keywords """

from datetime import datetime
from pyglow import Point

dn = datetime(2010, 3, 23, 15, 30)
lat = 40.
lon = -80.
alt = 250.

pt = Point(dn, lat, lon, alt)

# pt._run_hwm93()
# pt._run_hwm07()
# pt._run_hwm14()

print('testing 1993')
pt.run_hwm(version=1993)
print('testing 2007')
pt.run_hwm(version=2007)
print('testing 2014')
pt.run_hwm(version=2014)
pt.run_hwm()
print('testing msis')
pt.run_msis()
pt.run_msis(version=2000)

print('testing igrf')
pt.run_igrf()
pt.run_igrf(version=11)
pt.run_igrf(version=12)

print('testing iri')
pt.run_iri()
print('testing iri 2016')
pt.run_iri(version=2016)
print('testing iri 2012')
pt.run_iri(version=2012)

print('testing 2020')
try:
    pt.run_iri(version=2020)
    print('all tests passed')
except ValueError as e:
    print("Caught an exception: `{}`".format(e))
