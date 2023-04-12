Import('env')
from os.path import join, realpath

MCU = env.get('BOARD_MCU')

if MCU == 'nrf52840':
    MCU = 'cortex-m4/fpv4-sp-d16-hard'

print('BSEC Software Library: MCU = ' + MCU)

env.Append(
    LIBPATH=[realpath(join('src', MCU))],
    LIBS=['algobsec']
)
