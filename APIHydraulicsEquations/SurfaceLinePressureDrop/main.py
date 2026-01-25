import math

# Conversion function
def feetToMeters(feet):
    return feet * 0.3048

def psiToBar(psi):
    return psi / 14.5038

# always using log10 for default calculations

print("SURFACE LINE PRESSURE DROP")

'''
Pipe "n" and "K" values:
np = 3.32 * log (Θ600 / Θ300) = 3.32 * log (34/53) =
Kp = 5.11 * log (Θ600) / 1022 np = 5.11 * log (53) / 1022 * 0.64 =
'''
Np = 3.32 * math.log10(34 / 53)
Kp = 5.11 * 53 / math.pow(1022, 0.64)

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
= ... cP
'''

ft = 24.48 * 335 / math.pow(3.826, 2) # or 3.826 ** 2

m = feetToMeters(ft)

Ev = 100 * 3.21 * ((math.pow((1.6 * 560.23) / 3.826, 0.64 - 1))) * math.pow((3 * 0.64 + 1) / (4 * 0.64), 0.64) # corrected formula

# Ev = 100 * 3.21 * ((1.6 * 560.23) / 3.826) ** (0.64 - 1) * ((3 * 0.64 + 1) / (4 * 0.64)) ** 0.64 # conventional formula

print('Surface Connection:')
print(f"Velocity = {ft} ft/min {m} m/min") # 560.23

print(f"Effective Viscosity = {Ev} cP") # 76.94

'''
Reynolds Number:
NRep = (15.467 * Vp*D*ρ) / μep
--> Reynolds number ? 2100;
'''
NRep = (15.467 * 560.23 * 3.826 * 12.8) / 48.97

print(f"Reynolds Number = {NRep}")

''' 
Friction Factor:
fp = {(log n + 3.93)/50} / [Nrep]{(1.75-log np)/7)}
'''
# issue
fp = ((math.log10(0.64) + 3.93) / 50) / math.pow(8.667, (1.75 - (math.log10(0.64)) / 7))

# fp = (((math.log10(0.64)) + 3.93) / 50) / 8.667 ** ((1.75 - math.log10(0.64)) / 7)

print(f"Friction Factor = {fp}")

'''
Pressure loss:
Pp (psi) = ((fp * Vp2 * ρ) / (92916 * D)) * Lm
'''
Pp_psi = ((0.006025 * math.pow(560.23, 2) * 12.8) / (92916 * 3.826)) * 610

bar = psiToBar(Pp_psi)

print(f"Pressure Loss = {Pp_psi} psi {bar} bar")