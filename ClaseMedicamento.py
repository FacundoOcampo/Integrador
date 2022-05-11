class medicamento:
    def __init__(self,Id,IdMed,Nom,Mono,Pres,Cant,Prec):
        self.__ID=Id
        self.__IdMed=IdMed
        self.__Nom=Nom
        self.__MonoDro=Mono
        self.__Presen=Pres
        self.__Cant=Cant
        self.__Prec=Prec

    def GetIdCama(self):
        return self.__ID
    def GetInfo(self):
        return "{:15}{:2}{:20}{:20}{:5}{:17.2f}\n".format(self.__Nom,"/",self.__MonoDro,self.__Presen,self.__Cant,self.__Prec)
    def GetPrec(self):
        return self.__Prec
