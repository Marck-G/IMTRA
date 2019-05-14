<div class="one-page">
<h1 class="book-title">IMTRA</h1>
<h2>Image Manager and TRansfer Application</h2>
<div class="footer">
<p class="date">fecha</p>
<p class="authors">Unai Díaz, Marck Carrión</p>
</div>
</div>

<div class="header">
<p class="name">IMTRA</p>
<p class="page">1</p>
</div>

# Índice
1. [Introducción](#intro)
2. [Overview](#over)
3. [Librerías](#lib)
4. [Módulo Image Transfer](#im_tr)
   1. Introducción
   2. Esquema del módulo
   3. Base de datos
5. [Módulo Image Manager](#im_ma)
   1. [Introducción](#im_ma_i)
   2. Esquema del módulo
   3. Base de datos
   4. AI y auto etiquetado
6. Módulo Search Engine
   1. Introducción
   2. Esquema del módulo
   3. Base de datos
   4. Funciones de busqueda
7. Módulo CL-API
   1. Introducción
   2. Esquema del módulo
8. Integración
   1. Esquema de módulos
9. GUI

# 1. Introducción {#intro}
**Image Manager and TRansfer Application (IMTRA)** es un programa orientado a aquellos usuario de Linux que sean apasionados de la fotografía. Está desarrollado principalmente en __python 3__ y cuenta con una interfaz atractiva al público desarrollada con __tecnologías web__.

IMTRA surge de la necesidad de programas para la organización y transferencia de fotos en el entorno linux, pues como siempre ocurre en la comunidad linux, existen programas funcionales pero carecen de una interfaz gráfica agradable. Casi todos tienen interfaces que no siguen los estandares de dise&ntilde;o de interfaces. IMTRA proporciona una interfaz minimaista y limpia para que el usario tenga lo que necesita siempre a mano.

Así mismo _IMTRA_ desde el punto de vista del desarrollo permite utilizar sus modulos de forma independiente, se trata de una aplicación totalmente modular. __No existe una dependencia directa entre los módulos__ es el controlador de la aplicación quien se encarga de interconectarlas.

# 2. Overview {#over}
La aplicación cuenta con tres módulos principales más el controlador y la interfaz gráfica. Los tre módulos principales son:
- _Image Transfer_
- _Search Engine_ 
- _Image Manger_
  
La comunicación entre los módulos principales se hace mediante el módulo __CL-API (Command Line Application Programming Interface)__.

![](overview_node_graph.png)

# 3. Librer&iacute;as {#lib}
En desarrollo de la aplicación se ha visto la necesidad de buscar librerías y APIs para facilitar y agilizar el desarrollo de la misma.
## 3.1 Interfaz 
Para la interfaz se ha usado una librería que permite la creación de un servidor local temporal y mediante el motor de _Google Chrome_ o de _Chromiun_ permite visualizar una interfaz hecha completamente en __HTML 5__ y __CSS3__. Se trata de la libreía __[eel](https://pypi.org/project/Eel/)__.

## 3.2 Inteligencia Artificial
Para el tema de la _inteligencia artificial_ se ha utilizado una API REST __para agilizar el procesado de imágenes y evitar la dependencia del hardware__. En concreto se ha usado  [Clarifai](https://clarifai.com/).
# 4. Módulo Image Transfer {#im_tr}


# 5. Módulo Image Manager {#im_ma}
## 5.1 Introducción {#im_ma_i}
La función principal del módulo es la organización de imágenes y la etiquetación de las mismas.
## 5.2 Esquema del módulo
Este consta de un etiquetador automático, una base de datos propia y un sistema de copias de seguridad.
![](img_mng.png)

#### 5.1 Etiquetador Automatico
Mediante una _API REST_ de inteligencia artificial se procesa la imagen y detecta los elementos que se encuentran en la imagen.
El funcionamiento es simple, la función  recibe una imagen que la lee de forma binaria y envía los bytes al servidor, este los procesa mediante inteligencia artificial, tomando como referencia un modelo preestablecido, y devuelve un archivo en __JSON__. La respuesta se procesa y se almacena en una base de datos embebida.
![](IA_img.png)

#### 5.2 Backup Tools
Permite crear copias de seguridad de las carpetas y las imágenes que se le pasas como argumento. Utiliza la compresión tar para comprimir todos las carpetas de la forma más efieciente.

## 5.3 Base de datos
El administrador de imágenes utiliza una tabla para relacionar la imágen con un id, esto se hace para no almacenarla directamente, se relaciona la dirección absoluta de la imágen con un id numérico. Esto nos resultará utili para trabajar de forma más abstracta con las imágenes y poder crear interrelaciones con los otros módulos.
![](img_tr.png)
La base de datos interrelaciona las etiquetas que se leen desde el servidor con la imagen correspondiente.