# hendylaCasasScrapper :maple_leaf:

Proyecto realizado en 2019 donde se estira datos de las casas en oferta en hendyla, y se agrega en un mapa con la info basica de la publicacion

## Descipcion :page_facing_up:

Modificacion de un proyecto que habia realizado para un curso avanzado de web scrapping con web development, la idea basicamente es escrapear la pagina de hendyla, informacion de las casas ofertadas, y ubicacion de estas en el mapa.

## In process :hammer:

- Detalles de cada publicacion(mas de lo detallado que tiene cada pop-up)
- filtro por rango de precio
- interfaz mas linda
- Jugar con hilos para que al scrapear muestre en la interfaz algun mensaje de carga en segundo plano

# Como correr el proyecto :computer:

<p>1. Clonar la repo</p>

```bash
git clone https://github.com/WilliBobadilla/hendylaCasasScrapper.git
```

<p>2. Moverte al directorio de la repo</p>

```bash
cd  hendylaCasasScrapper
```

<p>3. Crear el virtualenv</p>

```bash
virtualenv env
```

o si no funciona lo anterior

```bash
python -m virtualenv env
```

<p>4. Activar el virtual env</p> 
** Para linux

```bash
source env/bin/activate
```

\*\*\* En el caso de no contar con virtualenv

```bash
pip install virtualenv
```

\*\* Para windows

```bash
cd env
cd Scripts
activate.bat
cd ..
cd ..
```

Estos ultimos dos cd .. llevan de nuevo a la raiz del proyecto, en el caso de que esten usando windows hacer esto.

<p>5. Instalar dependencias</p>

```bash
pip install -r requirements.txt
```

<p>6. Correr el proyecto </p>

```bash
python app.py
```
