class SchemaComparator:
    def compare(self, source_schema, target_schema):
        source_tables = set(source_schema.keys())
        target_tables = set(target_schema.keys())

        tables_to_create = source_tables - target_tables
        tables_to_drop = target_tables - source_tables
        tables_common = source_tables & target_tables

        columns_diff = {}

        for table_name in tables_common:
            source_columns = {
                col.name: col for col in source_schema[table_name].columns
            }
            target_columns = {
                col.name: col for col in target_schema[table_name].columns
            }

            source_col_set = set(source_columns.keys())
            target_col_set = set(target_columns.keys())

            columns_to_add = source_col_set - target_col_set
            columns_to_remove = target_col_set - source_col_set

            if columns_to_add or columns_to_remove:
                columns_diff[table_name] = {
                    "columns_to_add": list(columns_to_add),
                    "columns_to_remove": list(columns_to_remove),
                }

        return {
            "tables_to_create": list(tables_to_create),
            "tables_to_drop": list(tables_to_drop),
            "columns_diff": columns_diff,
        }
