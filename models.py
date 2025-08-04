from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from pydantic import EmailStr


class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    usu_id: Optional[int] = Field(default=None, primary_key=True)
    usu_nome: str = Field(max_length=100)
    usu_email: EmailStr = Field(max_length=100, index=True)
    usu_senha: str = Field(max_length=200)
    usu_tipo: str = Field(max_length=20)


class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    cat_id: Optional[int] = Field(default=None, primary_key=True)
    cat_nome: str = Field(max_length=100)
    produtos: List["Produto"] = Relationship(back_populates="categoria")

class Fornecedor(SQLModel, table=True):
    __tablename__ = "fornecedor"
    for_id: Optional[int] = Field(default=None, primary_key=True)
    for_nome: str = Field(max_length=100)
    for_telefone: str = Field(max_length=20)
    for_email: str = Field(max_length=100)
    produtos: List["Produto"] = Relationship(back_populates="fornecedor")

class Produto(SQLModel, table=True):
    __tablename__ = "produto"
    pro_id: Optional[int] = Field(default=None, primary_key=True)
    pro_nome: str = Field(max_length=100)
    pro_descricao: str
    pro_quantidade: int
    pro_unidade: str = Field(max_length=10)
    pro_cat_id: int = Field(foreign_key="categoria.cat_id")
    pro_for_id: int = Field(foreign_key="fornecedor.for_id")
    categoria: Optional[Categoria] = Relationship(back_populates="produtos")
    fornecedor: Optional[Fornecedor] = Relationship(back_populates="produtos")

# --- Schemas Pydantic ---
class UsuarioCreate(SQLModel):
    usu_nome: str
    usu_email: EmailStr
    usu_senha: str
    usu_tipo: str

class UsuarioRead(SQLModel):
    usu_id: int
    usu_nome: str
    usu_email: EmailStr
    usu_tipo: str

class UsuarioUpdate(SQLModel):
    usu_nome: Optional[str] = None
    usu_email: Optional[EmailStr] = None
    usu_senha: Optional[str] = None
    usu_tipo: Optional[str] = None

class CategoriaCreate(SQLModel):
    cat_nome: str

class CategoriaRead(SQLModel):
    cat_id: int
    cat_nome: str

class CategoriaUpdate(SQLModel):
    cat_nome: Optional[str] = None

class FornecedorCreate(SQLModel):
    for_nome: str
    for_telefone: str
    for_email: str

class FornecedorRead(SQLModel):
    for_id: int
    for_nome: str
    for_telefone: str
    for_email: str

class FornecedorUpdate(SQLModel):
    for_nome: Optional[str] = None
    for_telefone: Optional[str] = None
    for_email: Optional[str] = None

class ProdutoCreate(SQLModel):
    pro_nome: str
    pro_descricao: str
    pro_quantidade: int
    pro_unidade: str
    pro_cat_id: int
    pro_for_id: int

class ProdutoRead(SQLModel):
    pro_id: int
    pro_nome: str
    pro_descricao: str
    pro_quantidade: int
    pro_unidade: str
    pro_cat_id: int
    pro_for_id: int

class ProdutoUpdate(SQLModel):
    pro_nome: Optional[str] = None
    pro_descricao: Optional[str] = None
    pro_quantidade: Optional[int] = None
    pro_unidade: Optional[str] = None
    pro_cat_id: Optional[int] = None
    pro_for_id: Optional[int] = None