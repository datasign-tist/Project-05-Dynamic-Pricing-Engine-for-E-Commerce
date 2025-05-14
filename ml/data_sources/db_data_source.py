from ml.base.data_source import DataSource
import pandas as pd
import sqlalchemy

class PostgresSalesDataSource(DataSource):
    def __init__(self, connection_string):
        self.engine = sqlalchemy.create_engine(connection_string)

    def load_data(self) -> pd.DataFrame:
        query = """
        SELECT timestamp, product_id, region, units_sold, price, inventory
        FROM sales_data
        WHERE timestamp >= CURRENT_DATE - INTERVAL '365 days'
        """
        return pd.read_sql(query, self.engine)
