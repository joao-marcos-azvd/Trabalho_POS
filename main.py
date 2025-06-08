from fastapi import FastAPI, Depends
from models import Categoria, Fornecedor, Produto, Usuario
TESTANDO!

app = FastAPI()

usuarios = []
categorias = []
fornecedores = []
produtos = []

#usuarios
@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    usuarios.append(usuario)
    return {"mensagem": "Usuário criado com sucesso", "usuario": usuario}

@app.get("/usuarios/")
def listar_usuarios():
    return usuarios

@app.put("/usuarios/{usu_nome}")
def atualizar_usuario(usu_nome: str, usuario: Usuario):
    for i, usu in enumerate(usuarios):
        if usu.usu_nome == usu_nome:
            usuarios[i] = usuario
            return {"mensagem": "Usuário atualizado com sucesso", "usuario": usuario}
    return {"erro": "Usuário não encontrado"}

@app.delete("/usuarios/{usu_nome}")
def deletar_usuario(usu_nome: str):
    for i, usu in enumerate(usuarios):
        if usu.usu_nome == usu_nome:
            usuarios.pop(i)
            return {"mensagem": "Usuário deletado com sucesso"}
    return {"erro": "Usuário não encontrado"}

#categorias
@app.post("/categorias/")
def criar_cat(categoria: Categoria):
    categorias.append(categoria)
    return {"mensagem": "Categoria criada com sucesso", "categoria": categoria}

@app.get("/categorias/")
def listar_cat():
    return categorias

@app.put("/categorias/{cat_nome}")
def atualizar_cat(cat_nome: str,categoria: Categoria):
    for i, cat in enumerate(categorias):
        if cat.nome == cat_nome:
            categorias[i] = categoria
            return {"mensagem": "categoria atualizada com sucsso", "categoria": categoria}
        return {"erro": "Categoria não encontrada"}
    
@app.delete("/categorias/{cat_nome}")
def deletar_cat(cat_nome: str):
    for i, cat in enumerate(categorias):
        if cat.nome == cat_nome:
            categorias.pop(i)
            return {"mensagem": "categoria deletada com sucsso"}
        return {"erro": "Categoria não encontrada"}

#produtos
@app.post("/produtos/")
def criar_pro(produto: Produto):
    produtos.append(produto)
    return {"mensagem": "Produto criado com sucesso", "produto": produto}

@app.get("/produtos/")
def listar_pro():
    return produtos  

@app.put("/produtos/{pro_nome}")
def atualizar_pro(pro_nome: str, produto: Produto):
    for i, pro in enumerate(produtos):
        if pro.nome == pro_nome:
            produtos[i] = produto
            return {"mensagem": "Produto atualizado com sucesso", "produto": produto}
    return {"erro": "Produto não encontrado"}  

@app.delete("/produtos/{pro_nome}")
def deletar_pro(pro_nome: str):
    for i, pro in enumerate(produtos):
        if pro.nome == pro_nome:
            produtos.pop(i)
            return {"mensagem": "Produto deletado com sucesso"}
    return {"erro": "Produto não encontrado"}  

#fornecedores
@app.post("/fornecedores/")
def criar_fornecedor(fornecedor: Fornecedor):
    fornecedores.append(fornecedor)
    return {"mensagem": "Fornecedor criado com sucesso", "fornecedor": fornecedor}

@app.get("/fornecedores/")
def listar_fornecedores():
    return fornecedores

@app.put("/fornecedores/{for_nome}")
def atualizar_fornecedor(for_nome: str, fornecedor: Fornecedor):
    for i, fornc in enumerate(fornecedores):
        if fornc.for_nome == for_nome:
            fornecedores[i] = fornecedor
            return {"mensagem": "Fornecedor atualizado com sucesso", "fornecedor": fornecedor}
    return {"erro": "Fornecedor não encontrado"}

@app.delete("/fornecedores/{for_nome}")
def deletar_fornecedor(for_nome: str):
    for i, fornc in enumerate(fornecedores):
        if fornc.for_nome == for_nome:
            fornecedores.pop(i)
            return {"mensagem": "Fornecedor deletado com sucesso"}
    return {"erro": "Fornecedor não encontrado"}



