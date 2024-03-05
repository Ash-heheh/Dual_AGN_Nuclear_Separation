from math import sin, cos, acos, radians

# Helper function for RA and Dec conversion
def ra_to_decimal(hours, minutes, seconds):
    return (hours + minutes / 60 + seconds / 3600) * 15

def dec_to_decimal(degrees, arcminutes, arcseconds):
    return degrees + arcminutes / 60 + arcseconds / 3600

# Eastern AGN coordinates in decimal degrees
ra_eastern_deg = ra_to_decimal(12, 59, 39.8102)
dec_eastern_deg = dec_to_decimal(27, 57, 16.417)

# Western AGN coordinates in decimal degrees
ra_western_deg = ra_to_decimal(12, 59, 35.6909)
dec_western_deg = dec_to_decimal(27, 57, 32.527)

# Convert to radians
ra_eastern_rad = radians(ra_eastern_deg)
dec_eastern_rad = radians(dec_eastern_deg)
ra_western_rad = radians(ra_western_deg)
dec_western_rad = radians(dec_western_deg)

# Calculate the difference in right ascension in radians
delta_alpha_rad = abs(ra_eastern_rad - ra_western_rad)

# Calculate angular distance using the spherical law of cosines
cos_d = sin(dec_eastern_rad) * sin(dec_western_rad) + cos(dec_eastern_rad) * cos(dec_western_rad) * cos(delta_alpha_rad)
d_rad = acos(cos_d)

# Convert angular distance from radians to arcseconds for interpretation
d_arcsec = d_rad * (206265)  # 1 radian = 206265 arcseconds

d_arcsec
