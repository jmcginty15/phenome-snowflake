class Warehouse():

    def __init__(self, warehouse_data):
        self.name = warehouse_data[0]
        self.state = warehouse_data[1]
        self.type = warehouse_data[2]
        self.size = warehouse_data[3]
        self.min_cluster_count = warehouse_data[4]
        self.max_cluster_count = warehouse_data[5]
        self.started_clusters = warehouse_data[6]
        self.running = warehouse_data[7]
        self.queued = warehouse_data[8]
        self.is_default = warehouse_data[9] == 'Y'
        self.is_current = warehouse_data[10] == 'Y'
        self.auto_suspend = warehouse_data[11]
        self.auto_resume = warehouse_data[12] == 'true'
        self.available = warehouse_data[13]
        self.provisioning = warehouse_data[14]
        self.quiescing = warehouse_data[15]
        self.other = warehouse_data[16]
        self.created_on = warehouse_data[17]
        self.resumed_on = warehouse_data[18]
        self.updated_on = warehouse_data[19]
        self.owner = warehouse_data[20]
        self.comment = warehouse_data[21]
        self.resource_monitor = warehouse_data[22] if warehouse_data[22] != 'null' else None
        self.actives = warehouse_data[23]
        self.pendings = warehouse_data[24]
        self.failed = warehouse_data[25]
        self.suspended = warehouse_data[26]
        self.uuid = warehouse_data[27]


class Database():

    def __init__(self, database_data):
        self.created_on = database_data[0]
        self.name = database_data[1]
        self.is_default = database_data[2] == 'Y'
        self.is_current = database_data[3] == 'Y'
        self.origin = database_data[4]
        self.owner = database_data[5]
        self.comment = database_data[6]
        self.options = database_data[7]
        self.retention_time = database_data[8]


class Table():

    def __init__(self, table_data, columns):
        self.created_on = table_data[0]
        self.name = table_data[1]
        self.database_name = table_data[2]
        self.schema_name = table_data[3]
        self.kind = table_data[4]
        self.comment = table_data[5]
        self.cluster_by = table_data[6]
        self.rows = table_data[7]
        self.bytes = table_data[8]
        self.owner = table_data[9]
        self.retention_time = table_data[10]
        self.dropped_on = table_data[11]
        self.automatic_clustering = table_data[12]
        self.search_optimization = table_data[13]
        self.search_optimization_progress = table_data[14]
        self.search_optimization_bytes = table_data[15]
        self.columns = columns


class Column():

    def __init__(self, column_data):
        self.table_name = column_data[0]
        self.schema_name = column_data[1]
        self.column_name = column_data[2]
        self.data_type = column_data[3]
        self.nullable = column_data[4] == 'true'
        self.default = column_data[5]
        self.kind = column_data[6]
        self.expression = column_data[7]
        self.comment = column_data[8]
        self.database_name = column_data[9]
        self.autoincrement = column_data[10]


class RowData():

    def __init__(self, row_data, column_names):
        for i, name in enumerate(column_names):
            setattr(self, name, row_data[i])
