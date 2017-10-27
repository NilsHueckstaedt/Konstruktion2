from helpers import *
# Konstanten Deklaration
MomAbMin1 = 790     # Minimales Abtriebsmoment Gang 1, Nm
DrehAbMin1 = UmtoUs(360)    # Minimale Abtriebsdrehzahl Gang 1, 1/min
DrehAbMin2 = UmtoUs(900)    # Minimale Abtriebsdrehzahl Gang 2, 1/min
DrehAbTol = 2       # Toleranz der Abtriebsdrehzahlen nach oben, %
Modul = mmtom(5)           # Normalmodul, mm
z1 = 17             # Zähnezahl Zahnrad 1, 1
AbstW1W2Min = mmtom(124)   # Abstand zwischen Welle 1 und Welle 2, mm
AbstW1W2Tol = 0.5   # Toleranz des Abstandes zwischen Welle 1 und Welle 2, %
BemLeisMotor = kWtoW(7.5)  # Bemessungsleistung des Motors, kW
DrehMotor = UmtoUs(1445)    # Drehzahl des Motors, 1/min
WirkMotor = 87      # Wirkungsgrad des Motors bei 100%, %
