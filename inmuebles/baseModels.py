
from django.db import connection
'''
def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()
    return row
'''
# metodos genericos que permiten realizar consultas sql
class BaseModels:
    def executeQuery(self,sql,parametros=None):
        # Obtenemos un objeto cursor que nos entrega la coneccion
        cursor = connection.cursor()
        # with connection.cursor() as cursor:
        cursor.execute (sql, parametros if not None else [])
        
        print(cursor.description) #data que trenemos como respuesta.
        
        row = cursor.fetchone()
        return row
    
    def executeQuery(self,sql,parametros=None):
        #Obtenemos un objeto cursor que nos entrega la conexión.
        cursor = connection.cursor()
        #with connection.cursor() as cursor:
        cursor.execute(sql, parametros if parametros is not None else [])
        
        print(cursor.description)#data que tenemos como respuesta
        data = cursor.description # recorrer la data
        #retornar lista[dicc]

        row = cursor.fetchone()
        return row