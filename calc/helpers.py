prec = 0.004

def frange (val , bor1 , bor2):
    """Function is true if a value is between to others. Order of borders doesn't have an impact."""
    if ( (1-prec) * bor1 <= val <= bor2 * (1+prec) or (1-prec) * bor2 <= val <= bor1 * (1+prec) ):
        return True
    else:
        return False

def UmtoUs (val):
    """Function converts U/min to U/sec"""
    res  = val/60
    return res

def mmtom (val):
    """Function converts mm to m"""
    res = val/1000
    return res

def kWtoW (val):
    """Function converts kW to W"""
    res = val * 1000
    return val
