{% if target.name == 'dev_public_s3' %}

SELECT * FROM 's3://us-prd-motherduck-open-datasets/jaffle_shop/csv/raw_customers.csv'

{% else %}

select 1 as id

{% endif %}