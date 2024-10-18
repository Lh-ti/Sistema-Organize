from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from config import DATABASE_URL  # Importa a URL do banco de dados do arquivo de configuração

# Criar o engine usando a URL do banco de dados definida em config.py
engine = create_engine(DATABASE_URL)

# Criar uma fábrica de sessões
Session = sessionmaker(bind=engine)

@contextmanager
def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()
