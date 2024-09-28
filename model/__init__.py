"""Módulo de inicialização dos modelos"""
import os
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# importando os elementos definidos no modelo
from model.base import Base
from model.mobile import Mobile
from model.preditor import Preditor
from model.pipeline import Pipeline
from model.preprocessador import PreProcessador
from model.avaliador import Avaliador
from model.carregador import Carregador

DB_PATH = "database/"
# Verifica se o diretorio não existe
if not os.path.exists(DB_PATH):
    # então cria o diretorio
    os.makedirs(DB_PATH)

# url de acesso ao banco (essa é uma url de acesso ao sqlite local)
DB_URL = f"sqlite:///{DB_PATH}/mobiles.sqlite3"

# cria a engine de conexão com o banco
engine = create_engine(DB_URL, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# cria o banco se ele não existir
if not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
