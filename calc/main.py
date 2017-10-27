#!/usr/bin/env python3
# coding: utf8

from vars import *
from helpers import *

# Berechnung resultierender Konstanten,

# Berechnung Ergebnisse
for z2 in range(1,300):
    Abstand12 = abst(z1 , z2)
    # print (Abstand , AbstW1W2Min , AbstW1W2Max)
    if (frange(Abstand12 , AbstW1W2Min , AbstW1W2Max)):
        Uber12 = z2/z1
        for z3 in range(1,300):
            Uber23 = z3/z2
            Uber13 = Uber12 * Uber23
            if (frange(Uber13 , UberGesMin2 , UberGesMax2)):
                for z4 in range(1,300):
                    for z5 in range(1,300):
                        Uber45 = z5/z4
                        Uber15 = Uber12 * Uber45
                        if (frange(Uber15 , UberGesMin1 , UberGesMax1)):
                            Abstand23 = abst(z2 , z3)
                            Abstand45 = abst(z4 , z5)

                            if (abs(Abstand45 - Abstand23) <= 0.005):
                                zahne = ["You did something wrong" , z1 , z2 , z3 , z4 , z5]
                                print ("-----------------------")
                                print ("Ergebnis \n")
                                print ("Abstände Welle 2 und Welle 3" , mtomm(Abstand45) , mtomm(Abstand23))
                                print ("Übersetzungen")
                                print ("\n Übersetzung (Gang 1):" , Uber13)
                                print ("\n Übersetzung (Gang 2):" , Uber15)
                                print ("\n Übersetzung z1 zu z2:" , Uber12)
                                print ("\n Übersetzung z2 zu z3:" , Uber23)
                                print ("\n Übersetzung z4 zu z5:" , Uber45 , "\n")
                                print ("Abstände in mm")
                                print ("\n Abstand der Wellen 1 und 2:" , mtomm(Abstand12))
                                print ("\n Abstand der Wellen 2 und 3:" , mtomm(Abstand23) , "\n")
                                print ("Zähnezahlen")
                                for i in range(1,6):
                                    print ("\n Zahnrad" , i , zahne[i])
                                print ("")
                                print ("Radien und Durchmesser in mm")
                                for i in range(1,6):
                                    print ("\n Zahnrad" , i , mtomm(radius(zahne[i])) , "|" , mtomm(radius(zahne[i])) * 2)
                                print ("")
                                print ("Drehzahlen in 1/min")
                                print ("\n Antrieb" , UstoUm(DrehAn))
                                print ("\n Abtrieb Gang 1", UstoUm(DrehAn / Uber13))
                                print ("\n Abtrieb Gang 2", UstoUm(DrehAn / Uber15) , "\n")
                                print ("Moment in Nm")
                                print ("\n Antrieb" , UstoUm(DrehAn))
                                print ("\n Abtrieb Gang 1", MomentAn * Uber13)
                                print ("\n Abtrieb Gang 2", MomentAn * Uber15)
                                # print ("Moment Gang 2")
                                print ("-----------------------")

for z2 in range(1,300):
    Abstand12 = abst(z1 , z2)
    # print (Abstand , AbstW1W2Min , AbstW1W2Max)
    if (frange(Abstand12 , AbstW1W2Min , AbstW1W2Max)):
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
                            Abstand23 = abst(z2 , z3)
                            Abstand45 = abst(z4 , z5)

                            if (abs(Abstand45 - Abstand23) <= 0.001):
                                zahne = ["You did something wrong" , z1 , z2 , z3 , z4 , z5]
                                print ("-----------------------")
                                print ("Ergebnis \n")
                                print ("Abstände Welle 2 und Welle 3" , mtomm(Abstand45) , mtomm(Abstand23))
                                print ("Übersetzungen")
                                print ("\n Übersetzung (Gang 1):" , Uber13)
                                print ("\n Übersetzung (Gang 2):" , Uber15)
                                print ("\n Übersetzung z1 zu z2:" , Uber12)
                                print ("\n Übersetzung z2 zu z3:" , Uber23)
                                print ("\n Übersetzung z4 zu z5:" , Uber45 , "\n")
                                print ("Abstände in mm")
                                print ("\n Abstand der Wellen 1 und 2:" , mtomm(Abstand12))
                                print ("\n Abstand der Wellen 2 und 3:" , mtomm(Abstand23) , "\n")
                                print ("Zähnezahlen")
                                for i in range(1,6):
                                    print ("\n Zahnrad" , i , zahne[i])
                                print ("")
                                print ("Radien und Durchmesser in mm")
                                for i in range(1,6):
                                    print ("\n Zahnrad" , i , mtomm(radius(zahne[i])) , "|" , mtomm(radius(zahne[i])) * 2)
                                print ("")
                                print ("Drehzahlen in 1/min")
                                print ("\n Antrieb" , UstoUm(DrehAn))
                                print ("\n Abtrieb Gang 1", UstoUm(DrehAn / Uber13))
                                print ("\n Abtrieb Gang 2", UstoUm(DrehAn / Uber15) , "\n")
                                print ("Moment in Nm")
                                print ("\n Antrieb" , UstoUm(DrehAn))
                                print ("\n Abtrieb Gang 1", MomentAn * Uber13)
                                print ("\n Abtrieb Gang 2", MomentAn * Uber15)
                                # print ("Moment Gang 2")
                                print ("-----------------------")


# Ausgaben
print ("Tatsächliche Leistung im Getriebe" , Leistung , "W")
print ("Übersetzungsspektrum Gang 1 (ges): zwischen" , UberGesMax1 , "und" , UberGesMin1)
print ("Übersetzungsspektrum Gang 2 (ges): zwischen" , UberGesMax2 , "und" , UberGesMin2)
print ("Achsenabstand Welle 1 und 2: zwischen" , AbstW1W2Min*1000 , "und" , AbstW1W2Max*1000 , "mm")
