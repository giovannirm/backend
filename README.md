# ADAPTACIÓN Y MODELAMIENTO CON FLASK Y MYSQL-API REST

### Crear entorno virtual

```console
    conda create -n proyecto_entrada python=3.11.0
```
### Instalar dependencias

```console
    pip install -r requirements.txt
```

### Modificar el archivo .env_copy por .env

Agregar sus credenciales user_db, password y name_db en el archivo .env

```bash
    SECRET_KEY="your-secret-key"
    FLASK_APP=main.py
    FLASK_DEBUG=1
    FLASK_ENV=FLASK_DEVELOPMENT

    # DATABASE INFORMATION FOR POSTGRESQL
    DATABASE=postgresql
    USER_DB=user_db
    PASSWORD=password
    SERVER=localhost
    PORT=5432
    NAME_DB=name_db

    # DATABASE INFORMATION FOR SQLITE
    DATABASE=sqlite
    USER_DB=
    PASSWORD=
    SERVER=
    PORT=
    NAME_DB=name_db

    # DATABASE INFORMATION FOR MYSQL
    DATABASE=mysql
    USER_DB=user_db
    PASSWORD=password
    SERVER=localhost
    PORT=
    NAME_DB=name_db

    # MAIL INFORMATION
    MAIL_USERNAME=correodegmail@gmail.com
    MAIL_PASSWORD=contraseñadeaplicacionesdegmail
```

El valor que contenga NAME_DB será la base de datos que deberán crear en su gestor de base de datos ya sea para MySQL o PostgreSQL

### Link de mi [Diagrama E-R](https://dbdiagram.io/d/641f6f635758ac5f17241ecf)

```console
    https://dbdiagram.io/d/641f6f635758ac5f17241ecf
```

### Correr las migraciones

```console
    flask db init
    flask db migrate -m "Iniciando base de datos"
    flask db upgrade
```

## 🚀 End points

### Endpoint para ver las empresas que existen
```console
    http://localhost:5000/companies/
```

### Para crear la imagen en Docker, ejecutar lo siguiente desde la raíz del proyecto

```console
    docker build -t proyecto .
```
### Para correr nuestra imagen en un contenedor de Docker, ejecutar lo siguiente desde la raíz del proyecto

```console
    docker run --name contenedor_proyecto -p 5000:5000 -d proyecto
```