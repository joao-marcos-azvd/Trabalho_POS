from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship

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

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
    
    usu_id: Optional[int] = Field(default=None, primary_key=True)
    usu_nome: str = Field(max_length=100)
    usu_email: str = Field(max_length=100)
    usu_senha: str = Field(max_length=100)
    usu_tipo: str = Field(max_length=20)
