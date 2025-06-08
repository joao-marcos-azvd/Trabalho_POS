from pydantic import BaseModel

class CategoriaCreate(BaseModel):
    cat_nome: str

class FornecedorCreate(BaseModel):
    for_nome: str
    for_telefone: str
    for_email: str

class ProdutoCreate(BaseModel):
    pro_nome: str
    pro_descricao: str
    pro_quantidade: int
    pro_unidade: str
    pro_cat_id: int
    pro_for_id: int

class UsuarioCreate(BaseModel):
    usu_nome: str
    usu_email: str
    usu_senha: str
    usu_tipo: str
