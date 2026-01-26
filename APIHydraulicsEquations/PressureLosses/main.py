import math

'''
Pressure Losses Calculations in PSI and BAR
'''
surface_line_pressure_drop_psi = 41.53
surface_line_pressure_drop_bar = 2.86

drill_string_interval1_drill_pipe_psi = 0.79
drill_string_interval1_drill_pipe_bar = 0.05

drill_string_interval2_drill_collar_psi = 377.52
drill_string_interval2_drill_collar_bar = 26.02

annular_interval1_drill_collar_psi = 16659.27
annular_interval1_drill_collar_bar = 1148.61

annular_interval2_drill_pipe_psi = 15342.69
annular_interval2_drill_pipe_bar = 1057.83

annular_interval3_casing_drill_pipe_psi = 178446.12
annular_interval3_casing_drill_pipe_bar = 12303.40

psi_result = surface_line_pressure_drop_psi + drill_string_interval1_drill_pipe_psi + drill_string_interval2_drill_collar_psi + annular_interval1_drill_collar_psi + annular_interval2_drill_pipe_psi + annular_interval3_casing_drill_pipe_psi
bar_result = surface_line_pressure_drop_bar + drill_string_interval1_drill_pipe_bar + drill_string_interval2_drill_collar_bar + annular_interval1_drill_collar_bar + annular_interval2_drill_pipe_bar + annular_interval3_casing_drill_pipe_bar

print(f'Bit Pressure Drop = {psi_result} psi {bar_result} bar')