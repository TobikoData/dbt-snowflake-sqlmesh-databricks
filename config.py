from pathlib import Path
import os

from sqlmesh.dbt.loader import sqlmesh_config
from sqlmesh.core.config import PostgresConnectionConfig

# databricks
# config = sqlmesh_config(
#     project_root=Path(__file__).parent,
#     state_connection=PostgresConnectionConfig(
#         host=os.getenv("SQLMESH_STATE_HOST"),
#         port=5432,
#         user=os.getenv("SQLMESH_STATE_USERNAME"),
#         password=os.getenv("SQLMESH_STATE_PASSWORD"),
#         database="sqlmesh_state_snowbricks_demo",
#     ),
# )

# bigquery
config = sqlmesh_config(
    project_root=Path(__file__).parent,
    state_connection=PostgresConnectionConfig(
        host=os.getenv("SQLMESH_STATE_HOST"),
        port=5432,
        user=os.getenv("SQLMESH_STATE_USERNAME"),
        password=os.getenv("SQLMESH_STATE_PASSWORD"),
        database="sqlmesh_state_migrate_bigquery_demo",
    ),
)

# yaml equivalent
# state_connection:
#     type: postgres
#     host: {{ env_var('SQLMESH_STATE_HOST') }}
#     port: 5432
#     user: {{ env_var('SQLMESH_STATE_USERNAME') }}
#     password: {{ env_var('SQLMESH_STATE_PASSWORD') }}
#     database: sqlmesh_state_snowbricks_demo
