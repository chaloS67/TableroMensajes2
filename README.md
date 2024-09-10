## instalacio 
    1- clona el repositorio
        git clone <https://github.com/chaloS67/TableroMensajes2.git>

    2- Crea y activa un entorno virtual
        python -m venv env
        source env/bin/activate  
        # En Windows: env\Scripts\activate

    3- Instala las dependencias
        pip install -r requirements.txt


    4- Realiza las migraciones de la base de datos:
        python manage.py migrate

    5- Ejecuta el servidor
        python manage.py runserver

    6- Abre tu navegador y navega http://localhost:8000 o al puerto que le asignes

    