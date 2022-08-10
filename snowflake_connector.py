import string

from pyparsing import col
from snowflake_init import cs
import pandas as pd
from classes import *
from utils import apply_wheres


class SNOWFLAKE_CONNECTOR():

    def __init__(self, warehouse_name: str = 'GDM_ATHENA_DEID', database_name: str = 'DATA_SCIENCE_DEID'):
        self.warehouse_name = warehouse_name
        self.database_name = database_name
        self.cursor = cs
        self.cursor.execute(f'USE DATABASE {database_name}')

    def list_warehouses(self):
        self.cursor.execute('SHOW WAREHOUSES')

        results = self.cursor.fetchall()
        warehouses = []
        for result in results:
            warehouses.append(Warehouse(result))

        return warehouses

    def list_databases(self):
        self.cursor.execute('SHOW DATABASES')

        results = self.cursor.fetchall()
        databases = []
        for result in results:
            databases.append(Database(result))

        return databases

    def list_tables(self):
        self.cursor.execute('SHOW TABLES')

        results = self.cursor.fetchall()
        tables = []
        for result in results:
            self.cursor.execute(
                f'SELECT * FROM {self.warehouse_name}.{result[1]}')
            tables.append(Table(result, self.cursor.description))

        return tables

    def list_columns(self, table_name=None):
        query = 'SHOW COLUMNS'
        if table_name:
            query += f' IN TABLE {self.warehouse_name}.{table_name}'

        try:
            self.cursor.execute(query)

            results = self.cursor.fetchall()
            columns = []
            for result in results:
                columns.append(Column(result))

            return {'table': table_name, 'columns': columns}
        except:
            return f'Table {table_name} not found'

    def get_data(self, table_name, where=None):
        column_names = []
        for column in self.list_columns(table_name)['columns']:
            column_names.append(column.column_name)

        query = f'SELECT * FROM {self.warehouse_name}.{table_name}'
        self.cursor.execute(apply_wheres(query, where))
        results = self.cursor.fetchall()
        rows = []
        for result in results:
            rows.append(RowData(result, column_names))

        return rows


connector = SNOWFLAKE_CONNECTOR()
