from helpers import *
# Konstanten Deklaration, NUR DIESE WERTE BEARBEITEN
MomAbMin1 = 790     # Minimales Abtriebsmoment Gang 1, Nm
DrehAbMin1 = UmtoUs(360)    # Minimale Abtriebsdrehzahl Gang 1, 1/min
DrehAbMin2 = UmtoUs(900)    # Minimale Abtriebsdrehzahl Gang 2, 1/min
DrehAbTol = 2       # Toleranz der Abtriebsdrehzahlen nach oben, %
Modul = mmtom(5)           # Normalmodul, mm
z1 = 17             # Zähnezahl Zahnrad 1, 1
AbstW1W2Min = mmtom(124)   # Abstand zwischen Welle 1 und Welle 2, mm
AbstW1W2Tol = 0.5   # Toleranz des Abstandes zwischen Welle 1 und Welle 2, %
BemLeisMotor = kWtoW(7.5)  # Bemessungsleistung des Motors, kW
DrehAn = UmtoUs(1445)    # Drehzahl des Motors, 1/min
WirkMotor = 87      # Wirkungsgrad des Motors bei 100%, %


# -------------------------------------------------------------------------------------------
DrehAbMax1 = DrehAbMin1 * (1 + DrehAbTol/100)
DrehAbMax2 = DrehAbMin2 * (1 + DrehAbTol/100)
AbstW1W2Max = AbstW1W2Min * (1 + AbstW1W2Tol/100)
Leistung = BemLeisMotor * (WirkMotor/100)
MomentAn = Leistung / DrehAn
UberGesMin1 = DrehAn/DrehAbMin1    # Gesamtübersetzung mindestens Gang 1, 1
UberGesMax1 = DrehAn/DrehAbMax1    # Gesamtübersetzung maximal Gang 1, 1
UberGesMin2 = DrehAn/DrehAbMin2    # Gesamtübersetzung mindestens Gang 2, 1
UberGesMax2 = DrehAn/DrehAbMax2    # Gesamtübersetzung maximal Gang 2, 1
