from txiktxak import *

#Create a lane object from the Lane 34 direction "Anglet Bordes/Troix Croix"
MyLaneInOneWay=Lane("https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/34/direction/OUTWARD/CHRONOPLUS:34")

#Create a lane object from the Lane 34 direction "Anglet Chambre d'Amour"
MyLaneTheOtherWay=Lane("https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/34/direction/RETURN/CHRONOPLUS:34")

#Print the name of the lane
print(MyLaneInOneWay,"\n")
print(MyLaneTheOtherWay,"\n")

#Print the list of stops
print(MyLaneInOneWay.getStopList(),"\n")
print(MyLaneTheOtherWay.getStopList(),"\n")

#Print the list of times for the stop "Minerva"
print(MyLaneInOneWay.getStopTimes()["Minerva"],"\n")
print(MyLaneTheOtherWay.getStopTimes()["Minerva"],"\n")

#Return the stop object "Minerva"
stop=MyLaneInOneWay.getStop("Minerva")


#return the lane object of the lane "Haut de Bayonne"
T1_return=Lane.getLane("Haut de Bayonne")

#return the lane object of the lane "Mairie de Biarritz"
T1_forward=Lane.getLane("Mairie de Biarritz")