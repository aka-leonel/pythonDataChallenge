# aqui rompere cosas
import archivosFuente

museoDict = dict(url='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv', categoria='museos')
bibliotecaDict = dict(url='https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/11_bibliotecapopular-datos-abiertos.csv', categoria='bibliotecas')

if __name__ == '__main__':

# 1 Obtener los archivos fuente
    archivosFuente.BajarRecurso(museoDict)
    archivosFuente.BajarRecurso(bibliotecaDict)

# 2 transformar

# 3 cargar