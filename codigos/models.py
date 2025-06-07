from typing import List, Optional
from pydantic import BaseModel

class Categoria(BaseModel):
    cat_id: int
    cat_nome: str

class Fornecedor(BaseModel):
    for_id: int
    for_nome: str
    for_telefone: str
    for_email: str

class Produto(BaseModel):
    pro_id: int
    pro_nome: str
    pro_descricao: str
    pro_quantidade: int
    pro_unidade: str
    pro_cat_id: int
    pro_for_id: int


class Usuario(BaseModel):
    usu_id: int
    usu_nome: str
    usu_email: str
    usu_senha: str
    usu_tipo: str

