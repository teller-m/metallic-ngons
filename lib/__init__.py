from mpmath import mp
from .argparser import args

DPS = args.dps
DPS_BUFFER = args.buffer + int(mp.log10(DPS))
# set mpmath decimal precision
mp.dps = DPS + DPS_BUFFER
