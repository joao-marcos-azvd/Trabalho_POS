from fastapi import FastAPI, Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, Categoria, Fornecedor, Produto, Usuario
from schemas import CategoriaCreate, FornecedorCreate, ProdutoCreate, UsuarioCreate


DATABASE_URL = "sqlite:///./db_estoque.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/categorias/")
def criar_categoria(cat: CategoriaCreate, db: Session = Depends(get_db)):
    nova = Categoria(cat_nome=cat.cat_nome)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

@app.post("/fornecedores/")
def criar_fornecedor(fornec: FornecedorCreate, db: Session = Depends(get_db)):
    novo = Fornecedor(**fornec.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/produtos/")
def criar_produto(prod: ProdutoCreate, db: Session = Depends(get_db)):
    novo = Produto(**prod.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.post("/usuarios/")
def criar_usuario(usu: UsuarioCreate, db: Session = Depends(get_db)):
    novo = Usuario(**usu.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
