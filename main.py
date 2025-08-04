from fastapi import FastAPI, Depends, HTTPException, status
from sqlmodel import SQLModel, select
from sqlalchemy.exc import IntegrityError
from database import engine, get_session
from sqlmodel import Session
from passlib.hash import bcrypt

import models
from models import (
    Usuario, UsuarioCreate, UsuarioRead, UsuarioUpdate,
    Categoria, CategoriaCreate, CategoriaRead, CategoriaUpdate,
    Fornecedor, FornecedorCreate, FornecedorRead, FornecedorUpdate,
    Produto, ProdutoCreate, ProdutoRead, ProdutoUpdate
)

app = FastAPI()

# Cria todas as tabelas
SQLModel.metadata.create_all(engine)

# --- Usuários ---
@app.post(
    "/usuarios/", response_model=UsuarioRead,
    status_code=status.HTTP_201_CREATED
)
def criar_usuario(
    dados: UsuarioCreate,
    session: Session = Depends(get_session)
):
    hashed = bcrypt.hash(dados.usu_senha)
    usuario = Usuario(
        usu_nome=dados.usu_nome,
        usu_email=dados.usu_email,
        usu_senha=hashed,
        usu_tipo=dados.usu_tipo
    )
    session.add(usuario)
    try:
        session.commit()
        session.refresh(usuario)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado"
        )
    return usuario

@app.get(
    "/usuarios/", response_model=list[UsuarioRead]
)
def listar_usuarios(
    session: Session = Depends(get_session)
):
    return session.exec(select(Usuario)).all()

@app.put(
    "/usuarios/{usu_id}", response_model=UsuarioRead
)
def atualizar_usuario(
    usu_id: int,
    dados: UsuarioUpdate,
    session: Session = Depends(get_session)
):
    usuario = session.get(Usuario, usu_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    update_data = dados.dict(exclude_unset=True, exclude={"usu_id"})
    if "usu_senha" in update_data:
        update_data["usu_senha"] = bcrypt.hash(update_data["usu_senha"])
    for key, value in update_data.items():
        setattr(usuario, key, value)
    try:
        session.commit()
        session.refresh(usuario)
    except IntegrityError:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="E-mail já cadastrado"
        )
    return usuario

@app.delete(
    "/usuarios/{usu_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_usuario(
    usu_id: int,
    session: Session = Depends(get_session)
):
    usuario = session.get(Usuario, usu_id)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado"
        )
    session.delete(usuario)
    session.commit()
    return

# --- Categorias ---
@app.post(
    "/categorias/", response_model=CategoriaRead,
    status_code=status.HTTP_201_CREATED
)
def criar_categoria(
    dados: CategoriaCreate,
    session: Session = Depends(get_session)
):
    categoria = Categoria(cat_nome=dados.cat_nome)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria

@app.get(
    "/categorias/", response_model=list[CategoriaRead]
)
def listar_categorias(
    session: Session = Depends(get_session)
):
    return session.exec(select(Categoria)).all()

@app.put(
    "/categorias/{cat_id}", response_model=CategoriaRead
)
def atualizar_categoria(
    cat_id: int,
    dados: CategoriaUpdate,
    session: Session = Depends(get_session)
):
    categoria = session.get(Categoria, cat_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(categoria, key, value)
    session.commit()
    session.refresh(categoria)
    return categoria

@app.delete(
    "/categorias/{cat_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_categoria(
    cat_id: int,
    session: Session = Depends(get_session)
):
    categoria = session.get(Categoria, cat_id)
    if not categoria:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    session.delete(categoria)
    session.commit()
    return

# --- Fornecedores ---
@app.post(
    "/fornecedores/", response_model=FornecedorRead,
    status_code=status.HTTP_201_CREATED
)
def criar_fornecedor(
    dados: FornecedorCreate,
    session: Session = Depends(get_session)
):
    fornecedor = Fornecedor(
        for_nome=dados.for_nome,
        for_telefone=dados.for_telefone,
        for_email=dados.for_email
    )
    session.add(fornecedor)
    session.commit()
    session.refresh(fornecedor)
    return fornecedor

@app.get(
    "/fornecedores/", response_model=list[FornecedorRead]
)
def listar_fornecedores(
    session: Session = Depends(get_session)
):
    return session.exec(select(Fornecedor)).all()

@app.put(
    "/fornecedores/{for_id}", response_model=FornecedorRead
)
def atualizar_fornecedor(
    for_id: int,
    dados: FornecedorUpdate,
    session: Session = Depends(get_session)
):
    fornecedor = session.get(Fornecedor, for_id)
    if not fornecedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fornecedor não encontrado"
        )
    for key, value in dados.dict(exclude_unset=True).items():
        setattr(fornecedor, key, value)
    session.commit()
    session.refresh(fornecedor)
    return fornecedor

@app.delete(
    "/fornecedores/{for_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_fornecedor(
    for_id: int,
    session: Session = Depends(get_session)
):
    fornecedor = session.get(Fornecedor, for_id)
    if not fornecedor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fornecedor não encontrado"
        )
    session.delete(fornecedor)
    session.commit()
    return

# --- Produtos ---
@app.post(
    "/produtos/", response_model=ProdutoRead,
    status_code=status.HTTP_201_CREATED
)
def criar_produto(
    dados: ProdutoCreate,
    session: Session = Depends(get_session)
):
    # Verifica existência de categoria e fornecedor
    if not session.get(Categoria, dados.pro_cat_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Categoria não encontrada"
        )
    if not session.get(Fornecedor, dados.pro_for_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Fornecedor não encontrado"
        )
    produto = Produto(
        **dados.dict()
    )
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return produto

@app.get(
    "/produtos/", response_model=list[ProdutoRead]
)
def listar_produtos(
    session: Session = Depends(get_session)
):
    return session.exec(select(Produto)).all()

@app.put(
    "/produtos/{pro_id}", response_model=ProdutoRead
)
def atualizar_produto(
    pro_id: int,
    dados: ProdutoUpdate,
    session: Session = Depends(get_session)
):
    produto = session.get(Produto, pro_id)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    update_data = dados.dict(exclude_unset=True)
    # Verifica possíveis mudanças de relações
    if "pro_cat_id" in update_data and not session.get(Categoria, update_data["pro_cat_id"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Nova categoria não encontrada"
        )
    if "pro_for_id" in update_data and not session.get(Fornecedor, update_data["pro_for_id"]):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Novo fornecedor não encontrado"
        )
    for key, value in update_data.items():
        setattr(produto, key, value)
    session.commit()
    session.refresh(produto)
    return produto

@app.delete(
    "/produtos/{pro_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def deletar_produto(
    pro_id: int,
    session: Session = Depends(get_session)
):
    produto = session.get(Produto, pro_id)
    if not produto:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Produto não encontrado"
        )
    session.delete(produto)
    session.commit()
    return