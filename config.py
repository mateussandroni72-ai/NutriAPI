import os
from pydantic_settings import BaseSettings
from typing import List
from functools import lru_cache

class Settings(BaseSettings):
    """
    Configurações globais da aplicação.
    As variáveis podem ser lidas de um arquivo .env ou variáveis de ambiente.
    """
    
    # Informações da API
    APP_TITLE: str = "NutriAPI - Banco de Dados Nutricional Profissional"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "API de alta performance para consulta e gestão de dados nutricionais."
    
    # Configurações de Banco de Dados
    # Se não houver DATABASE_URL no ambiente, usa SQLite por padrão
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./nutriapi.db")
    
    # Configurações de Cache (Exemplo de tempo em segundos)
    CACHE_EXPIRE: int = 3600
    
    # Lista de Categorias pré-definidas (Conforme requisito)
    CATEGORIAS_LISTA: List[str] = [
        "Frutas", "Verduras", "Legumes", "Carnes", "Peixes", "Frango", 
        "Laticínios", "Cereais", "Grãos", "Oleaginosas", "Bebidas", 
        "Doces", "Massas", "Pães", "Temperos", "Óleos", "Gorduras", 
        "Industrializados", "Fast Food", "Sobremesas", "Suplementos"
    ]

    # Configurações de Segurança e Logs
    LOG_LEVEL: str = "INFO"
    DEBUG_MODE: bool = False

    class Config:
        # Permite carregar de um arquivo .env na raiz do projeto
        env_file = ".env"
        case_sensitive = True

@lru_cache()
def get_settings() -> Settings:
    """
    Retorna uma instância única das configurações (Singleton).
    O uso do @lru_cache garante que o arquivo .env seja lido apenas uma vez.
    """
    return Settings()

# Instância pronta para importação
settings = get_settings()