import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String

from app.db.inspector import SchemaInspector
from app.diff.comparator import SchemaComparator


load_dotenv()


def main():
    source_engine = create_engine(os.getenv("SOURCE_DB_URL"))
    target_engine = create_engine(os.getenv("TARGET_DB_URL"))

    metadata = MetaData()

    Table(
        "users",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
    )

    metadata.create_all(source_engine)

    source_inspector = SchemaInspector(source_engine)
    target_inspector = SchemaInspector(target_engine)

    source_schema = source_inspector.get_schema()
    target_schema = target_inspector.get_schema()

    comparator = SchemaComparator()
    diff = comparator.compare(source_schema, target_schema)

    print("DIFF:", diff)


if __name__ == "__main__":
    main()
