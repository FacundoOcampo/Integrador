import csv
from ManejadorCama import ManCama
from ManejadorMedicamento import ManMed


if __name__ == '__main__':
    #Carga el archivo "camas" y crea las instancias
    ArchivoC=open("camas.csv","r")
    ReaderC=csv.reader(ArchivoC,delimiter=";")
    NuevoManCama=ManCama()
    NuevoManCama.Cargar(ReaderC)
    #Carga el archivo "medicamentos" y crea las instancias
    ArchivoM=open("medicamentos.csv","r")
    ReaderM=csv.reader(ArchivoM,delimiter=";")
    NuevoManMed=ManMed()
    NuevoManMed.Cargar(ReaderM)

    NomPac=str(input("Ingrese el nombre de un paciente:\n"))
    NuevoManCama.Buscar(NomPac,NuevoManMed)

    Diag=str(input("Ingrese el diagnostico\n"))
    NuevoManCama.Listar(Diag)
