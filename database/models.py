from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BotConfig(Base):
    __tablename__ = "bot_config"
    id = Column(Integer, primary_key=True)
    token = Column(String, nullable=False)
    prefix = Column(String, default="!")

# Configuração do banco de dados
engine = create_engine("sqlite:///bot_config.db")
Base.metadata.create_all(engine)