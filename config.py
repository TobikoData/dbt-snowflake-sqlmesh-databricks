from pathlib import Path
import os

from sqlmesh.dbt.loader import sqlmesh_config
from sqlmesh.core.config import (
    GatewayConfig,
    ModelDefaultsConfig,
    DatabricksConnectionConfig,
    DuckDBConnectionConfig
)

# databricks
config = sqlmesh_config(
    project_root=Path(__file__).parent,
    gateways={
        "": GatewayConfig(
            connection=DatabricksConnectionConfig(
                server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                http_path=os.getenv("DATABRICKS_HTTP_PATH"),
                access_token=os.getenv("DATABRICKS_ACCESS_TOKEN"),
                catalog="migrate_demo",
            ),
            state_connection=DuckDBConnectionConfig( # TODO: in a production setting, you'll use Tobiko Cloud or postgres
                database="sqlmesh_state_snowbricks_demo.duckdb",
            ),
        )
    },
)


# bonus: bigquery
# config = sqlmesh_config(
#     project_root=Path(__file__).parent,
#     state_connection=PostgresConnectionConfig(
#         host=os.getenv("SQLMESH_STATE_HOST"),
#         port=5432,
#         user=os.getenv("SQLMESH_STATE_USERNAME"),
#         password=os.getenv("SQLMESH_STATE_PASSWORD"),
#         database="sqlmesh_state_migrate_bigquery_demo",
#     ),
# )
