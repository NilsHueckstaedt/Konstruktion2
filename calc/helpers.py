from vars import prec

def frange (val , bor1 , bor2):
    """Function is true if a value is between to others. Order of borders doesn't have an impact."""
    if ( (1-prec) * bor1 <= val <= bor2 * (1+prec) or (1-prec) * bor2 <= val <= bor1 * (1+prec) ):
        return True
    else:
        return False
