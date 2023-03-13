import requests
from bs4 import BeautifulSoup


class Stop():
    """
    Class to represent a bus stop
    """


    def __init__(self, name, times):
        self.name = name
        self.times = times

    def __repr__(self):
        return self.name

    def __str__(self) -> str:
        return self.name



class Lane():
    """
    Class to represent a bus lane

    """


    def __init__(self,url:str):
        """
        url: url of the lane
        """
        self.url = url
        self.stop_list = []
        self.name=self.__get_Info()

    def __get_Info(self):
        """
        Get the name of the lane and the list of stops aswell as the times
        """
        page = requests.get(self.url)
        soup=BeautifulSoup(page.content, "html.parser")


        #Get the name of the Lane
        lane_name=soup.find("span",class_="is-Badge-Text").text.replace(" ","").replace("Ligne","").replace("\n","")+" "+ soup.find("strong",class_="is-Button-Content").text
        
        stop_list = soup.find_all("tr", class_="is-Equalizer")
        for stop in stop_list:
            #Get the name of the stop
            name=stop.find("strong","is-Timesheet-StopPoint-Name").text

            #Get the times
            time_list=stop.find_all("span", class_="is-Timesheet-Passage-Item-C1")
            for i in range (len(time_list)):
                time_list[i]=time_list[i].text.replace(" ","").replace("\n","")

            self.stop_list.append(Stop(name,time_list))
        return lane_name
    
    def __repr__(self):
        """
        Return the name of the lane
        """
        return self.name 

    def getStopTimes(self):
        """
        Return a dictionnary with the name of the stop as key and the list of times as value
        """
        dict_stop={}
        for stop in self.stop_list:
            dict_stop[str(stop)]=stop.times
        return dict_stop


    def getStopList(self):
        """
        Return the list of stops objects
        """
        return self.stop_list

    def getStop(self,stop_name:str):
        """
        Return the stop object with the name stop_name
        """
        for stop in self.stop_list:
            if stop.name==stop_name:
                return stop
        return None
    

    def getLanesName():
        """
        return a dictonnary with the name of the lane as key and the lane url as value\n
        ex: getLane()["Haut de Bayonne"] -> url of the lane\n
        Only T1,T2 and A4 lanes are available for now\n
        use the constructor Lane(url) if you want to get a lane that is not in the dict or add it to the dict
        """
        Lanes={
            "Haut de Bayonne":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/T1/direction/RETURN/T1",
            "Mairie de Biarritz":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/T1/direction/FORWARD/T1",
            "Bayonne Marrac":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/T2/direction/OUTWARD/T2",
            "Tarnos Garròs":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/T2/direction/RETURN/T2",
            "Biarritz Aeroport":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/4/direction/FORWARD/4",
            "Bayonne Saisonton":"https://itineraires.txiktxak.fr/fr/horaires/TXIK-TXAK-Nord/Bus/ligne/4/direction/RETURN/4",
            #Follow this pattern to add more lanes to the dict
            #Because it as to be done manually and there is a lot of lanes and don't have the time to do it
        }
        return Lanes
        
    def getLane(lane_name:str):
        """
        return the lane Object of the lane name in argument
        """
        return Lane(Lane.getLanesName()[lane_name])



