import math

# Conversion function
def feetToMeters(feet):
    return feet * 0.3048

# always using log10 for default calculations

'''
Pipe "n" and "K" values:
np = 3.32 * log (Θ600 / Θ300) = 3.32 * log (34/53) = ...
Kp = 5.11 * log (Θ600) / 1022 np = 5.11 * log (53) / 1022 * 0.64 = ...
'''
Np = 3.32 * math.log10(34 / 53)

Kp = 5.11 * 53 / (1022 ** 0.64)
# Kp = 5.11 * math.log10(53) / (1022 * 0.64)

print('Pipe "n" and "K" values:')
print(f"Np = {Np}") # 0.64
print(f"Kp = {Kp}") # 3.21

print("\n")

'''
Surface Connection:
Velocity: Vp
(ft/min) = 24.48 x Q (gpm) / D2 (in.) = 24.48 x 335 / 3.826
= ... ft/min ...m/min

Effective viscosity =
μep (cP)
= 100 * Kp * {(1.6 * Vp)/D)}(np-1) * {(3np + 1)/(4 * np)}np
= 100 * 3.21 * {(1.6 * 560.23)/3.826)(0.64-1) * {(3 * 0.64 + 1/(4 * 0.64) 0.64
= ... cP
'''

ft = (24.48 * 335) / math.pow(3.826, 2) # or 3.826 ** 2

meters = feetToMeters(ft)

# Ev = 100 * 3.21 * math.pow((1.6 * 560.23) / 3.826, (0.64 - 1)) * math.pow((3 * 0.64 + 1) / (4 * 0.64), 0.64) # incorrect formula

Ev = 100 * 3.21 * math.pow((1.6 * 560.23) / 3.826, 0.64 - 1) * math.pow((3 * 0.64) + 1 / (4 * 0.64), 0.64) # corrected formula

# Ev = 100 * 3.21 * ((1.6 * 560.23) / 3.826) ** (0.64 - 1) * (3 * 0.64 + (1 / (4 * 0.64))) ** 0.64 # conventional formula

print('Surface Connection:')
print(f"{ft} ft/min") # 560.23
print(f"{meters} m/min") # 170.77

print(f"Effective viscosity: {Ev} cP") # 76.95