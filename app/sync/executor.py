from sqlalchemy import MetaData, Table, Column, Integer, String


class SyncExecutor:
    def __init__(self, engine):
        self.engine = engine

    def apply(self, diff):
        metadata = MetaData()

        for table_name in diff["tables_to_create"]:
            Table(
                table_name,
                metadata,
                Column("id", Integer, primary_key=True),
                Column("name", String),
            )

        metadata.create_all(self.engine)
