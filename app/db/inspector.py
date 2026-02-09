from sqlalchemy import inspect

from app.db.models import TableSchema, ColumnSchema


class SchemaInspector:
    def __init__(self, engine):
        self.engine = engine
        self.inspector = inspect(engine)

    def get_schema(self):
        tables = []

        for table_name in self.inspector.get_table_names():
            columns_info = self.inspector.get_columns(table_name)

            columns = [
                ColumnSchema(
                    name=col["name"],
                    type=str(col["type"])
                )
                for col in columns_info
            ]

            tables.append(
                TableSchema(
                    name=table_name,
                    columns=columns
                )
            )

        return tables
