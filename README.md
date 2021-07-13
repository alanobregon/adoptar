# README #

## Autor
- Obregón Alan

## Prerequisitos
- git
- Python 3.8+ con pip
- venv or virtualenv
- Microsoft SQL Server
- Microsoft ODBC 13+ for SQL Server

## Guia de insalación rapida
```
# Crear un entorno virtual
python -m venv virtual_env_name

# Activar entorno
# Windows 
.\virtual_env_name\Scripts\activate

# Linux
source virtual_env_name/bin/activate

# Clonar el repositorio
git clone https://github.com/Alan49/adoptar.git
cd adoptar/

# Instalar los paquetes
pip install wheel
pip install -r requirements.txt
```

## Configuración


Crear un archivo `local.py` en la carpeta `settings` con las siguientes lineas decodigo.

> Para que el reinicio de contraseña funcione, en Google, necesitas tener desactivada la autenticación de dos pasos y tener [activado el acceso de aplicaciones menos seguras](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4M3V8HExiUumtms7Cfsw4jeZxg4DvMB0xssDTy52YItQz1AKhcNDPW4vq99npAk7-iFUcOaitWNHyKyZm8NYbbGIgCGNA)

> Si quieres, puedes ocupar la base de datos SQLite que viene por defecto. Continua con las [Migraciones](#migraciones)

```
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'YOUR_DATABASE_NAME',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_PASSWORD',
        'HOST': 'HOST', # 127.0.0.1
        'PORT': 'PORT', # 1433

        'OPTIONS': {
            'driver': 'DRIVER', # ODBC Driver 13/17 for SQL Server
        },
    },
}

EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

## Migraciones
Ejecutar las migraciones.
```
python manage.py migrate

```


# Importante
## Seeds
Ejecutar las siguientes seeds para cargar datos.
```
python manage.py loaddata provinces.json
python manage.py loaddata cities.json
python manage.py loaddata reasons.json
python manage.py loaddata post_status.json
python manage.py loaddata postulation_status.json
python manage.py loaddata categories.json

```

Crear un usuario administrador (Opcional)
```
python manage.py createsuperuser
```

Ejecutar el servidor
```
python manage.py runserver
```
