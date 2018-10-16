import json                 #Libreria para leer JSON
from xlwt import Workbook              #Libreria par escritura en Excel
import os                   #Permite acceder a funcionalidades dependientes del Sistema Operativo



listadoArchivos = os.listdir('.') #Obtiene el listado de archivos en un directorio, no lo necesitas creo
listadoArchivos = ["FactSolicitudCompra.json"] #Pone el nombre de un archivo para procesar, modifica este y pon el sln
listadoLimpio=[]

metricas=[]


#Selecciona solo los archivos presentes en el directorio que terminan en .dtsx
for each in listadoArchivos: #Para todos los archivos en el directorio 
    if ".json" in each:     #Si contienen .json en algun lado
        listadoLimpio.append(each)  #Agregar a la lista de archivos a procesar nueva


print(listadoArchivos)

libro = Workbook() #Crear un libro de excel
cursor=0;
hoja1 = libro.add_sheet('Relaciones') #Agregar una hoja al libro
hoja1.write(0,1,'Origen')
hoja1.write(0,2,'Campo')
hoja1.write(0,3,'Campo')
hoja1.write(0,4,'Destino')

hoja1.col(0).width=1000
hoja1.col(1).width=10000
hoja1.col(2).width=10000
hoja1.col(3).width=10000
hoja1.col(4).width=10000

#print("-- TABLAS --")

for element in listadoLimpio: #Para cada archivo en la lista de archivos
    t=1 #Persistencia del cursor a través de archivos
    y=0#Persistencia del cursor a través de archivos
    cont = 0;#Cursor para definir en que fila del excel estoy escribiendo
            
    file= open('FactSolicitudCompra.json')
    data=json.load(file)
            
    for r in data['model']['relationships']:
        hoja1.write(t,y,t)
        print(r['fromTable']) # Origrn
        print(r['fromColumn']) # campo
        print(r['toColumn']) # Hasta  
        print(r['toTable']) # Hasta

        hoja1.write(t,y+1,r['fromTable'])
        hoja1.write(t,y+2,r['fromColumn'])
        hoja1.write(t,y+3,r['toColumn'])
        hoja1.write(t,y+4,r['toTable'])
        t=t+1
libro.save('37.FactSolicitudCompra.xls')
