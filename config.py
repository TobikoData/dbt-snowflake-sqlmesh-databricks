from pathlib import Path
import os

from sqlmesh.dbt.loader import sqlmesh_config
from sqlmesh.core.config import (
    GatewayConfig,
    ModelDefaultsConfig,
    PostgresConnectionConfig,
    DatabricksConnectionConfig,
)

# databricks
config = sqlmesh_config(
    project_root=Path(__file__).parent,
    model_defaults=ModelDefaultsConfig(dialect='databricks'), # renders spark sql
    gateways={
        "": GatewayConfig(
            connection=DatabricksConnectionConfig(
                server_hostname="dbc-b9f590c4-0a08.cloud.databricks.com",
                http_path="/sql/protocolv1/o/5705746990502068/0603-211256-ns7ii2e2",
                access_token=os.getenv("DATABRICKS_ACCESS_TOKEN"),
                catalog="migrate_demo",
            ),
            state_connection=PostgresConnectionConfig(
                host=os.getenv("SQLMESH_STATE_HOST"),
                port=5432,
                user=os.getenv("SQLMESH_STATE_USERNAME"),
                password=os.getenv("SQLMESH_STATE_PASSWORD"),
                database="sqlmesh_state_snowbricks_demo",
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
