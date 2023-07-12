# Motherduck Demo

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.


### Let's get started!

> Note: I leave out detailed steps in uploading csv files. I simply uploaded the seed csv files in this dbt project and played around with it on neon.

1. Setup your neon account: https://neon.tech/docs/tutorial/project-setup
2. Setup your S3 bucket: https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html
3. Setup your motherduck account: https://motherduck.com/

Set your environment variables:

```shell
# all examples are fake
export motherduck_token=<your motherduck token> # aouiweh98229g193g1rb9u1
export NEON_PROJECT_ID=<your project id # empty-grass-954313
export NEON_API_KEY=<your api key> # hauwef9821371
export HOST=<host url> # ep-shrill-meadow-043325-pooler.us-west-2.aws.neon.tech
export ROLE=<username> # sungwonchung3
export PASSWORD=<passowrd> # aweufhawoi
export DBNAME=neondb

export S3_ACCESS_KEY_ID=<your access key id> # haoiwehfpoiahpwohf
export S3_SECRET_ACCESS_KEY=<your secret access key> # jiaowhefa998333
```

Update your `profiles.yml` file:

```yaml
jaffle_shop:

  target: dev
  outputs:
    dev:
      type: duckdb
      schema: dev_sung # update this for your own schema
      path: 'jaffle_shop.duckdb'
      threads: 16

    prod:
      type: duckdb
      schema: prod_sung # update this for your own schema
      path: 'md:jaffle_shop'
      threads: 16

    insane_o_style:
      type: duckdb
      schema: insane_o_style
      path: 'md:jaffle_shop'
      threads: 16
      extensions:
        - httpfs
      settings:
        s3_region: us-west-1 # update this for your own AWS region
        s3_access_key_id: "{{ env_var('S3_ACCESS_KEY_ID') }}"
        s3_secret_access_key: "{{ env_var('S3_SECRET_ACCESS_KEY') }}"
      plugins:
        - module: postgres
          config:
            dsn: "dbname={{ env_var('DBNAME') }} user={{ env_var('ROLE') }} host={{ env_var('HOST') }} password={{ env_var('PASSWORD') }} port=5432"
            source_schema: dbt_sung_dev # update this for your own schema
            sink_schema: plugin_postgres
            overwrite: true
```

