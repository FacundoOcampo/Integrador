from ClaseMedicamento import medicamento

class ManMed:
    __List=[]
    def __init__(self):
        self.__List=[]
    def Cargar(self,Reader):
        Band=False
        for fila in Reader:
            if Band==False:
                Band=True
            else:
                NuevoMed=medicamento(int(fila[0]),int(fila[1]),str(fila[2]),str(fila[3]),str(fila[4]),int(fila[5]),int(fila[6]))
                self.__List.append(NuevoMed)

    def Info(self,Id):
        acum=0
        s="{:37}{:20}{:15}{}\n".format("Medicamento/monodroga","Presentacion","Cantidad","Precio")
        for fila in range(len(self.__List)):
            if(self.__List[fila].GetIdCama()==Id):
                Cadena=self.__List[fila].GetInfo()
                s+=str(Cadena)
                acum=self.__List[fila].GetPrec()+acum
        print(s+"Total adeudado:{:64.2f}".format(acum))
