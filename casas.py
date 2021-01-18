import requests
from bs4 import BeautifulSoup
def separador(arg):
    contador = 0
    for x in arg:
        contador+=1 #recorre hasta que encuentra la coma y alli separa
        if x ==",":
            index_coma = contador
            break
    r1 = arg[0:index_coma]
    r2 = arg[index_coma:]
    return r1,r2 
#para una sola casa       
def casas():
    """
    Funcion que extrae los datos de las casas de hendyla
    y retorna estos datos en un diccionario
    """
    page = requests.get("https://casas.hendyla.com/") #pagina a scraper
    soup = BeautifulSoup(page.content,"html.parser")
    casas = soup.find_all("article", class_ ="product-item clasificado") #lista casas
    lista_datos = [] #el diccionario con todos los datos
    for indice in range(len(casas)): #recorriendo
        try:
            primera_casa = casas[indice] 
            primer_precio = primera_casa.find_all("div", class_ ="precio left")[0].p.get_text() #se saca los datos del string que no interesan
            primer_precioMod = primer_precio[primer_precio.find("Gs.")+4:] #para borrar el espacio y el Gs.
            if primer_precioMod.find("nta") == -1:
                primer_precio = "Gs."+primer_precioMod
                print("Gs.",primer_precioMod) #si esta en guaranies
            else:
                primer_precioMod = primer_precio[primer_precio.find("$")+2:]
                primer_precio = "$"+primer_precioMod #si esta en uss
                print("$",primer_precioMod)

            descripcion = primera_casa.select("div.desc a")[0].get_text() #selecciona todas las "a" que tengan la clase desc dentro del div
            #print(descripcion)
            #print(len(descripcion))
            url_publicacion = primera_casa.select("div.desc a")[0].get("href") #se saca el url de la publicacion
            imagen = primera_casa.select("figure.img img")[0].get("src") #url imagen
            #print(url_publicacion) #esta es la url de la pagina
            #sacar la latitud y longitud
            pagina2 = requests.get(url_publicacion) #se "entra" a la ulr de la publicacion para scrapear datos que no se tienen en la pag inicial
            soup2= BeautifulSoup(pagina2.content, "html.parser")
            coord = soup2.find_all("div", id="map") #se saca coordenadas 
            coord = coord[0].find("iframe").get("src") #del link
            index_primero = coord.find("=") #se halla de donde a donde se va a recortar el string
            index_final = coord.find("&")
            coord= coord[index_primero+1:index_final-1]
            #print(coord)
            latitud,longitud = separador(coord) #se separa la latitud y la longitud
            datos = { #el diccionario a usar
                "precio" : primer_precio,
                "precionum" : primer_precioMod,
                "descripcion": descripcion,
                "ubicacion": {
                    "latitud": latitud,
                    "longitud": longitud
                },
                "img":imagen
            }
            lista_datos.append(datos) #se agrega a la lista de datos
            #print("-------------------------------------------") 
        except IndexError:
            #print("No ofrece coordenadas satelitales") #cuando no se dio la ubicacion en maps
            #print("----------------------------------------")
            continue 

    #print("Cantidad recolectada: ",len(lista_datos))    
    return lista_datos #cuando se llama a la funcion retorna la lista                
       

