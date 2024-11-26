import folium
from tkinter import *
from tkhtmlview import HTMLLabel
import re
import webbrowser

def normalizar_coordenadas(coord_arr):
    coordenadas_normalizadas = []
    try:
        coord_arr = [
            re.sub(r"[^0-9.\-]", "", c.split()[0]) 
            for c in coord_arr
        ]
        coord_arr = [float(c) for c in coord_arr]
        
        if -90 <= coord_arr[0] <= 90 and -180 <= coord_arr[1] <= 180:
            coordenadas_normalizadas.append(coord_arr)
    except (ValueError, IndexError):
        pass
    
    return coordenadas_normalizadas

def mapa(coordenadas):
    coordenadasArr = []
    for row in coordenadas.namedtuples():
        lat  = row.lat
        lng = row.lng
        nombre = row.nombre
        descripcion = row.descripcion
        latFixed =   str(lat).replace(',' , '.')
        lngFixed =   str(lng).replace(',' , '.')
        arrayCoordenadsFixed = normalizar_coordenadas([latFixed, lngFixed])
        if len(arrayCoordenadsFixed) > 0:
            o = {
                "coordenadas": normalizar_coordenadas([latFixed, lngFixed]),
                "nombre": nombre,
                "descripcion": descripcion
            }
            coordenadasArr.append(o)
    mapaObras = folium.Map(location=[-34.603722, -58.381592], zoom_start=13)

    
    for coord in coordenadasArr:
        folium.Marker(location=coord['coordenadas'][0],
                      popup=f"<b>{coord['nombre']}</b><br>{coord['descripcion']}",
                      tooltip=coord["nombre"]).add_to(mapaObras)

    
    mapaObras.save("markerian-coscarelli-mele-vanotti-joyce/data/mapaObras.html")
    webbrowser.open("markerian-coscarelli-mele-vanotti-joyce/data/mapaObras.html")
