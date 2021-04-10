import sqlite3
import pandas as pd

conn = sqlite3.connect('H:/Proyectos/Programacion/Django/Django_GraphQL/gqlproject/db.sqlite3')
df = pd.read_csv('H:/Proyectos/Programacion/Django/Django_GraphQL/sam.csv')
df['id'] = df.index
df = df[['id', 'Segment', 'Country', 'Product', 'Units', 'Sales', 'Datesold']]
df.to_sql('gql_app_productmodel', conn, if_exists='replace', index=False)
