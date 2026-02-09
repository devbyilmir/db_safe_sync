import os
import argparse

from dotenv import load_dotenv
from sqlalchemy import create_engine

from app.db.inspector import SchemaInspector
from app.diff.comparator import SchemaComparator
from app.sync.executor import SyncExecutor


load_dotenv()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    source_engine = create_engine(os.getenv("SOURCE_DB_URL"))
    target_engine = create_engine(os.getenv("TARGET_DB_URL"))

    source_inspector = SchemaInspector(source_engine)
    target_inspector = SchemaInspector(target_engine)

    source_schema = source_inspector.get_schema()
    target_schema = target_inspector.get_schema()

    comparator = SchemaComparator()
    diff = comparator.compare(source_schema, target_schema)

    print("\nPLAN:")
    
    if not diff["tables_to_create"] and not diff["tables_to_drop"]:
        print("  no changes detected")


    for table in diff["tables_to_create"]:
        print(f"  + create table {table}")

    for table in diff["tables_to_drop"]:
        print(f"  - drop table {table}")

    executor = SyncExecutor(target_engine)
    executor.apply(
        diff,
        source_schema,
        dry_run=not args.apply
    )


if __name__ == "__main__":
    main()
