from math import *
import Graphs_Design as gp
from Variables import StrengthYield, StrengthUltimate, D1 as D

M = 218.55
d = 0.5
Fz = 1529.05
Fy = 509.68

# Set a factor of safety
MS = 2

# Calculate the force in the lug due to the moment
def get_F1():
    F1 = M/d
    return F1

# Calculate the oblique force P in the yz-plane of the lug
def get_P():
    F1 = get_F1()
    P = sqrt(Fz**2 + (Fy + F1)**2)
    return P

# Calculate the direction of the force P wrt the y-axis
def get_theta():
    F1 = get_F1()
    theta = atan(Fz / (F1 + Fy))
    return theta

# Set the ratios of the dimensions
ratio_e_D = 1.5                    # Ratio e/D
ratio_D_t = 5                   # Ratio D/t

# Calculate the other dimensions based on D
e = ratio_e_D * D
w = 2 * e                         # Width
t = D / ratio_D_t                 # Thickness




# Calculate area A1
def get_A1():
    A1 = t * (2 * w - sqrt(2) * D) / 4
    return A1

# Calculate area A2
def get_A2():
    A2 = ((w - D) * t) / 2
    return A2

# Use A1 and A2 to determine area A_av
def get_A_av():
    A1 = get_A1()
    A2 = get_A2()
    A_av = 6 / ((4 / A1) + (2 / A2))
    return A_av

# Calculate area A_br
def get_Abr():
    A_br = D * t
    return A_br

# Calculate the ratio between the areas A_av/A_br
def get_Aav_over_Abr():
    A_av = get_A_av()
    A_br = get_Abr()
    return A_av/A_br

"""   Find critical loads   (transverse  and  axial)   """
"""   Transverse loads   """
# Find the coefficient Kty from graph of transverse loading
def get_Kty(ratio_areas):
    i = 0
    while i <= len(gp.x_transverse) - 1:
        if ratio_areas >= gp.x_transverse[i] and ratio_areas <= gp.x_transverse[i + 1]:     # Find the interval
            slope = (gp.y_transverse[i + 1] - gp.y_transverse[i]) / (gp.x_transverse[i + 1] - gp.x_transverse[i])
            Kty = gp.y_transverse[i] + slope * (ratio_areas - gp.x_transverse[i])
            break
        else:
            i += 1
    return Kty

# Find the critical force in the transverse direction Pty
def get_Pty():
    ratio_areas = get_Aav_over_Abr()
    Kty = get_Kty(ratio_areas)
    A_br = get_Abr()
    Pty = Kty * A_br * StrengthYield * 10**6
    return Pty


"""   Axial loads   """
# Find the coefficient Kbry from graph of axial loading
def get_Kbry(ratio_e_D):
    i = 0
    while i <= len(gp.x_axial) - 1:
        if ratio_e_D >= gp.x_axial[i] and ratio_e_D <= gp.x_axial[i + 1]:  # Find the interval
            slope = (gp.y_axial[i + 1] - gp.y_axial[i]) / (gp.x_axial[i + 1] - gp.x_axial[i])
            Kbry = gp.y_axial[i] + slope * (ratio_e_D - gp.x_axial[i])
            break
        else:
            i += 1
    return Kbry

# Find the critical force in the axial direction Pbry
def get_Pbry():
    Kbry = get_Kbry(ratio_e_D)
    A_br = get_Abr()
    Pbry = Kbry * A_br * StrengthUltimate * 10**6
    return Pbry


"""   Find the total critical force   (axial  +  transverse)   """
# Find the oblique critical force
def get_Pcr():
    Pty = get_Pty()
    Pbry = get_Pbry()
    P_cr = sqrt(Pty**2 + Pbry**2)
    return P_cr


"""   Test the factor of safety   """
# Find the factor of safety implied by the design
def get_MS_implied():
    P_cr = get_Pcr()
    P = get_P()
    MS_implied = P_cr / P
    return MS_implied

# Test if the factor of safety implied by the design is higher or equal to the factor of safety decided upon
def test():
    MS_implied = get_MS_implied()
    if MS_implied >= MS:
        print("The design is good. " + "The factor of safety is: " + str(MS_implied))
    else:
        print("The design is bad. " + "The factor of safety is: " + str(MS_implied))

# ratio_areas = get_Aav_over_Abr()
# print(ratio_areas)
test()











