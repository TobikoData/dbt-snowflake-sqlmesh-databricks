
-- Add pre-hook configuration
{{ config(
  pre_hook="install postgres_scanner; load postgres_scanner;"
) }}

SELECT *
FROM POSTGRES_SCAN(
  "dbname={{ env_var('DBNAME') }} user={{ env_var('ROLE') }} host={{ env_var('HOST') }} password={{ env_var('PASSWORD') }}",
  "dbt_sung_dev",
  "customers"
)
