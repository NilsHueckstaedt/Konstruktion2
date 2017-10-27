#!/usr/bin/env python3
# coding: utf8

from vars import *
from helpers import *

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
            if (frange(Uber13 , UberGesMin1 , UberGesMax1)):
                 for z4 in range(1,300):
                     for z5 in range(1,300):
                         Uber45 = z5/z4
                         Uber15 = Uber12 * Uber45
                         if (frange(Uber15 , UberGesMin2 , UberGesMax2)):
                             Abstand23 = Modul * (z2 + z3) / 2
                             Abstand45 = Modul * (z4 + z5) / 2
                             if (Abstand45 == Abstand23):
                                 zahne = [z1 , z2 , z3 , z4 , z5]
                                 print ("-----------------------")
                                 print ("Ergebnis \n")
                                 print ("Übersetzung (Gang 1):" , Uber13)
                                 print ("Übersetzung (Gang 2):" , Uber15 , "\n")
                                 print ("Abstand der Wellen 1 und 2:" , Abstand12)
                                 print ("Abstand der Wellen 2 und 3:" , Abstand23)
                                 print ("Querverschub zwischen z3 und z5:" , Abstand23 - Abstand45 , "\n")
                                 print("Zähnezahlen")
                                 for i in range(0,5):
                                     print ("\n Zahnrad" , i+1 , zahne[i])
                                 print("Durchmesser und Radien in mm")
                                 for i in range(0,5):
                                     print ("\n Zahnrad" , i+1 , (zahne[i] / Modul) * 1000)
                                # print ("Moment Gang 2")
                                 print ("-----------------------")


# Ausgaben
# print ("Tatsächliche Leistung des Motors" , LeisMotor , "W")
print ("Übersetzungsspektrum Gang 1 (ges): zwischen" , UberGesMax1 , "und" , UberGesMin1)
print ("Übersetzungsspektrum Gang 2 (ges): zwischen" , UberGesMax2 , "und" , UberGesMin2)
# print ("Achsenabstand Welle 1 und 2: zwischen" , AbstW1W2Min*1000 , "und" , AbstW1W2Max*1000 , "mm")