Run it all:

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
dbt build -t insane_o_style
```

> Note: the rest of this is the original README.md file from the dbt-labs/jaffle_shop_duckdb repo

### What is this repo?
What this repo _is_:
- A self-contained playground dbt project, useful for testing out scripts, and communicating some of the core dbt concepts.

What this repo _is not_:
- A tutorial — check out the [Getting Started Tutorial](https://docs.getdbt.com/tutorial/setting-up) for that. Notably, this repo contains some anti-patterns to make it self-contained, namely the use of seeds instead of sources.
- A demonstration of best practices — check out the [dbt Learn Demo](https://github.com/dbt-labs/dbt-learn-demo) repo instead. We want to keep this project as simple as possible. As such, we chose not to implement:
    - our standard file naming patterns (which make more sense on larger projects, rather than this five-model project)
    - a pull request flow
    - CI/CD integrations
- A demonstration of using dbt for a high-complex project, or a demo of advanced features (e.g. macros, packages, hooks, operations) — we're just trying to keep things simple here!

### What's in this repo?
This repo contains [seeds](https://docs.getdbt.com/docs/building-a-dbt-project/seeds) that includes some (fake) raw data from a fictional app.

The raw data consists of customers, orders, and payments, with the following entity-relationship diagram:

![Jaffle Shop ERD](/etc/jaffle_shop_erd.png)

### Why should I care about this repo?
If you're just starting your cloud data warehouse journey and are hungry to get started with dbt before your organization officially gets a data warehouse, you should check out this repo.

If you want to run 28 SQL operations with dbt in less than `1 second`, for free, and all on your local machine, you should check out this repo.
![dbt_performance](images/dbt_performance.png)

If you want an adrenaline rush from a process that used to take dbt newcomers `1 hour` and is now less than `1 minute`, you should check out this repo.

![dbt_full_deploy_commands](images/dbt_full_deploy_commands.png)

[Verified GitHub Action on dbt Performance](https://github.com/dbt-labs/jaffle_shop_duckdb/runs/7141529753?check_suite_focus=true#step:4:306)

### Running this project

**Mach Speed: No explanation needed**
> Run `dbt` as fast as possible in a single copy and paste motion!

```shell
git clone https://github.com/dbt-labs/jaffle_shop_duckdb.git
cd jaffle_shop_duckdb
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
dbt build
dbt docs generate
dbt docs serve
```

Prerequisities: Python >= 3.5

To get up and running with this project:

1. Clone this repository.

1. Change into the `jaffle_shop_duck` directory from the command line:
    ```shell
    cd jaffle_shop_duckdb
    ```

1. Install dbt and DuckDB in a virtual environment.

    Expand your shell below:

    <details>
    <summary>POSIX bash/zsh</summary>

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    venv/bin/python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    source venv/bin/activate
    ```
    </details>

    <details>
    <summary>POSIX fish</summary>

    ```shell
    python3 -m venv venv
    source venv/bin/activate.fish
    venv/bin/python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    source venv/bin/activate.fish
    ```
    </details>

    <details>
    <summary>POSIX csh/tcsh</summary>

    ```shell
    python3 -m venv venv
    source venv/bin/activate.csh
    venv/bin/python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    source venv/bin/activate.csh
    ```
    </details>

    <details>
    <summary>POSIX PowerShell Core</summary>

    ```shell
    python3 -m venv venv
    venv/bin/Activate.ps1
    venv/bin/python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
    venv/bin/Activate.ps1
    ```
    </details>

    <details>
    <summary>Windows cmd.exe</summary>

    ```shell
    python -m venv venv
    venv\Scripts\activate.bat
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    venv\Scripts\activate.bat
    ```
    </details>

    <details>
    <summary>Windows PowerShell</summary>

    ```shell
    python -m venv venv
    venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    venv\Scripts\Activate.ps1
    ```
    </details>

    *Why a 2nd activation of the virtual environment?*
    <details>
    <summary>This may not be necessary for many users, but might be for some. Read on for a first-person report from @dbeatty10.</summary>

    I use `zsh` as my shell on my MacBook Pro, and I use `pyenv` to manage my Python environments. I already had an alpha version of dbt Core 1.2 installed (and yet another via [pipx](https://pypa.github.io/pipx/installation/)):
    ```shell
    $ which dbt
    /Users/dbeatty/.pyenv/shims/dbt
    ```
    ```shell
    $ dbt --version
    Core:
      - installed: 1.2.0-a1
      - latest:    1.1.1    - Ahead of latest version!

    Plugins:
      - bigquery:  1.2.0a1 - Ahead of latest version!
      - snowflake: 1.2.0a1 - Ahead of latest version!
      - redshift:  1.2.0a1 - Ahead of latest version!
      - postgres:  1.2.0a1 - Ahead of latest version!
    ```

    Then I ran all the steps to create a virtual environment and install the requirements of our DuckDB-based Jaffle Shop repo:
    ```shell
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ venv/bin/python3 -m pip install --upgrade pip
    (venv) $ python3 -m pip install -r requirements.txt
    ```

    Let's examine where `dbt` is installed and which version it is reporting:
    ```shell
    (venv) $ which dbt
    /Users/dbeatty/projects/jaffle_duck/venv/bin/dbt
    ```

    ```shell
    (venv) $ dbt --version
    Core:
      - installed: 1.2.0-a1
      - latest:    1.1.1    - Ahead of latest version!

    Plugins:
      - bigquery:  1.2.0a1 - Ahead of latest version!
      - snowflake: 1.2.0a1 - Ahead of latest version!
      - redshift:  1.2.0a1 - Ahead of latest version!
      - postgres:  1.2.0a1 - Ahead of latest version!
    ```

    ❌ That isn't what we expected -- something isn't right. 😢

    So let's reactivate the virtual environment and try again...
    ```shell
    (venv) $ source venv/bin/activate
    ```

    ```shell
    (venv) $ dbt --version
    Core:
      - installed: 1.1.1
      - latest:    1.1.1 - Up to date!

    Plugins:
      - postgres: 1.1.1 - Up to date!
      - duckdb:   1.1.3 - Up to date!
    ```

    ✅ This is what we want -- the 2nd reactivation worked. 😎 
    </details>

1. Ensure your [profile](https://docs.getdbt.com/reference/profiles.yml) is setup correctly from the command line:
    ```shell
    dbt --version
    dbt debug
    ```

1. Load the CSVs with the demo data set, run the models, and test the output of the models using the [dbt build](https://docs.getdbt.com/reference/commands/build) command:
    ```shell
    dbt build
    ```

1. Query the data:

    Launch a DuckDB command-line interface (CLI):
    ```shell
    duckcli jaffle_shop.duckdb
    ```

    Run a query at the prompt and exit:
    ```
    select * from customers where customer_id = 42;
    exit;
    ```

    Alternatively, use a single-liner to perform the query:
    ```shell
    duckcli jaffle_shop.duckdb -e "select * from customers where customer_id = 42"
    ```
    or:
    ```shell
    echo 'select * from customers where customer_id = 42' | duckcli jaffle_shop.duckdb
    ```

1. Generate and view the documentation for the project:
    ```shell
    dbt docs generate
    dbt docs serve
    ```

### Running `build` steps independently

1. Load the CSVs with the demo data set. This materializes the CSVs as tables in your target schema. Note that a typical dbt project **does not require this step** since dbt assumes your raw data is already in your warehouse.
    ```shell
    dbt seed
    ```

1. Run the models:
    ```shell
    dbt run
    ```

    > **NOTE:** If you decide to run this project in your own data warehouse (outside of this DuckDB demo) and steps fail, it might mean that you need to make small changes to the SQL in the models folder to adjust for the flavor of SQL of your target database. Definitely consider this if you are using a community-contributed adapter.

1. Test the output of the models using the [test](https://docs.getdbt.com/reference/commands/test) command:
    ```shell
    dbt test
    ```

### Browsing the data
Some options:
- [duckcli](https://pypi.org/project/duckcli/)
- [DuckDB CLI](https://duckdb.org/docs/installation/?environment=cli)
- [How to set up DBeaver SQL IDE for DuckDB](https://duckdb.org/docs/guides/sql_editors/dbeaver)

#### Troubleshooting

You may get an error like this, in which case you will need to disconnect from any sessions that are locking the database:
```
IO Error: Could not set lock on file "jaffle_shop.duckdb": Resource temporarily unavailable
```

This is a known issue in DuckDB. If you are using DBeaver, this means shutting down DBeaver (merely disconnecting didn't work for me).

Very worst-case, deleting the database file will get you back in action (BUT you will lose all your data).

---
For more information on dbt:
- Read the [introduction to dbt](https://docs.getdbt.com/docs/introduction)
- Read the [dbt viewpoint](https://docs.getdbt.com/docs/about/viewpoint)
- Join the [dbt Community](http://community.getdbt.com/)