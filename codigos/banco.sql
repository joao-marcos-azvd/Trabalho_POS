CREATE DATABASE db_estoque;
USE db_estoque;

CREATE TABLE tb_categorias (
    cat_id INT PRIMARY KEY AUTO_INCREMENT,
    cat_nome VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE tb_fornecedores (
    for_id INT PRIMARY KEY AUTO_INCREMENT,
    for_nome VARCHAR(255) NOT NULL,
    for_telefone VARCHAR(255) NOT NULL,
    for_email VARCHAR(255) NOT NULL
);

CREATE TABLE tb_produtos (
    pro_id INT PRIMARY KEY AUTO_INCREMENT,
    pro_nome VARCHAR(255) NOT NULL,
    pro_descricao VARCHAR(255) NOT NULL,
    pro_quantidade INT NOT NULL,
    pro_unidade VARCHAR(255) NOT NULL, -- unidade pode ser kg, m, g... etc
    /*pro_preco_custo FLOAT NOT NULL,
    pro_preco_venda FLOAT NOT NULL,*/
    pro_cat_id INT,
    pro_for_id INT,
    FOREIGN KEY (pro_cat_id) REFERENCES tb_categorias(cat_id),
    FOREIGN KEY (pro_for_id) REFERENCES tb_fornecedores(for_id)
);

CREATE TABLE tb_usuarios (
    usu_id INT PRIMARY KEY AUTO_INCREMENT,
    usu_nome VARCHAR(255) NOT NULL,
    usu_email VARCHAR(255) NOT NULL,
    usu_senha VARCHAR(255) NOT NULL,
    usu_tipo VARCHAR(255) NOT NULL -- o tipo seria adm ou fucionario normal, ja que ainda não foui definido
);
