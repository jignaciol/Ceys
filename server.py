#!/user/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'jignaciol'

import bottle
import psycopg2
import json
import datetime
from constants import BDP_IP, BDP_PORT, BDP_DBNAME, BDP_USER, BDP_PASSWORD
from constants import BTL_HOST, BTL_PORT

DSN = "host='{0}' port={1} dbname='{2}' user='{3}' password='{4}'"
DSN = DSN.format(BDP_IP, BDP_PORT, BDP_DBNAME, BDP_USER, BDP_PASSWORD)

SERVER = bottle.app()


def post_get(name):
    """Funcion que devuelve el valor de una variable enviada por POST """
    return bottle.request.forms.get(name)


def json_get(name):
    """Funcion para capturar valores enviados por json"""
    data = bottle.request.json
    return data[name]


def json_result():
    return bottle.request.json


@bottle.route("/fotos/<filename:path>")
def static_images(filename):
    """ Funcion que busca las imagenes de los empleados """
    response = {"OK": False, "msg": ""}
    try:
        img = bottle.static_file(filename, root="../Fotos")
        return img
    except Exception:
        return response


@bottle.route("/api/template/<filename:path>")
def static_template(filename):
    """ Funcion que busca y devuelve el archivo template solicitado """
    return bottle.static_file(filename, root="public/template/")


@bottle.route("/public/<filename:path>")
def static(filename):
    """ Funcion que devuelve los archivos estaticos """
    return bottle.static_file(filename, root="public/")


# punto de inicio de la app #
@bottle.route("/", method="GET")
def index():
    """ Funcion que devuelve solo el index del directorio """
    return bottle.static_file("index.html", root="public/")


# funciones API RESTFULL #

@bottle.route("/api/persona", method="GET")
def lista_empleados():
    """ Funcion que lista todos los empleados """
    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = """
                SELECT  p.id,
                        p.voe,
                        p.cedula,
                        p.nombre,
                        p.apellido,
                        p.bl
                FROM persona p
                ORDER BY p.nombre;
              """
        cur.execute(sql)
        records = cur.fetchall()
        cur.close()
    except psycopg2.Error as error:
        print 'ERROR: no se pudo realizar la conexion: ', error

    cabecera = [col[0] for col in cur.description]
    json_result = json.dumps([dict(zip(cabecera, rec)) for rec in records])

    return json_result


@bottle.route("/api/persona/:id", method="GET")
def listar_empleado_id(id=0):
    """ funcion que lista una persona """
    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = """
                SELECT  p.id,
                        p.voe,
                        p.cedula,
                        p.nombre,
                        p.apellido,
                        p.bl
                FROM persona p
                WHERE p.id={0}
                ORDER BY p.nombre;
              """.format(id)

        cur.execute(sql)
        records = cur.fetchall()
        cur.close()
    except psycopg2.Error as error:
        print 'ERROR: no se pudo realizar la conexion: ', error

    cabecera = [col[0] for col in cur.description]
    json_result = json.dumps([dict(zip(cabecera, rec)) for rec in records])

    return json_result


@bottle.route("/api/persona/:cedula", method="GET")
def listar_empleado_cedula(cedula=0):
    """ funcion que lista una persona """
    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = """
                SELECT  p.id,
                        p.voe,
                        p.cedula,
                        p.nombre,
                        p.apellido,
                        p.bl
                FROM persona p
                WHERE p.cedula='{0}'
                ORDER BY p.nombre;
              """.format(cedula)

        cur.execute(sql)
        records = cur.fetchall()
        cur.close()
    except psycopg2.Error as error:
        print 'ERROR: no se pudo realizar la conexion: ', error

    cabecera = [col[0] for col in cur.description]
    json_result = json.dumps([dict(zip(cabecera, rec)) for rec in records])

    return json_result


@bottle.route("/api/persona", method="POST")
def agregar_empleado():
    """ funcion para agregar un empleado a la base de datos """
    response = {"OK": False, "msg": "", "id": 0}
    try:
        data = json_result()
    except ValueError:
        print "error capturando json"

    voe = data["voe"]
    cedula = data["cedula"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    bl = data["bl"]

    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql_next_val = """ SELECT nextval(pg_get_serial_sequence('persona', 'id_persona')) as new_id; """

        cur.execute(sql_next_val)
        records = cur.fetchall()
        new_id = records[0][0]
        sql = """ INSERT INTO persona(id, voe, cedula, nombre, apellido, bl)
                     VALUES ( {0}, '{1}', '{2}', '{3}', '{4}', '{5}');
              """.format(new_id, voe, cedula, nombre, apellido, bl)

        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        response['OK'] = True
        response['id'] = new_id
    except psycopg2.Error as error:
        response['OK'] = False
        response['msg'] = 'error al insertar el registro a la base de datos'
        print 'ERROR: no se pudo insertar el registo ', error

    return response


@bottle.route("/api/persona/:id", method="PUT")
def actualizar_empleado(id=0):
    """ funcion para actualizar los datos de una persona """
    response = {"OK": False, "msg": ""}
    try:
        data = json_result()
    except ValueError:
        print "error capturando json"

    voe = data["voe"]
    cedula = data["cedula"]
    nombre = data["nombre"]
    apellido = data["apellido"]
    bl = data["bl"]

    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = """ UPDATE persona
                  SET voe={0},
                      cedula={1},
                      nombre={2},
                      apellido={3},
                      bl={4}
                  WHERE id = {5};""".format(voe, cedula, nombre, apellido, bl, id)

        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

        response["OK"] = True
    except psycopg2.Error as error:
        response["OK"] = False
        response["msg"] = 'error al intentar actualizar el registro en la base de datos'
        print 'ERROR: no se pudo actualizar el registo ', error

    return response


@bottle.route("/api/persona/:id", method="DELETE")
def borrar_empleado(id=0):
    """ funcion para borrar una persona en la base de datos """
    response = {"OK": False, "msg": ""}
    id = json_result()
    try:
        conn = psycopg2.connect(DSN)
        cur = conn.cursor()

        sql = """ DELETE FROM "persona" WHERE id = {0} """.format(id)
        cur.execute(sql)
        conn.commit()

        cur.close()
        conn.close()

        response["OK"] = True
    except psycopg2.Error as error:
        response["OK"] = False
        response["msg"] = "error al intentar borrar el registro en la base de datos"
        print "ERROR: no se pudo borrar el registo -->", error

    return response


# punto de inicio del servidor #


def main():
    """ funcion principal """
    bottle.debug(True)
    bottle.run(SERVER, host=BTL_HOST, port=BTL_PORT, reloader=True)

if __name__ == "__main__":
    main()
