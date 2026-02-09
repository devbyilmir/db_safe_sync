from sqlalchemy import MetaData, Table, Column, Integer, String


TYPE_MAP = {
    "INTEGER": Integer,
    "VARCHAR": String,
    "TEXT": String,
}


class SyncExecutor:
    def __init__(self, engine):
        self.engine = engine

    def map_type(self, col_type_str):
        for key in TYPE_MAP:
            if key in col_type_str.upper():
                return TYPE_MAP[key]
        return String

    def apply(self, diff, source_schema):
        metadata = MetaData()

        for table_name in diff["tables_to_create"]:
            table_schema = source_schema[table_name]

            columns = []

            for col in table_schema.columns:
                col_type = self.map_type(col.type)

                columns.append(
                    Column(
                        col.name,
                        col_type,
                        primary_key=(col.name == "id"),
                    )
                )

            Table(
                table_name,
                metadata,
                *columns
            )

        metadata.create_all(self.engine)
