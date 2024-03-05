from astropy.cosmology import FlatLambdaCDM
import astropy.units as u
from math import radians

# Cosmology parameters (Planck 2018 results)
cosmo = FlatLambdaCDM(H0=67.4, Om0=0.315)

# Function to convert angular distance in arcseconds to physical distance in kpc
def arcsec_to_kpc(arcsec_distance, z, z_error=0.0):
    # Convert arcsec to radians
    angular_distance_rad = radians(arcsec_distance / 3600)
    
    # Calculate angular diameter distance for given z
    D_A = cosmo.angular_diameter_distance(z)
    
    # Calculate physical distance in kpc
    physical_distance_kpc = (D_A * angular_distance_rad).to(u.kpc, u.dimensionless_angles())
    
    # Calculate error margins based on z_error
    if z_error > 0:
        D_A_min = cosmo.angular_diameter_distance(z - z_error)
        D_A_max = cosmo.angular_diameter_distance(z + z_error)
        physical_distance_kpc_min = (D_A_min * angular_distance_rad).to(u.kpc, u.dimensionless_angles())
        physical_distance_kpc_max = (D_A_max * angular_distance_rad).to(u.kpc, u.dimensionless_angles())
        error_margin_kpc = max(physical_distance_kpc_max - physical_distance_kpc,
                               physical_distance_kpc - physical_distance_kpc_min)
        return physical_distance_kpc, error_margin_kpc
    else:
        return physical_distance_kpc, 0*u.kpc

# Example usage
arcsec_distance = 10  # angular separation in arcseconds
z = 0.0297  # redshift
z_error = 0.0001  # error in redshift

physical_distance_kpc, error_margin_kpc = arcsec_to_kpc(arcsec_distance, z, z_error)

print(f"Physical distance: {physical_distance_kpc}")
print(f"Error margin: ±{error_margin_kpc}")
