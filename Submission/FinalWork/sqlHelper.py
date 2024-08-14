import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd
import calendar
class SQLHelper:
    def __init__(self):
        # Initialize the engine and base
        self.engine = create_engine("sqlite:///storms_final.sqlite")
        self.Base = None
        self.Session = sessionmaker(bind=self.engine)
        self.init_base()
    def init_base(self):
        # Prepare the base for reflecting existing tables
        self.Base = automap_base()
        self.Base.prepare(autoload_with=self.engine)
    def query_storms_by_month(self):
        query = """
        SELECT
            month,
            COUNT(*) AS storm_count
        FROM storm_data
        GROUP BY month
        ORDER BY month;
        """
        with self.Session() as session:
            df = pd.read_sql_query(query, self.engine)
        # Convert month numbers to month names
        df['month_name'] = df['month'].apply(lambda x: calendar.month_name[x])
        result = {
            'labels': df['month_name'].tolist(),
            'values': df['storm_count'].tolist()
        }
        return result
    def query_hurricane_number_bar(self):
        query = """
        SELECT
            category,
            COUNT(*) AS number_of_hurricanes
        FROM storm_data
        WHERE status = 'hurricane'
        GROUP BY category
        ORDER BY category;
        """
        with self.Session() as session:
            df = pd.read_sql_query(query, self.engine)
        result = {
            'categories': df['category'].tolist(),
            'number_of_hurricanes': df['number_of_hurricanes'].tolist()
        }
        return result
    def query_hurricane_by_decade(self):
        query = """
        SELECT
            FLOOR(year / 10) * 10 AS decade_start,
            category,
            COUNT(*) AS hurricane_count
        FROM storm_data
        WHERE status = 'hurricane'
            AND year BETWEEN 1852 AND 2021
        GROUP BY
            FLOOR(year / 10) * 10,
            category
        ORDER BY
            decade_start,
            category;
        """
        with self.Session() as session:
            df = pd.read_sql_query(query, self.engine)
        # Pivot the data for stacked bar chart
        df_pivot = df.pivot(index='decade_start', columns='category', values='hurricane_count').fillna(0)
        # Convert DataFrame to dictionary format suitable for plotting
        result = {
            'decades': df_pivot.index.tolist(),
            'categories': df_pivot.columns.tolist(),
            'data': df_pivot.to_dict(orient='list')
        }
        return result