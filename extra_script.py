Import('env')
from os.path import join, realpath

MCU = env.get('BOARD_MCU')
FPU = env.get('BOARD_FPU')

if FPU != None and FPU != '':
    MCU=join (MCU, FPU)

env.Append(
    LIBPATH=[realpath(join('src', MCU))],
    LIBS=['algobsec']
)
