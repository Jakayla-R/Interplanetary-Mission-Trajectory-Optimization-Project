import numpy as np

def hohmann_transfer(r1, r2):
    """
    Calculates delta-v for a Hohmann transfer orbit between two circular orbits.
    
    Parameters:
    r1: Radius of the initial orbit (m)
    r2: Radius of the target orbit (m)
    
    Returns:
    delta_v1: Change in velocity for the first burn (m/s)
    delta_v2: Change in velocity for the second burn (m/s)
    """
    mu = 3.986e14  # Gravitational constant for Earth in m^3/s^2
    
    # Semi-major axis of the transfer orbit
    a = (r1 + r2) / 2
    
    # Velocity in the initial orbit
    v1 = np.sqrt(mu / r1)
    
    # Velocity in the transfer orbit at the initial position (perigee)
    v_transfer_perigee = np.sqrt(mu * (2 / r1 - 1 / a))
    
    # Velocity in the transfer orbit at the final position (apogee)
    v_transfer_apogee = np.sqrt(mu * (2 / r2 - 1 / a))
    
    # Velocity in the target orbit
    v2 = np.sqrt(mu / r2)
    
    # Delta-v required for each burn
    delta_v1 = v_transfer_perigee - v1
    delta_v2 = v2 - v_transfer_apogee
    
    return delta_v1, delta_v2
