
import click
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')


    # taxi_data_url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet'

    # df = pd.read_parquet(taxi_data_url)

    # print(df.head())

    # taxi_data_table = 'green_taxi_data'

    # df.head(0).to_sql(name=taxi_data_table, con=engine, if_exists='replace', index=False)
        
    # df.to_sql(name=taxi_data_table, con=engine, if_exists='append', index=False)


    zone_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv'

    zone_df = pd.read_csv(zone_url)

    zone_table = 'zones'

    zone_df.head(0).to_sql(name=zone_table, con=engine, if_exists='replace', index=False)

    zone_df.to_sql(name=zone_table, con=engine, if_exists='append', index=False)

if __name__ == '__main__':
    run()
