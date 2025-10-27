from pydantic  import BaseModel 

class Cliente(BaseModel):
	nombre: str
	
class Pedido(BaseModel):
	producto_id: int
	cliente_id: int
	
class Producto(BaseModel):
	nombre: str 
	precio: int
	