#!/usr/bin/env python3
# coding: utf8

prec = 0.00305
# Konstanten Deklaration
MomAbMin1 = 790     # Minimales Abtriebsmoment Gang 1, Nm
DrehAbMin1 = 360    # Minimale Abtriebsdrehzahl Gang 1, 1/min
DrehAbMin2 = 900    # Minimale Abtriebsdrehzahl Gang 2, 1/min
DrehAbTol = 2       # Toleranz der Abtriebsdrehzahlen nach oben, %
Modul = 5           # Normalmodul, mm
z1 = 17             # Zähnezahl Zahnrad 1, 1
AbstW1W2Min = 124   # Abstand zwischen Welle 1 und Welle 2, mm
AbstW1W2Tol = 0.5   # Toleranz des Abstandes zwischen Welle 1 und Welle 2, %
BemLeisMotor = 7.5  # Bemessungsleistung des Motors, kW
DrehMotor = 1445    # Drehzahl des Motors, 1/min
WirkMotor = 87      # Wirkungsgrad des Motors bei 100%, %


# Konstanten Umrechnung nach SI
# 1/min -> 1/s
DrehAbMin1 = DrehAbMin1/60
DrehAbMin2 = DrehAbMin2/60
DrehMotor = DrehMotor/60
# mm -> m
Modul = Modul/1000
AbstW1W2Min = AbstW1W2Min/1000
# kW -> W
BemLeisMotor = BemLeisMotor * 1000


# Berechnung resultierender Konstanten, alle SI
DrehAbMax1 = DrehAbMin1 * (1 + DrehAbTol/100)
DrehAbMax2 = DrehAbMin2 * (1 + DrehAbTol/100)
AbstW1W2Max = AbstW1W2Min * (1 + AbstW1W2Tol/100)
LeisMotor = BemLeisMotor * (WirkMotor/100)
DrehAn = DrehMotor

UberGesMin1 = DrehAn/DrehAbMin1    # Gesamtübersetzung mindestens Gang 1, 1
UberGesMax1 = DrehAn/DrehAbMax1    # Gesamtübersetzung maximal Gang 1, 1
UberGesMin2 = DrehAn/DrehAbMin2    # Gesamtübersetzung mindestens Gang 2, 1
UberGesMax2 = DrehAn/DrehAbMax2    # Gesamtübersetzung maximal Gang 2, 1

# Berechnung Ergebnisse
# print ("Gültige Zähnezahlpaarungen für Üb 1:")
for z2 in range(1,300):
    Abstand12 = Modul * (z1 + z2) / 2
    # print (Abstand , AbstW1W2Min , AbstW1W2Max)
    if ((1-prec) * AbstW1W2Min <= Abstand12 <= AbstW1W2Max * (1+prec)):
        Uber12 = z2/z1
        for z3 in range(1,300):
            Uber23 = z3/z2
            Uber13 = Uber12 * Uber23
            if ((1-prec) * UberGesMax1 <= Uber13 <= UberGesMin1 * (1+prec)):
                 for z4 in range(1,300):
                     for z5 in range(1,300):
                         Uber45 = z5/z4
                         Uber15 = Uber12 * Uber45
                         if ((1-prec) * UberGesMax2 <= Uber15 <= UberGesMin2 * (1+prec)):
                             Abstand23 = Modul * (z2 + z3) / 2
                             Abstand45 = Modul * (z4 + z5) / 2
                             if (abs(Abstand45 - Abstand23) <= 1/1000):
                                 print ("-----------------------")
                                 print ("Ergebnis \n")
                                 print ("Übersetzung (Gang 1):" , Uber13)
                                 print ("Übersetzung (Gang 2):" , Uber15 , "\n")
                                 print ("Abstand der Wellen 1 und 2:" , Abstand12)
                                 print ("Abstand der Wellen 2 und 3:" , Abstand23)
                                 print ("Querverschub zwischen z3 und z5:" , Abstand23 - Abstand45 , "\n")
                                 print("Zähnezahlen")
                                 print ("\n Z1:" , z1 , "\n Z2:" , z2 , "\n Z3:" , z3 , "\n Z4:" , z4 , "\n Z5:" , z5)
                                 print ("-----------------------")


# Ausgaben
# print ("Tatsächliche Leistung des Motors" , LeisMotor , "W")
print ("Übersetzungsspektrum Gang 1 (ges): zwischen" , UberGesMax1 , "und" , UberGesMin1)
print ("Übersetzungsspektrum Gang 2 (ges): zwischen" , UberGesMax2 , "und" , UberGesMin2)
# print ("Achsenabstand Welle 1 und 2: zwischen" , AbstW1W2Min*1000 , "und" , AbstW1W2Max*1000 , "mm")
