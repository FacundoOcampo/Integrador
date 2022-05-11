import csv
import numpy as np
from ClaseCama import cama

class ManCama:
    __Dim=0
    __Cant=0
    __Inc=0
    __Archivo=open("camas.csv","r")
    def __init__(self):
        self.__Dim=ManCama.CalDim(self.__Archivo)
        self.__Arr=np.empty(self.__Dim,dtype=cama)

    def Cargar(self,Reader):
        Band=False
        for fila in Reader:
            if Band==False:
                Band=True
            else:
                if self.__Dim == self.__Cant:
                    self.__Dim=self.__Inc+self.__Dim
                    self.__Arr.resize(self.__Dim)
                NuevaCama=cama(int(fila[0]),int(fila[1]),bool(fila[2]),str(fila[4]),str(fila[5]),str(fila[6]),str(fila[3]))
                self.__Arr[self.__Cant]=NuevaCama
                self.__Cant=self.__Cant+1

    def Buscar(self,Nom,NuevMed):
        Ban=True
        for i in range(len(self.__Arr)):
            if Nom == self.__Arr[i].GetNom():
                self.__Arr[i].CamFech()
                print("Paciente: {}     Cama: {}     Habitacion: {}\nDiagnostico: {}     Fecha de internacion: {}\nFecha de Alta: {}".format(self.__Arr[i].GetNom(),self.__Arr[i].GetID(),self.__Arr[i].GetHab(),self.__Arr[i].GetDiag(),self.__Arr[i].GetFechInt(),self.__Arr[i].GetFechAlt()))
                NuevMed.Info(self.__Arr[i].GetID())
                break
        if Ban ==False:
            print("Paciente no encontrado")



    def Listar(self,Diag):
        for i in range(len(self.__Arr)):
            if(self.__Arr[i].GetEst()==True):
                if self.__Arr[i].GetDiag()==Diag:
                    print("Cama: {}       Habitacion: {}       Nombre: {}       Fecha de internacion: {}\n".format(self.__Arr[i].GetID(),self.__Arr[i].GetHab(),self.__Arr[i].GetNom(),self.__Arr[i].GetFechInt()))

    @classmethod
    def CalDim(cls,Archi):
        Reader=csv.reader(Archi,delimiter=";")
        Cant=0
        Band=False
        for i in Reader:
            if Band==False:
                Band=True
            else:
                Cant+=1
        return Cant
