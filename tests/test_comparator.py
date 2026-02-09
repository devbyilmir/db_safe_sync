from app.diff.comparator import SchemaComparator
from app.db.models import TableSchema, ColumnSchema


def test_table_creation_diff():
    comparator = SchemaComparator()

    source_schema = {
        "users": TableSchema(
            name="users",
            columns=[ColumnSchema(name="id", type="INTEGER")]
        )
    }

    target_schema = {}

    diff = comparator.compare(source_schema, target_schema)

    assert "users" in diff["tables_to_create"]
