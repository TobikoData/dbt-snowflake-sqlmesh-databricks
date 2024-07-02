
select * from {{ source('plugin_postgres', 'customers') }}