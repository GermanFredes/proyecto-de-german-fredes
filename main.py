from fastapi import FastAPI , Depends
from modelos import Cliente , Pedido , Producto 
from manager import Manager , getCursor
import psycopg

app = FastAPI()

manager = Manager()

@app.post("/agregar_cliente")
def agregar_cliente(cliente: Cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.postcliente(cliente, cursor)
    return {"msg" : res}

@app.get("/ver_cliente")
def ver_cliente(cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getcliente(cursor)
    return res


@app.get("/ver_cliente/{cliente_id}")
def getclienteporid(cliente_id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getcliente_by_id(id, cursor)
    return res


@app.put("/actualizar_cliente/{cliente_id}")
def actualizarCliente(id: int, actualizarCliente: Cliente, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.actualizarcliente(id , actualizarCliente, cursor )
    return {"msg": res}


@app.delete("/eliminar_cliente/{cliente_id}")
def eliminarcliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.eliminarcliente(id, cursor)
    return {"msg": res}


@app.post("/agregar_producto")
def agregar_producto(producto:Producto, cursor : psycopg.Cursor = Depends(getCursor)):
    res= manager.postproducto(producto, cursor)
    return {"msg": res}

	
@app.get("/ver_productos")
def ver_productos(cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getproducto(cursor)
    return res

    
@app.post("/agregar_pedido")
def agregar_pedido(pedido: Pedido, cursor: psycopg.Cursor = Depends(getCursor)):
    res=manager.postpedido(pedido, cursor)
    return {"msg": res}

  
@app.get("/ver_pedido")
def ver_pedido(cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getpedido(cursor)
    return res

@app.get("/ver_pedido/{pedido_id}")
def ver_pedido_by_id(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getpedido_by_id(id,cursor)
    return res
 
@app.get("/pedido/cliente/{id}")
def pedidos_por_cliente(id: int, cursor: psycopg.Cursor = Depends(getCursor)):
    res = manager.getpedido_by_cliente(id,cursor)
    return res




    
    
    
