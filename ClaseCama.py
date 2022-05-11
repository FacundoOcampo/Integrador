from datetime import datetime

class cama:
    def __init__(self,Id,Habitacion,Estado,diag,FechInit,FechAlt,ApellyNom=None):
        self.__ID=Id
        self.__Habitacion=Habitacion
        self.__Estado=Estado
        if Estado==True:
            self.__ApellyNom=ApellyNom
        else:
            self.__ApellyNom=None
        self.__Diag=diag
        self.__FechInt=FechInit
        self.__FechAlt=FechAlt
    def GetNom(self):
        return self.__ApellyNom
    def GetID(self):
        return self.__ID
    def GetHab(self):
        return self.__Habitacion
    def GetDiag(self):
        return self.__Diag
    def GetFechInt(self):
        return self.__FechInt
    def GetFechAlt(self):
        return self.__FechAlt
    def GetEst(self):
        return self.__Estado
    def CamFech(self):
        self.__FechAlt=datetime.today().strftime('%Y-%m-%d')
