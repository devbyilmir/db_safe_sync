import os

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.db.inspector import SchemaInspector


load_dotenv()


def main():
    source_engine = create_engine(os.getenv("SOURCE_DB_URL"))
    target_engine = create_engine(os.getenv("TARGET_DB_URL"))

    source_inspector = SchemaInspector(source_engine)
    target_inspector = SchemaInspector(target_engine)

    source_schema = source_inspector.get_schema()
    target_schema = target_inspector.get_schema()

    print("SOURCE:", source_schema)
    print("TARGET:", target_schema)


if __name__ == "__main__":
    main()
