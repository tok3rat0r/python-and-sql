from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()


def create_connection():
    return psycopg2.connect(os.environ.get("DATABASE_URI"))
