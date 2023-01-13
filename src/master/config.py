from os import path
from dataclasses import dataclass, field


@dataclass
class Config:
    BASE_DIR: str = path.dirname(path.abspath(__file__))  # /app/

    # DB
    DB_HOST: str = "mongo"
    DB_PORT: int = 27017
    DBS: list = field(default_factory=lambda: [
        "yml",
    ])
    TIMEOUT: int = 5000

