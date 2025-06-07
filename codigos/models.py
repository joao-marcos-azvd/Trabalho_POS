from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'tb_categorias'
    
    cat_id = Column(Integer, primary_key=True, autoincrement=True)
    cat_nome = Column(String(255), nullable=False, unique=True)
    
    produtos = relationship("Produto", back_populates="categoria")


class Fornecedor(Base):
    __tablename__ = 'tb_fornecedores'
    
    for_id = Column(Integer, primary_key=True, autoincrement=True)
    for_nome = Column(String(255), nullable=False)
    for_telefone = Column(String(255), nullable=False)
    for_email = Column(String(255), nullable=False)
    
    produtos = relationship("Produto", back_populates="fornecedor")


class Produto(Base):
    __tablename__ = 'tb_produtos'
    
    pro_id = Column(Integer, primary_key=True, autoincrement=True)
    pro_nome = Column(String(255), nullable=False)
    pro_descricao = Column(String(255), nullable=False)
    pro_quantidade = Column(Integer, nullable=False)
    pro_unidade = Column(String(255), nullable=False)
    pro_cat_id = Column(Integer, ForeignKey('tb_categorias.cat_id'))
    pro_for_id = Column(Integer, ForeignKey('tb_fornecedores.for_id'))
    
    categoria = relationship("Categoria", back_populates="produtos")
    fornecedor = relationship("Fornecedor", back_populates="produtos")


class Usuario(Base):
    __tablename__ = 'tb_usuarios'
    
    usu_id = Column(Integer, primary_key=True, autoincrement=True)
    usu_nome = Column(String(255), nullable=False)
    usu_email = Column(String(255), nullable=False)
    usu_senha = Column(String(255), nullable=False)
    usu_tipo = Column(String(255), nullable=False)
