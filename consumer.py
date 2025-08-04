# consumer_cli.py
# Requer: requests  → pip install requests

import requests

BASE_URL = "http://127.0.0.1:8000"
HEADERS = {"Content-Type": "application/json"}

# --- Usuários ---
def listar_usuarios():
    r = requests.get(f"{BASE_URL}/usuarios/", headers=HEADERS)
    if r.status_code == 200:
        usuarios = r.json()
        if usuarios:
            print("\n--- Usuários Cadastrados ---")
            for u in usuarios:
                print(f"ID: {u['usu_id']}, Nome: {u['usu_nome']}, E-mail: {u['usu_email']}, Tipo: {u['usu_tipo']}")
        else:
            print("Nenhum usuário cadastrado.")
    else:
        print("Erro ao listar usuários.")

def cadastrar_usuario():
    nome  = input("Nome: ")
    email = input("E-mail: ")
    senha = input("Senha: ")
    tipo  = input("Tipo: ")
    payload = {
        "usu_nome": nome,
        "usu_email": email,
        "usu_senha": senha,
        "usu_tipo": tipo
    }
    r = requests.post(f"{BASE_URL}/usuarios/", json=payload, headers=HEADERS)
    if r.status_code == 201:
        print("Usuário cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar usuário:", r.json().get("detail", r.status_code))

def deletar_usuario():
    usu_id = input("ID do usuário a deletar: ")
    r = requests.delete(f"{BASE_URL}/usuarios/{usu_id}", headers=HEADERS)
    if r.status_code == 204:
        print("Usuário deletado com sucesso!")
    else:
        print("Erro ao deletar usuário.")

def editar_usuario():
    usu_id = input("ID do usuário a editar: ")
    payload = {}
    nome  = input("Novo nome (ENTER p/ manter): ")
    email = input("Novo e-mail (ENTER p/ manter): ")
    senha = input("Nova senha (ENTER p/ manter): ")
    tipo  = input("Novo tipo (ENTER p/ manter): ")
    if nome:  payload["usu_nome"]  = nome
    if email: payload["usu_email"] = email
    if senha: payload["usu_senha"] = senha
    if tipo:  payload["usu_tipo"]  = tipo

    r = requests.put(f"{BASE_URL}/usuarios/{usu_id}", json=payload, headers=HEADERS)
    if r.status_code == 200:
        print("Usuário atualizado com sucesso!")
    else:
        print("Erro ao atualizar usuário:", r.json().get("detail", r.status_code))

# --- Categorias ---
def listar_categorias():
    r = requests.get(f"{BASE_URL}/categorias/", headers=HEADERS)
    if r.status_code == 200:
        cats = r.json()
        if cats:
            print("\n--- Categorias Cadastradas ---")
            for c in cats:
                print(f"ID: {c['cat_id']}, Nome: {c['cat_nome']}")
        else:
            print("Nenhuma categoria cadastrada.")
    else:
        print("Erro ao listar categorias.")

def cadastrar_categoria():
    nome = input("Nome da categoria: ")
    r = requests.post(f"{BASE_URL}/categorias/", json={"cat_nome": nome}, headers=HEADERS)
    if r.status_code == 201:
        print("Categoria cadastrada com sucesso!")
    else:
        print("Erro ao cadastrar categoria.")

def deletar_categoria():
    cat_id = input("ID da categoria a deletar: ")
    r = requests.delete(f"{BASE_URL}/categorias/{cat_id}", headers=HEADERS)
    if r.status_code == 204:
        print("Categoria deletada com sucesso!")
    else:
        print("Erro ao deletar categoria.")

def editar_categoria():
    cat_id = input("ID da categoria a editar: ")
    nome = input("Novo nome da categoria: ")
    r = requests.put(f"{BASE_URL}/categorias/{cat_id}", json={"cat_nome": nome}, headers=HEADERS)
    if r.status_code == 200:
        print("Categoria atualizada com sucesso!")
    else:
        print("Erro ao atualizar categoria.")

# --- Fornecedores ---
def listar_fornecedores():
    r = requests.get(f"{BASE_URL}/fornecedores/", headers=HEADERS)
    if r.status_code == 200:
        fts = r.json()
        if fts:
            print("\n--- Fornecedores Cadastrados ---")
            for f in fts:
                print(f"ID: {f['for_id']}, Nome: {f['for_nome']}, Tel: {f['for_telefone']}, Email: {f['for_email']}")
        else:
            print("Nenhum fornecedor cadastrado.")
    else:
        print("Erro ao listar fornecedores.")

def cadastrar_fornecedor():
    nome     = input("Nome do fornecedor: ")
    telefone = input("Telefone: ")
    email    = input("E-mail: ")
    payload = {"for_nome": nome, "for_telefone": telefone, "for_email": email}
    r = requests.post(f"{BASE_URL}/fornecedores/", json=payload, headers=HEADERS)
    if r.status_code == 201:
        print("Fornecedor cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar fornecedor.")

