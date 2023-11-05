import os
import requests
import datetime

# el ahora es el ahora o.O
ahora = datetime.datetime.now()
'''
Organizar los archivos en rutas siguiendo la siguiente estructura:
“categoría\año-mes\categoria-dia-mes-año.csv”
○ Por ejemplo: “museos\2021-noviembre\museos-03-11-2021”
○ Si el archivo existe debe reemplazarse. La fecha de la nomenclatura
es la fecha de descarga.
'''
# este modulo recibe un diccionario(url:'', categoria:'')
# ejemplo = dict(url='https://ejemplo.ar//museos.csv', categoria='museos')
def BajarRecurso(dict):
    response = requests.get(dict["url"])
    
    nameOfNewFile= nombrarArchivo(dict['categoria'])
    # crear ruta
    # nombrar archivo
    # guardar archivo en ruta indicada
    ruta = crearRuta(dict['categoria'])
    
    
    #os.chdir(ruta)
    ruta = ruta + nameOfNewFile
    with open(ruta, 'w', encoding='latin-1') as f:        
        f.write(response.text)
        f.close()
        print('***Bajada informacion en: ', nameOfNewFile)


def nombrarArchivo(categoria):
# categoría\año-mes\categoria-dia-mes-año.csv
    nombre = categoria+'-'+ahora.strftime("%d")+'-'+ahora.strftime("%m")+'-'+ahora.strftime("%Y")+'.csv'
    return nombre

def crearRuta(categoria):
    #python program to check if a path exists if it doesn’t exist we create one
    # tiene que  verse asi: categoría\año-mes\
    anioMes= ahora.strftime("%Y") + '-' + ahora.strftime("%B")    
    ruta = categoria+'\\'+anioMes+'\\'        
    #ver si esxiste carpeta categoria
    if not os.path.exists(categoria):
        os.makedirs(categoria)
        #ver si esxiste carpeta de esa categoria\anio-mes\
    if not os.path.exists(ruta):
        os.mkdir(ruta)
    return ruta
    