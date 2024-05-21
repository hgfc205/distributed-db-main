import pymysql
import csv

# TODO: CAMBIAR DATOS DE ACCESO A LA DB en CENTOS

"""
# evie mamadisima
# Script para instalar la API cagada
yum install git
git clone https://github.com/eviecamila/distributed-db.git
cd API
pip install -r requirements.txt
py main.py
"""

# Configuración de la base de datos con mysql.connector
# config = {
#     'user': 'admindb',
#     'password': 'admin',
#     'host': '0.tcp.us-cal-1.ngrok.io',
#     'database': 'sucursalMochis',
#     'port': '16567',
#     'raise_on_warnings': True
# }

# Configuración de la base de datos con pymysql
config = {
    "user": "admindb",
    "password": "admin",
    "host": "192.168.1.106",
    "database": "sucursalMochis",
    "port": 3306,  # pymysql espera un entero, no una cadena
}


def filtrado(params):
    try:
        # Conectar a la base de datos
        conn = pymysql.connect(
            user=config["user"],
            password=config["password"],
            host=config["host"],
            database=config["database"],
            port=config["port"],
            cursorclass=pymysql.cursors.DictCursor,
        )
        query = "CALL Filtrar(%s, %s, %s, %s, %s, %s);"

        with conn.cursor() as cursor:
            # Ejecutar la consulta
            cursor.execute(
                query,
                (
                    params["src"],
                    params["dst"],
                    params["d1"],
                    params["d2"],
                    params["status"],
                    params["city"],
                ),
            )
            # Obtener los datos
            data = cursor.fetchall()

        conn.close()
        return data

    except pymysql.MySQLError as err:
        print("Error de conexión a la base de datos:", err)


# Ejemplo de llamada a la función con parámetros
# params = {
#     "src": "source_value",
#     "dst": "destination_value",
#     "d1": "2022-01-01",
#     "d2": "2022-12-31",
#     "status": "status_value",
#     "city": "city_value",
# }
# data = filtrado(params)
# print(data)
