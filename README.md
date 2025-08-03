# Documentação do Projeto: Estoque Fácil
## 1. Visão Geral
**Tecnologias utilizadas :**
- Python
- FastAPI
- Uvicorn
- SQLModel

**Descrição :** 

Dentro das tecnologias utilizadas no projeto, o python é uma linguagem de programação fácil e de alto nível.  No desenvolvimento web, Python é amplamente utilizado no backend, ou seja, na parte lógica e funcional dos sistemas, lidando com o processamento de dados, comunicação com bancos de dados, regras de negócio e integração com APIs. Tornando uma linguagem ótima para aplicações seguras na web.

Já a FastAPI é um framework moderno e rápido para a construção de APIs com Python, baseado nos padrões do OpenAPI e JSON Schema. Ele é conhecido por sua alta performance, facilidade de uso e suporte nativo a validação de dados, documentação automática de endpoints e tipagem estática com Python. É uma ótima opção para desenvolver aplicações web com o python. 

Como também o Uvicorn, que é um servidor ASGI (Asynchronous Server Gateway Interface) leve e de alta performance, projetado para rodar aplicações web assíncronas, como as desenvolvidas com FastAPI. Ele é eficiente no gerenciamento de múltiplas requisições simultâneas e é ideal para aplicações modernas baseadas em Python que utilizam operações assíncronas para melhor desempenho.


**Objetivo :** 

O principal objetivo do Estoque Fácil é desenvolver um sistema simples, rápido e eficaz que possa facilitar o uso de um gerenciamento de estoque de amplas formas, podendo atender uma grande gama de empresas e públicos. O sistema visa oferecer uma solução prática para controlar a entrada, saída e quantidade de produtos em estoque, garantindo maior organização, redução de perdas e apoio na tomada de decisões estratégicas. Além disso, busca-se automatizar tarefas rotineiras de uma forma  mais eficaz.


## 2. Descrição Detalhada do Projeto
### O que é o projeto? 
O projeto é o desenvolvimento de um sistema de gerenciamento de estoque, que é uma ferramenta crucial para a otimização de operações de qualquer negócio que lide com produtos, seja ele de pequeno, médio ou grande porte, e tem como objetivo principal assegurar a disponibilidade dos materiais.

A ausência de um controle de estoque eficiente pode gerar uma série de desafios que impactam diretamente a saúde financeira dos negócios e a satisfação de seus clientes. A falha em um estoque, por exemplo, leva à perda de vendas e à frustração do consumidor, que busca por um produto e não o encontra. Por outro lado, o excesso de estoque imobiliza capital, gera custos de armazenagem desnecessários e aumenta o risco de perdas por desatualização ou inutilização.

Ademais, a otimização de custos operacionais é um benefício significativo. Ao reduzir perdas, evitar gastos excessivos com armazenagem e otimizar a movimentação de produtos, a empresa consegue operar de forma mais enxuta e lucrativa. A eficiência operacional também é aprimorada, com processos claros e automatizados para a entrada e saída de mercadorias, o que agiliza o fluxo de trabalho e diminui a incidência de erros, além de ampliar a capacidade de tomar decisões estratégicas. 

Em suma, a implementação de um sistema como este nos leva a redução de custos ao evitar perdas e otimizar o espaço de armazenamento. As operações tornam-se mais eficientes, pois sabe-se exatamente o que se tem e onde está, de forma a agilizar o trabalho.


### 2.1 Funcionalidades Principais
- **Gerenciamento de Usuários**  
  Permite criar, listar, atualizar e deletar usuários com os campos: nome, email, senha e tipo.

- **Gerenciamento de Categorias**  
  Permite cadastrar, consultar, atualizar e excluir categorias que agrupam os produtos no estoque.

- **Gerenciamento de Produtos**  
  Possibilita o cadastro, listagem, edição e exclusão de produtos com os campos: nome, descrição, quantidade, unidade, e associações com categoria e fornecedor.

- **Gerenciamento de Fornecedores**  
  Permite manter um registro com nome, telefone e email dos fornecedores, além das operações de CRUD.

### 2.2 Arquitetura do Código
    main/
    ├── main.py            # Ponto de entrada (inicialização)
    ├── models.py          # Modelos com Pydantic

## 3. Etapas de Entrega (Cronograma Detalhado)
### Etapa 01: Definição do escopo do projeto
Traçamos os limites do que o sistema fará ou não, listando as funcionalidades essenciais, como registro de entradas e saídas, além das demais, como edição de dados, de modo a garantir que o sistema atenda às necessidades reais. 

### Etapa 02: Definição dos modelos UML
Desenvolveu-se os modelos UML do projeto. Diagrama de classe descreve a estrutura estática do sistema, mostrando objetos, seus atributos e como se relacionam. Diagrama de caso de uso foca na interação entre o usuário e o sistema. Diagrama de atividade ilustra o fluxo de trabalho ou o processo de execução. Por fim, o diagrama de sequência detalha a ordem e a interação das mensagens entre os objetos em um cenário específico.

### Etapa 03: Definição de modelo de banco de dados
Para construir nosso sistema de gerenciamento de estoque, definimos a estrutura do banco de dados utlizando SQLModel. Estabelecemos tabelas fundamentais: tb_categorias e tb_fornecedores para organizar informações básicas. tb_produtos relaciona os itens às categorias e fornecedores. Adicionamos tb_usuarios para controle de acesso e, para um sistema mais completo, tb_movimentacoes para registrar todas as entradas e saídas.

Observação: A definição do banco foi feita na branch Test do nosso repositório no GitHub.


### Etapa 04: Implementação dos endpoints
Na primeira parte da implementação dos endpoints do nosso sistema, definimos rotas claras para cada funcionalidade, como /produtos para listar itens ou /produtos/{pro_nome} para atualizar seus dados. Usamos métodos HTTP (GET para buscar, POST para criar, PUT para atualizar, DELETE para remover) para cada interação. 

### Etapa 05: Testes e melhorias
Realização de testes unitários em cada parte do código (funções de cadastro, baixa, etc.) para assegurar que funcionem individualmente. Em seguida, vêm os testes de integração, verificando se as diferentes partes do sistema se comunicam corretamente, por exemplo, se o cadastro de um produto reflete na movimentação de estoque. A partir da análise de desempenho, caso necessário, haverá a implementação de melhorias.
