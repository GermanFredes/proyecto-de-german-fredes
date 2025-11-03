import os
from typing import Generator
import psycopg
from dotenv import load_dotenv
from modelos import Cliente, Pedido, Producto

load_dotenv("bd.env")
passwordDB = os.getenv("PASSWORD")

url = f"postgresql://postgres:{passwordDB}@ijhzxqejmtfltbcivuro.supabase.co:5432/postgres"

def getCursor() -> Generator[psycopg.Cursor, None, None]:
    conn = psycopg.connect(url, sslmode="require")

    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    finally:
        cursor.close()
        conn.close()

class Manager:
#   def __init__(self):
      

#    self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS cliente(
#              cliente_id INTEGER PRIMARY KEY,
#              nombre TEXT)""") 
             
#    self.cursor.execute(""" 
#         CREATE TABLE IF NOT EXISTS
#              producto(
#              producto_id INTEGER PRIMARY KEY,
#              nombre TEXT,
#              precio INTEGER )""" 
# )
#    self.cursor.execute("""
#         CREATE TABLE IF NOT EXISTS pedido(
#                    pedido_id INTEGER PRIMARY KEY,
#                    producto_id INTEGER,
#                    cliente_id INTEGER,
#                    FOREIGN KEY (producto_id)    REFERENCES producto(producto_id),
#                    FOREIGN KEY (cliente_id) REFERENCES 
#                    cliente (cliente_id)
# )""")
#   self.conn.commit()


  def postcliente(self,cliente:Cliente, cursor: psycopg.Cursor ):
      cursor.execute(
  "INSERT INTO cliente (nombre) VALUES (%s)", (cliente.nombre,))
      return "cliente agregado"
   
    
  def getcliente(self , cursor : psycopg.Cursor) -> list:
      res = cursor.execute(
  "SELECT cliente_id, nombre FROM cliente").fetchall() 
      return [{"id": row[0], "nombre" : row[1]} for row in res ]
   
  def getcliente_by_id(self, id: int, cursor: psycopg.Cursor):
      res = cursor.execute(
  "SELECT cliente_id, nombre FROM cliente WHERE cliente_id = %s",
        (id,)
    ).fetchall()
      return [{"id": row [0], "nombre": row [1]} for row in res]
  
  def actualizarcliente(self, id: int, actualizarcliente: Cliente, cursor: psycopg.Cursor) -> str :
      cursor.execute(
  "UPDATE cliente SET nombre = %s WHERE cliente_id = %s",
        (actualizarcliente.nombre, id),
      )
      return "cliente actualizado"
  
  def eliminarcliente (self , id:int, cursor: psycopg.Cursor) -> str:
      cursor.execute(
  "DELETE FROM cliente WHERE cliente_id = %s",
    (id,))
      return "cliente eliminado"
    
  def postproducto(self, producto:Producto, cursor: psycopg.Cursor):
      cursor.execute(
  "INSERT INTO producto (nombre, precio) VALUES (%s,%s) ",(producto.nombre,producto.precio))
      return "producto agregado"
     
  def getproducto(self, cursor: psycopg.Cursor):
      res = cursor.execute(
   "SELECT * FROM producto").fetchall()
      return [{"producto_id": row[0], "nombre" : row[1],
   "precio" : row[2]} for row in res]	
    
  def postpedido(self , pedido : Pedido , cursor: psycopg.Cursor):
      cursor.execute(
  "INSERT INTO pedido(producto_id, cliente_id) VALUES (%s,%s)",
   (pedido.producto_id, pedido.cliente_id))
      return "Pedido agregado"
   
  def getpedido(self , cursor: psycopg.Cursor) -> list :
     res = cursor.execute(
  "SELECT producto.nombre,producto.precio,cliente.nombre FROM pedido INNER JOIN cliente ON pedido.cliente_id = cliente.cliente_id INNER JOIN producto ON pedido.producto_id = producto.producto_id"
         ).fetchall()
     return [{"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res]
 
  def getpedido_by_id(self, id: int, cursor: psycopg.Cursor) -> list:
        res = cursor.execute(
            """
            SELECT producto.nombre, producto.precio, cliente.nombre
            FROM pedido
            INNER JOIN cliente ON pedido.cliente_id = cliente.cliente_id
            INNER JOIN producto ON pedido.producto_id = producto.producto_id
            WHERE pedido.cliente_id = %s
            """,
            (id,),
        ).fetchall()
        return [{"producto": row[0], "precio": row[1], "cliente": row[2]} for row in res]
   
   
  def getpedido_by_cliente(self, id : int, cursor : psycopg.Cursor) -> list:
      res = cursor.execute ("""
        SELECT producto.nombre ,  producto.precio, cliente.nombre
        FROM pedido
        INNER JOIN cliente ON pedido.cliente_id = cliente.cliente_id
        INNER JOIN producto ON pedido.producto_id = producto.producto_id
        WHERE cliente.cliente_id = %s""", (id,)).fetchall()
      return [{"producto": row[0], "precio": row[1], "cliente":row[2]} for row in res]
        
  
