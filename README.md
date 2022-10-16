# txiktxak-web-scraper
Python module to retrieve stop information and timetables of chronoplus-txiktxak buses with the web-scraping method


# How does it work

Simply find the timetable page of your bus line on the page [https://itineraires.txiktxak.fr/fr/](https://itineraires.txiktxak.fr/fr/).

Use this link to create the "bus route" object.
Be careful, an outbound and an inbound are not the same line, you will have to create them separately 

```python
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
```

You can also simply use  the getLane method without having to look for the link of the lane (it is directly integrated in the module). For the moment it only works for the T1, T2 and 4 lanes because it as to be done manually and there is a lot of lanes and I don't have the time to do it.
You can add your lanes with their respective url in the txiktxak.py file
```python
#return the lane object of the lane "Haut de Bayonne"
T1_return=Lane.getLane("Haut de Bayonne")

#return the lane object of the lane "Mairie de Biarritz"
T1_forward=Lane.getLane("Mairie de Biarritz")
```

# Limitations

I have noticed several times that the request does not return the stop times but this is simply because they are not available on the site of txiktxak.

Moreover their page is quite heavy to load which makes the data retrieval quite slow (approximately 3sec per requests)

		

