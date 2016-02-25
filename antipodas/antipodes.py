#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Lucho
#
# Created:     25/02/2016
# Copyright:   (c) Lucho 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
# Original latitude and longitude values in Decimal Degrees
Latitude =  40.416691
Longitude = -3.700345

# Convert latitude to opposite hemisphere (e.g. −x* −1 = x)
AntiLatitide = Latitude *-1

print "Antipodal Latitude: " + str(AntiLatitide)

# Convert Longitude to opposite hemisphere (e.g. (180 - x)*-1 = y)
# Note this binds the maximum values to be -180 and 180 degrees
if Longitude > 0:
    AntiLongitude = (180 - Longitude)*-1
elif Longitude < 0:
    AntiLongitude = (-180 - Longitude)*-1

print "Antipodal Longitude: " + str(AntiLongitude)