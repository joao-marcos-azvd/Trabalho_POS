create database db_estoque;
use db_estoque;

CREATE TABLE tb_usuarios (
    usu_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    usu_nome TEXT NOT NULL,
    usu_email TEXT NOT NULL,
    usu_senha TEXT NOT NULL,
    usu_tipo TEXT NOT NULL -- o tipo seria adm ou fucionario normal, ja que ainda não foui definido
);

CREATE TABLE tb_produtos (
    pro_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    pro_nome TEXT NOT NULL,
    pro_descricao TEXT NOT NULL,
    pro_quantidade INTEGER NOT NULL,
    pro_unidade TEXT NOT NULL, -- unidade pode ser kg, m, g... etc
    /*pro_preco_custo FLOAT NOT NULL,
    pro_preco_venda FLOAT NOT NULL,*/
    pro_cat_id INTEGER,
    pro_for_id INTEGER,
    FOREIGN KEY (pro_cat_id) REFERENCES tb_categorias(cat_id),
    FOREIGN KEY (pro_for_id) REFERENCES tb_fornecedores(for_id)
);


CREATE TABLE tb_categorias (
    cat_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    cat_nome TEXT NOT NULL UNIQUE
);

CREATE TABLE tb_fornecedores (
    for_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    for_nome TEXT NOT NULL,
    for_telefone TEXT NOT NULL,
    for_email TEXT NOT NULL
);
