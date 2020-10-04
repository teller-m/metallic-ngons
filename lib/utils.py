import mpmath as mp
from . import DPS

def getkey(val): return mp.nstr(val, DPS)
def mmf(n): return (n+mp.sqrt(n*n+4))/2
