import mysql.connector
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

# config = {
#     'user': 'admindb',
#     'password': 'admin',
#     'host': '0.tcp.us-cal-1.ngrok.io',
#     'database': 'sucursalMochis',
#     'port': '16567',
#     'raise_on_warnings': True
# }
config = {
    "user": "admindb",
    "password": "admin",
    "host": "192.168.1.106",
    "database": "sucursalMochis",
    "port": "3306",
    "raise_on_warnings": True,
}


def filtrado(params):
    try:
        conn = mysql.connector.connect(**config)
        query = f"CALL Filtrar(%s,%s,%s,%s,%s,%s);"

        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            query,
            (
                params["src"],
                params["dst"],
                params["d1"],
                params["d2"],
                params["status"],
                params["city"]
            ),
        )
        data = cursor.fetchall()

        cursor.close()
        conn.close()
        return data

    except mysql.connector.Error as err:
        print("Error de conexión a la base de datos:", err)


# connect_and_write_to_csv()
