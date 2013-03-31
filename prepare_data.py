# Preparacion de la Data a utilizar en el ejemplo

from sqlalchemy import create_engine
from cubes.tutorial.sql import create_table_from_csv

# 1. Preparando la data SQL en memoria

FACT_TABLE = "fact_ventas"

print "[fact_ventas][INICIO] Preparacion de Datos..."

engine = create_engine('sqlite:///data.sqlite')

create_table_from_csv(engine,
                      "fact_ventas.csv",
                      table_name=FACT_TABLE,
                      fields=[("vendedor", "string"),
                              ("cliente", "string"),
                              ("indicador", "string"),
                              ("valor", "integer"),
                              ("fecha", "date"),
                              ("tipo", "string")],
                      create_id=True
                      )

print "[fact_ventas][FIN] archivo data.sqlite creado"