def deletar_fornecedor():
    for_id = input("ID do fornecedor a deletar: ")
    r = requests.delete(f"{BASE_URL}/fornecedores/{for_id}", headers=HEADERS)
    if r.status_code == 204:
        print("Fornecedor deletado com sucesso!")
    else:
        print("Erro ao deletar fornecedor.")

def editar_fornecedor():
    for_id = input("ID do fornecedor a editar: ")
    payload = {}
    nome     = input("Novo nome (ENTER p/ manter): ")
    telefone = input("Novo telefone (ENTER p/ manter): ")
    email    = input("Novo e-mail (ENTER p/ manter): ")
    if nome:     payload["for_nome"]     = nome
    if telefone: payload["for_telefone"] = telefone
    if email:    payload["for_email"]    = email
    r = requests.put(f"{BASE_URL}/fornecedores/{for_id}", json=payload, headers=HEADERS)
    if r.status_code == 200:
        print("Fornecedor atualizado com sucesso!")
    else:
        print("Erro ao atualizar fornecedor.")

# --- Produtos ---
def listar_produtos():
    r = requests.get(f"{BASE_URL}/produtos/", headers=HEADERS)
    if r.status_code == 200:
        prods = r.json()
        if prods:
            print("\n--- Produtos Cadastrados ---")
            for p in prods:
                print(f"ID: {p['pro_id']}, Nome: {p['pro_nome']}, Quantidade: {p['pro_quantidade']} {p['pro_unidade']}, CatID: {p['pro_cat_id']}, ForID: {p['pro_for_id']}")
        else:
            print("Nenhum produto cadastrado.")
    else:
        print("Erro ao listar produtos.")

def cadastrar_produto():
    nome      = input("Nome do produto: ")
    desc      = input("Descrição: ")
    qtd       = int(input("Quantidade: "))
    unidade   = input("Unidade: ")
    cat_id    = int(input("ID da categoria: "))
    for_id    = int(input("ID do fornecedor: "))
    payload = {
        "pro_nome": nome,
        "pro_descricao": desc,
        "pro_quantidade": qtd,
        "pro_unidade": unidade,
        "pro_cat_id": cat_id,
        "pro_for_id": for_id
    }
    r = requests.post(f"{BASE_URL}/produtos/", json=payload, headers=HEADERS)
    if r.status_code == 201:
        print("Produto cadastrado com sucesso!")
    else:
        print("Erro ao cadastrar produto:", r.json().get("detail", r.status_code))

def deletar_produto():
    pro_id = input("ID do produto a deletar: ")
    r = requests.delete(f"{BASE_URL}/produtos/{pro_id}", headers=HEADERS)
    if r.status_code == 204:
        print("Produto deletado com sucesso!")
    else:
        print("Erro ao deletar produto.")

def editar_produto():
    pro_id = input("ID do produto a editar: ")
    payload = {}
    nome = input("Novo nome (ENTER p/ manter): ")
    if nome: payload["pro_nome"] = nome
    # adicione outros campos conforme desejado...
    r = requests.put(f"{BASE_URL}/produtos/{pro_id}", json=payload, headers=HEADERS)
    if r.status_code == 200:
        print("Produto atualizado com sucesso!")
    else:
        print("Erro ao atualizar produto.")

# --- Menu principal ---
def menu():
    while True:
        print("""
==== MENU PRINCIPAL ====
1. Listar Usuários
2. Cadastrar Usuário
3. Editar Usuário
4. Deletar Usuário

5. Listar Categorias
6. Cadastrar Categoria
7. Editar Categoria
8. Deletar Categoria

9. Listar Fornecedores
10. Cadastrar Fornecedor
11. Editar Fornecedor
12. Deletar Fornecedor

13. Listar Produtos
14. Cadastrar Produto
15. Editar Produto
16. Deletar Produto

0. Sair
""")
        opc = input("Escolha uma opção: ")
        if opc == "0":
            print("Encerrando...")
            break
        elif opc == "1": listar_usuarios()
        elif opc == "2": cadastrar_usuario()
        elif opc == "3": editar_usuario()
        elif opc == "4": deletar_usuario()
        elif opc == "5": listar_categorias()
        elif opc == "6": cadastrar_categoria()
        elif opc == "7": editar_categoria()
        elif opc == "8": deletar_categoria()
        elif opc == "9": listar_fornecedores()
        elif opc == "10": cadastrar_fornecedor()
        elif opc == "11": editar_fornecedor()
        elif opc == "12": deletar_fornecedor()
        elif opc == "13": listar_produtos()
        elif opc == "14": cadastrar_produto()
        elif opc == "15": editar_produto()
        elif opc == "16": deletar_produto()
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
