from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from models import Categoria, Fornecedor, Produto, Usuario
from database import get_session, engine

app = FastAPI()

# Cria as tabelas no banco de dados
SQLModel.metadata.create_all(engine)

# Rotas para Usuarios
@app.post("/usuarios/")
def criar_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    session.add(usuario)
    session.commit()
    session.refresh(usuario)
    return {"mensagem": "Usuário criado com sucesso", "usuario": usuario}

@app.get("/usuarios/")
def listar_usuarios(session: Session = Depends(get_session)):
    usuarios = session.exec(select(Usuario)).all()
    return usuarios

@app.put("/usuarios/{usu_id}")
def atualizar_usuario(usu_id: int, usuario: Usuario, session: Session = Depends(get_session)):
    db_usuario = session.get(Usuario, usu_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    usuario_data = usuario.dict(exclude_unset=True)
    for key, value in usuario_data.items():
        setattr(db_usuario, key, value)
    
    session.add(db_usuario)
    session.commit()
    session.refresh(db_usuario)
    return {"mensagem": "Usuário atualizado com sucesso", "usuario": db_usuario}

@app.delete("/usuarios/{usu_id}")
def deletar_usuario(usu_id: int, session: Session = Depends(get_session)):
    db_usuario = session.get(Usuario, usu_id)
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    session.delete(db_usuario)
    session.commit()
    return {"mensagem": "Usuário deletado com sucesso"}

# Rotas para Categorias
@app.post("/categorias/")
def criar_cat(categoria: Categoria, session: Session = Depends(get_session)):
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return {"mensagem": "Categoria criada com sucesso", "categoria": categoria}

@app.get("/categorias/")
def listar_cat(session: Session = Depends(get_session)):
    categorias = session.exec(select(Categoria)).all()
    return categorias

@app.put("/categorias/{cat_id}")
def atualizar_cat(cat_id: int, categoria: Categoria, session: Session = Depends(get_session)):
    db_categoria = session.get(Categoria, cat_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    categoria_data = categoria.dict(exclude_unset=True)
    for key, value in categoria_data.items():
        setattr(db_categoria, key, value)
    
    session.add(db_categoria)
    session.commit()
    session.refresh(db_categoria)
    return {"mensagem": "Categoria atualizada com sucesso", "categoria": db_categoria}

@app.delete("/categorias/{cat_id}")
def deletar_cat(cat_id: int, session: Session = Depends(get_session)):
    db_categoria = session.get(Categoria, cat_id)
    if not db_categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    
    session.delete(db_categoria)
    session.commit()
    return {"mensagem": "Categoria deletada com sucesso"}

# Rotas para Produtos
@app.post("/produtos/")
def criar_pro(produto: Produto, session: Session = Depends(get_session)):
    # Verificar se categoria e fornecedor existem
    categoria = session.get(Categoria, produto.pro_cat_id)
    fornecedor = session.get(Fornecedor, produto.pro_for_id)
    
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    if not fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    session.add(produto)
    session.commit()
    session.refresh(produto)
    return {"mensagem": "Produto criado com sucesso", "produto": produto}

@app.get("/produtos/")
def listar_pro(session: Session = Depends(get_session)):
    produtos = session.exec(select(Produto)).all()
    return produtos

@app.put("/produtos/{pro_id}")
def atualizar_pro(pro_id: int, produto: Produto, session: Session = Depends(get_session)):
    db_produto = session.get(Produto, pro_id)
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    # Verificar se categoria e fornecedor existem
    if produto.pro_cat_id != db_produto.pro_cat_id:
        categoria = session.get(Categoria, produto.pro_cat_id)
        if not categoria:
            raise HTTPException(status_code=404, detail="Nova categoria não encontrada")
    
    if produto.pro_for_id != db_produto.pro_for_id:
        fornecedor = session.get(Fornecedor, produto.pro_for_id)
        if not fornecedor:
            raise HTTPException(status_code=404, detail="Novo fornecedor não encontrado")
    
    produto_data = produto.dict(exclude_unset=True)
    for key, value in produto_data.items():
        setattr(db_produto, key, value)
    
    session.add(db_produto)
    session.commit()
    session.refresh(db_produto)
    return {"mensagem": "Produto atualizado com sucesso", "produto": db_produto}

@app.delete("/produtos/{pro_id}")
def deletar_pro(pro_id: int, session: Session = Depends(get_session)):
    db_produto = session.get(Produto, pro_id)
    if not db_produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    session.delete(db_produto)
    session.commit()
    return {"mensagem": "Produto deletado com sucesso"}

# Rotas para Fornecedores
@app.post("/fornecedores/")
def criar_fornecedor(fornecedor: Fornecedor, session: Session = Depends(get_session)):
    session.add(fornecedor)
    session.commit()
    session.refresh(fornecedor)
    return {"mensagem": "Fornecedor criado com sucesso", "fornecedor": fornecedor}

@app.get("/fornecedores/")
def listar_fornecedores(session: Session = Depends(get_session)):
    fornecedores = session.exec(select(Fornecedor)).all()
    return fornecedores

@app.put("/fornecedores/{for_id}")
def atualizar_fornecedor(for_id: int, fornecedor: Fornecedor, session: Session = Depends(get_session)):
    db_fornecedor = session.get(Fornecedor, for_id)
    if not db_fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    fornecedor_data = fornecedor.dict(exclude_unset=True)
    for key, value in fornecedor_data.items():
        setattr(db_fornecedor, key, value)
    
    session.add(db_fornecedor)
    session.commit()
    session.refresh(db_fornecedor)
    return {"mensagem": "Fornecedor atualizado com sucesso", "fornecedor": db_fornecedor}

@app.delete("/fornecedores/{for_id}")
def deletar_fornecedor(for_id: int, session: Session = Depends(get_session)):
    db_fornecedor = session.get(Fornecedor, for_id)
    if not db_fornecedor:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    
    session.delete(db_fornecedor)
    session.commit()
    return {"mensagem": "Fornecedor deletado com sucesso"}
