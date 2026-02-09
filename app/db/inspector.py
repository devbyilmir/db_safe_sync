class SchemaInspector:
    def __init__(self, engine):
        self.engine = engine

    def get_schema(self):
        raise NotImplementedError
