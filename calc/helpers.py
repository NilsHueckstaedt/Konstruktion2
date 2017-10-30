prec = 0.0032
def frange (val , bor1 , bor2):
    """Function is true if a value is between to others. Order of borders doesn't have an impact."""
    if ( (1-prec) * bor1 <= val <= bor2 * (1+prec) or (1-prec) * bor2 <= val <= bor1 * (1+prec) ):
        return True
    else:
        return False

def UmtoUs (Umin):
    """Function converts U/min to U/sec."""
    Us  = Umin/60
    return Us

def UstoUm (Us):
    """Function converts U/s to U/min."""
    Umin  = Us * 60
    return Umin

def mmtom (mm):
    """Function converts mm to m."""
    m = mm/1000
    return m

def mtomm (m):
    """Function converts m to mm."""
    mm = m * 1000
    return mm


def kWtoW (kW):
    """Function converts kW to W."""
    W = kW * 1000
    return W

def abst (z1 , z2):
    """Function calculates the distance between to gears"""
    from vars import Modul
    ab =  Modul * (z1 + z2) / 2
    return ab

def radius (z):
    """Function calculates the radius of a gear"""
    from vars import Modul
    rad = z * Modul / 2
    return rad

def moment (dreh):
    """Function calculates the Moment from a given rotation"""
    from vars import Leistung
    mom = Leistung / dreh
    return mom
