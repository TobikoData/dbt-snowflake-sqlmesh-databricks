{% if target.name == 'dev_public_s3' %}

select 1 as id

{% else %}

SELECT * FROM 's3://duckdb-demo/raw_customers.csv'

{% endif %}