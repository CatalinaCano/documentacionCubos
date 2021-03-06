#NOTA IMPORTANTE DEBE CORRERSE CON PYTHON 3 SINO DA ERRORES EN LOS CARACTERES ESPECIALES
import os
import json  #Libreria para leer JSON
from xlwt import Workbook #Libreria par escritura en Excel

#Define la ejecucion del programa
if __name__ == '__main__':
    listadoArchivos = os.listdir('.') #Obtiene el listado de archivos en un directorio
    listadoLimpio=[]
    metricas=[]

    #Selecciona solo los archivos presentes en el directorio que terminan en .json
    for each in listadoArchivos: #Para todos los archivos en el directorio
        if ".json" in each and ".py" not in each and ".xls" not in each:   #Si contienen .json en algun lado
            listadoLimpio.append(each)  #Agregar a la lista de archivos a procesar

    print(listadoLimpio)

    print("-- TABLAS --")

    for element in listadoLimpio: #Para cada archivo en la lista de archivos
        t=1 #Persistencia del cursor a través de archivos
        y=0#Persistencia del cursor a través de archivos
        cont = 0;#Cursor para definir en que fila del excel estoy escribiendo
        libro = Workbook() #Crear un libro de excel
        cursor=0;
        hoja1 = libro.add_sheet('Tablas') #Agregar una hoja al libro
        hoja1.write(0,1,'Tablas del Cubo')

        hoja1.write(0,2,'Tablas de la Bodega')
        hoja1.write(0,3,'Query')

        hoja1.col(0).width=1000
        hoja1.col(1).width=10000
        hoja1.col(2).width=10000
        hoja1.col(3).width=50000

        file= open(element)
        data=json.load(file)
        for table in data['model']['tables']:
            nombreTabla= table['name']
            hoja1.write(t,y,t)
            hoja1.write(t,y+1,nombreTabla)
            for anno in table['annotations']:
                if anno ['name'].find('_TM_ExtProp_DbTableName')!=-1:
                    hoja1.write(t,y+2,anno['value'])
            for  p in table['partitions']:
                hoja1.write(t,y+3,p['source']['query'])
            t=t+1
        hoja2= libro.add_sheet('Metricas')
        hoja2.write(0,1,'Metricas')
        hoja2.col(0).width=1000
        hoja2.col(1).width=6000
        hoja2.col(2).width=50000
        nombreMetrica=[]
        q=1
        g=0
        u=1

        for tab in data['model']['tables']:
            if  tab ['name'][0].find("M")== -1:  #Son Dimensiones
                print (tab['name'])
            else: #Son Metricaas
                hoja2.write(q,g,q)
                hoja2.write(q,g+1,tab['name'])
                for m in tab['measures']:
                    expr= m['name'],":=",m['expression']
                    #hoja2.write(u,y+2,str(expr)) #con caracteres especiales
                    hoja2.write(u,y+2,expr) #normal
                    u=u+1
                q=u

        jerarquias=[]
        hoja3= libro.add_sheet('Jerarquias')
        hoja3.write(0,1,'Tabla de la Jerarquia')
        hoja3.write(0,2,'Nombre de la Jerarquia')
        hoja3.write(0,3,'Niveles de la Jerarquia')
        hoja3.col(0).width=1000
        hoja3.col(1).width=5000
        hoja3.col(2).width=5000
        hoja3.col(3).width=7000
        cv=1
        ly=3
        lx=2
        cg=1

        for tx in data['model']['tables']:
            if 'hierarchies' in tx :
                for h in tx['hierarchies']:
                    hoja3.write(cv,y,cv)
                    hoja3.write(cv,y+1,tx['name'])
                    hoja3.write(cv,y+2,h['name'])
                    for l in h['levels']:
                        hoja3.write(cg,y+3,l['name'])
                        cg=cg+1
                    cv=cg
        hoja4= libro.add_sheet('Roles')
        hoja4.write(0,1,'Nombre del Rol')
        hoja4.write(0,2,'Permisos')
        hoja4.write(0,3,'Miembros')
        hoja4.col(0).width=1000
        hoja4.col(1).width=15000
        hoja4.col(2).width=4000
        hoja4.col(3).width=15000
        hr=1
        y=0
        cr=1
        for r in data['model']['roles']:
            hoja4.write(hr,y,hr)
            hoja4.write(hr,y+1,r['name'])
            hoja4.write(hr,y+2,r['modelPermission'])
            if 'members' in r:
                for m in r['members']:
                    hoja4.write(cr,y+3,m['memberName'])
                    cr=cr+1
            hr=hr+cr
        libro.save(element.replace('.json','.xls'))
