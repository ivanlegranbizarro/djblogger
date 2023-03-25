# DJBlogger

DJBlogger es un proyecto realizado en Python, Django, Bootstrap 5 y HTMX con el fin de explorar las posibilidades de esta última tecnología.

## Descripción

Este proyecto es un blog simple en el que los usuarios pueden crear, ver, actualizar y eliminar publicaciones. Además, los usuarios también pueden crear y actualizar sus perfiles de usuario. El diseño se realiza utilizando el framework Bootstrap 5 y se utiliza HTMX para crear una experiencia de usuario más fluida y sin interrupciones.

## Funcionalidades

-   Creación, visualización, actualización y eliminación de publicaciones
-   Creación y actualización de perfiles de usuario
-   Diseño moderno y responsivo con Bootstrap 5
-   Interacción fluida con HTMX

## Instalación

Para instalar el proyecto, sigue estos pasos:

1.  Clona el repositorio: `git clone https://github.com/ivanlegranbizarro/djblogger.git`
2.  Accede al directorio del proyecto: `cd djblogger`
3.  Crea un entorno virtual: `python -m venv venv`
4.  Activa el entorno virtual: `source venv/bin/activate` (en Windows: `venv\Scripts\activate`)
5.  Instala las dependencias: `pip install -r requirements.txt`
6.  Crea la base de datos: `python manage.py migrate`
7.  Crea un superusuario: `python manage.py createsuperuser`
8.  Inicia el servidor: `python manage.py runserver`
9.  Abre un navegador web y accede a `http://localhost:8000`

## Inspiración

Este proyecto se basa en un curso de de Django y HTMX que puedes consultar aquí:

[djblogger con HTMX](https://www.udemy.com/course/django-project-djblogger/)

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
