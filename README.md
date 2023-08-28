# Motherduck Blog Demo

`jaffle_shop` is a fictional ecommerce store. This dbt project transforms raw data from an app database into a customers and orders model ready for analytics.


### Let's get started!

1. Setup your motherduck account: https://motherduck.com/
2. Setup your S3 bucket: https://docs.aws.amazon.com/AmazonS3/latest/userguide/GetStartedWithS3.html

Set your environment variables:

```shell
# all examples are fake
export motherduck_token=<your motherduck token> # aouiweh98229g193g1rb9u1
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
      schema: dev_sung
      path: 'md:jaffle_shop'
      threads: 16
      extensions: 
        - httpfs
      settings:
        s3_region: us-west-1
        s3_access_key_id: "{{ env_var('S3_ACCESS_KEY_ID') }}"
        s3_secret_access_key: "{{ env_var('S3_SECRET_ACCESS_KEY') }}"

    prod:
      type: duckdb
      schema: prod_sung
      path: 'md:jaffle_shop'
      threads: 16
      extensions: 
        - httpfs
      settings:
        s3_region: us-west-1
        s3_access_key_id: "{{ env_var('S3_ACCESS_KEY_ID') }}"
        s3_secret_access_key: "{{ env_var('S3_SECRET_ACCESS_KEY') }}"
```

Run it all:

```shell
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
source venv/bin/activate
dbt debug
dbt build
```