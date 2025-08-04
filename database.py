from sqlmodel import create_engine, Session

# Caminho do banco de dados SQLite
db_url = "sqlite:///estoque.db"

# Criação do engine com log SQL ativado
engine = create_engine(db_url, echo=True)

# Função para obter uma sessão do banco de dados
def get_session():
    with Session(engine) as session:
        yield session