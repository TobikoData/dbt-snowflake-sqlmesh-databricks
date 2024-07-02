import duckdb

con = duckdb.connect('md:')

# connect to your MotherDuck database through 'md:mydatabase' or 'motherduck:mydatabase'
# if the database doesn't exist, MotherDuck creates it when you connect
con = duckdb.connect('md:mydatabase')

# run a query to check verify that you are connected
con.sql("SHOW DATABASES").show()