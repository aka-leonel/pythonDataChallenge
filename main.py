import archivosFuente

# Url que seran fuente de los datos
museoDict = dict(url='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv', categoria='museos')
bibliotecaDict = dict(url='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/11_bibliotecapopular-datos-abiertos.csv', categoria='bibliotecas')

# Nota: son 3 los recursos a obtener: museos, bibliotecas y cines.
# Se quita el recurso cines por arrojar error 404 
# cinesDict = dict(url='https://datos.gob.ar/dataset/cultura-mapa-cultural-espacios-culturales/archivo/cultura_392ce1a8-ef11-4776-b280-6f1c7fae16ae', categoria='cines')

if __name__ == '__main__':

# 1 Obtener los archivos fuente ------
    archivosFuente.BajarRecurso(museoDict)
    archivosFuente.BajarRecurso(bibliotecaDict)
    # sacado por Error 404
    # archivosFuente.BajarRecurso(cinesDict)

# 2 transformar     ------------------

# 3 cargar          ------------------