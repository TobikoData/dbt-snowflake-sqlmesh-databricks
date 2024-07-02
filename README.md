# dbt Snowflake -> SQLMesh Databricks

Migrations are hard. I know it very deeply. I've had my fair share of data warehouse migrations during my consulting days. What's really wonderful is that we believe they shouldn't be so miserable. 

This is a demo project to show you how easy it is to migrate to SQLMesh AND a new data platform in 5 minutes (literally). This is not meant to be exhaustive. This is a starting point to show you what's possible. And that hopefully for all of us, migrations don't have to be so miserable anymore. 


## Setup

```bash
# create a virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
source venv/bin/activate
```

Update your `dbt_project.yaml` for a SQLMesh project start date

```yaml
models:
  +start: Jan 1 2000
```

TODO Instructions:
- set env vars for profiles
- setup state postgres(copy instructions from my original demo)
- dbt build first
- sqlmesh plan after
- sqlmesh run from there
- sqlmesh audit to see how testing feels