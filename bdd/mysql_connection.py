import os
from pathlib import Path

from dotenv import load_dotenv
import mysql.connector


class MySQLConnection:
    connection = None
    cursor = None

    @classmethod
    def connecter(cls):
        if cls.connection is not None and cls.cursor is not None:
            return cls.connection

        env_path = Path(__file__).resolve().parents[1] / ".env"
        load_dotenv(env_path)

        cls.connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        cls.cursor = cls.connection.cursor()
        return cls.connection

    @classmethod
    def deconnecter(cls):
        if cls.cursor is not None:
            cls.cursor.close()
            cls.cursor = None

        if cls.connection is not None:
            cls.connection.close()
            cls.connection = None
