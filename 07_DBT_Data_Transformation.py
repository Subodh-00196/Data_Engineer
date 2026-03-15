"""
================================================================================
                    DBT - DATA ENGINEER INTERVIEW GUIDE
================================================================================
dbt (Data Build Tool) concepts and examples for Data Engineering interviews
Last Updated: March 2026
================================================================================

TABLE OF CONTENTS:
1. DBT BASICS & CONCEPTS
2. SOURCES
3. MODELS (STAGING, INTERMEDIATE, MARTS)
4. MATERIALIZATIONS
5. TESTS (GENERIC & CUSTOM)
6. MACROS
7. INCREMENTAL MODELS
8. SNAPSHOTS (SCD TYPE 2)
9. SEEDS
10. DOCUMENTATION
11. DBT PROJECT STRUCTURE
12. BEST PRACTICES
================================================================================
"""

# ============================================================================
# 1. DBT BASICS & CONCEPTS
# ============================================================================

"""
DBT (Data Build Tool) is a transformation tool that enables data analysts and 
engineers to transform data in their warehouse more effectively.

KEY CONCEPTS:
- Models: SQL SELECT statements that define transformations
- Sources: Raw data tables in your warehouse
- Tests: Data quality checks
- Macros: Reusable SQL snippets (like functions)
- Materializations: How models are built (view, table, incremental, ephemeral)
- Seeds: CSV files loaded as tables
- Snapshots: Type 2 SCD implementation

DBT WORKFLOW:
1. Define sources (raw data)
2. Create staging models (clean, rename)
3. Create intermediate models (business logic)
4. Create mart models (final analytics tables)
5. Test data quality
6. Document models
7. Run: dbt run
8. Test: dbt test
"""

# ============================================================================
# 2. SOURCES
# ============================================================================

"""
Sources represent raw data tables in your data warehouse.
Defined in YAML files (typically sources.yml)
"""

# File: models/staging/sources.yml
"""
version: 2

sources:
  - name: raw_data
    database: my_database
    schema: public
    description: "Raw data from production database"
    tables:
      - name: customers
        description: "Raw customer data from CRM"
        columns:
          - name: customer_id
            description: "Unique ID for each customer"
            tests:
              - not_null
              - unique
          - name: name
            description: "Full name of the customer"
          - name: email
            description: "Customer email address"
            tests:
              - not_null
          - name: created_at
            description: "Account creation timestamp"
        
      - name: orders
        description: "Raw order data"
        loaded_at_field: updated_at
        freshness:
          warn_after: {count: 12, period: hour}
          error_after: {count: 24, period: hour}
        columns:
          - name: order_id
            tests:
              - not_null
              - unique
          - name: customer_id
            tests:
              - not_null
              - relationships:
                  to: source('raw_data', 'customers')
                  field: customer_id
"""

# ============================================================================
# 3. MODELS (STAGING, INTERMEDIATE, MARTS)
# ============================================================================

"""
STAGING MODELS:
- Clean and standardize raw data
- 1:1 with source tables
- Naming: stg_<source>_<table>
"""

# File: models/staging/stg_customers.sql
"""
-- Staging model for cleaned customer data
{{ config(materialized='view') }}

SELECT
    customer_id,
    TRIM(name) AS customer_name,
    LOWER(email) AS email,
    created_at,
    updated_at
FROM {{ source('raw_data', 'customers') }}
WHERE customer_id IS NOT NULL
"""

# File: models/staging/stg_customers.yml
"""
version: 2

models:
  - name: stg_customers
    description: "Staging model for cleaned customer data"
    columns:
      - name: customer_id
        description: "Unique ID for each customer"
        tests:
          - not_null
          - unique
      - name: customer_name
        description: "Cleaned customer name"
        tests:
          - not_null
      - name: email
        description: "Lowercase email address"
        tests:
          - not_null
"""

"""
INTERMEDIATE MODELS:
- Business logic transformations
- Join multiple staging models
- Naming: int_<entity>_<verb>
"""

# File: models/intermediate/int_customer_orders.sql
"""
{{ config(materialized='ephemeral') }}

SELECT
    c.customer_id,
    c.customer_name,
    c.email,
    COUNT(o.order_id) AS total_orders,
    SUM(o.order_amount) AS total_spent,
    MAX(o.order_date) AS last_order_date
FROM {{ ref('stg_customers') }} c
LEFT JOIN {{ ref('stg_orders') }} o 
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.customer_name, c.email
"""

"""
MART MODELS:
- Final analytics-ready tables
- Business-specific aggregations
- Naming: fct_<entity>, dim_<entity>
"""

# File: models/marts/fct_customer_metrics.sql
"""
{{ config(
    materialized='table',
    schema='analytics'
) }}

SELECT
    customer_id,
    customer_name,
    email,
    total_orders,
    total_spent,
    last_order_date,
    CASE
        WHEN total_spent > 1000 THEN 'High Value'
        WHEN total_spent > 500 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment,
    CURRENT_TIMESTAMP AS updated_at
FROM {{ ref('int_customer_orders') }}
"""

# ============================================================================
# 4. MATERIALIZATIONS
# ============================================================================

"""
VIEW (Default):
- Creates a database view
- No data stored, query runs each time
- Fast to build, slower to query
"""
# {{ config(materialized='view') }}

"""
TABLE:
- Creates a physical table
- Data stored in warehouse
- Slower to build, faster to query
"""
# {{ config(materialized='table') }}

"""
INCREMENTAL:
- Only processes new/changed records
- Efficient for large datasets
- Requires unique key
"""
# File: models/fct_events_incremental.sql
"""
{{ config(
    materialized='incremental',
    unique_key='event_id'
) }}

SELECT
    event_id,
    user_id,
    event_type,
    event_timestamp,
    properties
FROM {{ source('raw_data', 'events') }}

{% if is_incremental() %}
    WHERE event_timestamp > (SELECT MAX(event_timestamp) FROM {{ this }})
{% endif %}
"""

"""
EPHEMERAL:
- Not materialized in database
- CTE in dependent models
- Saves warehouse space
"""
# {{ config(materialized='ephemeral') }}

# ============================================================================
# 5. TESTS (GENERIC & CUSTOM)
# ============================================================================

"""
GENERIC TESTS (Built-in):
- unique
- not_null
- accepted_values
- relationships
"""

# In schema.yml
"""
models:
  - name: stg_customers
    columns:
      - name: customer_id
        tests:
          - not_null
          - unique
      
      - name: status
        tests:
          - accepted_values:
              values: ['active', 'inactive', 'pending']
      
      - name: country
        tests:
          - accepted_values:
              values: ['USA', 'India', 'UK']

  - name: stg_orders
    columns:
      - name: customer_id
        tests:
          - relationships:
              to: ref('stg_customers')
              field: customer_id
"""

"""
CUSTOM TESTS:
- SQL queries that return failing rows
- Stored in tests/ directory
"""

# File: tests/no_negative_order_amount.sql
"""
-- This test will fail if any orders have negative amounts
SELECT *
FROM {{ ref('stg_orders') }}
WHERE order_amount < 0
"""

# File: tests/no_future_orders.sql
"""
-- Orders should not be in the future
SELECT *
FROM {{ ref('stg_orders') }}
WHERE order_date > CURRENT_DATE
"""

"""
EXPRESSION TESTS:
"""
"""
columns:
  - name: discount
    tests:
      - dbt_utils.expression_is_true:
          expression: "discount >= 0 AND discount <= 100"
  
  - name: age
    tests:
      - dbt_utils.expression_is_true:
          expression: "age >= 0 AND age <= 120"
"""

# ============================================================================
# 6. MACROS
# ============================================================================

"""
Macros are reusable SQL snippets using Jinja templating.
Stored in macros/ directory.
"""

# File: macros/format_date.sql
"""
{% macro format_date(column) %}
    TO_CHAR({{ column }}, 'YYYY-MM-DD')
{% endmacro %}
"""

# Usage in model:
"""
SELECT
    customer_id,
    {{ format_date('order_date') }} AS formatted_order_date
FROM {{ ref('orders') }}
"""

# File: macros/cents_to_dollars.sql
"""
{% macro cents_to_dollars(column_name, scale=2) %}
    ROUND({{ column_name }} / 100.0, {{ scale }})
{% endmacro %}
"""

# File: macros/custom_schema.sql
"""
{% macro custom_schema_name() %}
    {% if target.name == 'prod' %}
        'production_schema'
    {% else %}
        'dev_schema'
    {% endif %}
{% endmacro %}
"""

# File: macros/generate_alias_name.sql
"""
{% macro generate_alias_name(custom_alias_name=none, node=none) -%}
    {%- if custom_alias_name is none -%}
        {{ node.name }}
    {%- else -%}
        {{ custom_alias_name | trim }}
    {%- endif -%}
{%- endmacro %}
"""

# File: macros/surrogate_key.sql
"""
{% macro surrogate_key(field_list) %}
    MD5(
        {% for field in field_list %}
            COALESCE(CAST({{ field }} AS VARCHAR), '')
            {% if not loop.last %}|| '|' ||{% endif %}
        {% endfor %}
    )
{% endmacro %}
"""

# Usage:
"""
SELECT
    {{ surrogate_key(['customer_id', 'order_date']) }} AS order_key,
    customer_id,
    order_date
FROM {{ ref('stg_orders') }}
"""

# ============================================================================
# 7. INCREMENTAL MODELS
# ============================================================================

"""
Incremental models only process new or changed data.
"""

# File: models/fct_daily_sales.sql
"""
{{ config(
    materialized='incremental',
    unique_key='sale_date',
    on_schema_change='fail'
) }}

SELECT
    DATE(order_timestamp) AS sale_date,
    COUNT(DISTINCT order_id) AS num_orders,
    SUM(order_amount) AS total_sales,
    COUNT(DISTINCT customer_id) AS unique_customers
FROM {{ ref('stg_orders') }}

{% if is_incremental() %}
    -- Only process new data
    WHERE DATE(order_timestamp) > (SELECT MAX(sale_date) FROM {{ this }})
{% endif %}

GROUP BY DATE(order_timestamp)
"""

"""
INCREMENTAL STRATEGIES:
1. append: Add new rows (default)
2. merge: Update existing, insert new (requires unique_key)
3. delete+insert: Delete matching, insert new
"""

# Merge strategy example:
"""
{{ config(
    materialized='incremental',
    unique_key='user_id',
    incremental_strategy='merge'
) }}

SELECT
    user_id,
    username,
    email,
    last_login,
    updated_at
FROM {{ source('raw_data', 'users') }}

{% if is_incremental() %}
    WHERE updated_at > (SELECT MAX(updated_at) FROM {{ this }})
{% endif %}
"""

# ============================================================================
# 8. SNAPSHOTS (SCD TYPE 2)
# ============================================================================

"""
Snapshots implement Type 2 Slowly Changing Dimensions.
Track historical changes to mutable tables.
"""

# File: snapshots/customers_snapshot.sql
"""
{% snapshot customers_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='customer_id',
      strategy='timestamp',
      updated_at='updated_at',
    )
}}

SELECT * FROM {{ source('raw_data', 'customers') }}

{% endsnapshot %}
"""

# Using check strategy (for tables without updated_at):
"""
{% snapshot orders_snapshot %}

{{
    config(
      target_schema='snapshots',
      unique_key='order_id',
      strategy='check',
      check_cols=['status', 'total_amount'],
    )
}}

SELECT * FROM {{ source('raw_data', 'orders') }}

{% endsnapshot %}
"""

# Snapshot creates these columns:
# - dbt_valid_from: When record became valid
# - dbt_valid_to: When record became invalid (NULL if current)
# - dbt_scd_id: Unique identifier for each version
# - dbt_updated_at: When snapshot was taken

# ============================================================================
# 9. SEEDS
# ============================================================================

"""
Seeds are CSV files in data/ directory.
Loaded as tables in warehouse.
Good for small lookup tables.
"""

# File: data/country_codes.csv
"""
country_code,country_name
US,United States
UK,United Kingdom
IN,India
"""

# Load seeds:
# dbt seed

# Reference in models:
"""
SELECT
    o.order_id,
    o.country_code,
    c.country_name
FROM {{ ref('stg_orders') }} o
LEFT JOIN {{ ref('country_codes') }} c
    ON o.country_code = c.country_code
"""

# ============================================================================
# 10. DOCUMENTATION
# ============================================================================

"""
Documentation is defined in YAML files and markdown.
"""

# File: models/schema.yml
"""
version: 2

models:
  - name: fct_customer_metrics
    description: |
      # Customer Metrics Fact Table
      
      This table contains aggregated metrics for each customer including:
      - Total number of orders
      - Total amount spent
      - Customer segment classification
      
      **Refresh Schedule:** Daily at 2 AM UTC
      
      **Data Quality:** All customers must have at least one order
    
    columns:
      - name: customer_id
        description: "Unique identifier for customer"
        tests:
          - not_null
          - unique
      
      - name: total_orders
        description: "Total number of orders placed by customer"
      
      - name: customer_segment
        description: |
          Customer value segment:
          - High Value: > $1000 total spent
          - Medium Value: $500-$1000 total spent
          - Low Value: < $500 total spent
"""

# Generate documentation site:
# dbt docs generate
# dbt docs serve

# ============================================================================
# 11. DBT PROJECT STRUCTURE
# ============================================================================

"""
my_dbt_project/
├── dbt_project.yml          # Project configuration
├── profiles.yml             # Database connection (in ~/.dbt/)
├── packages.yml             # dbt packages
├── models/
│   ├── staging/
│   │   ├── sources.yml
│   │   ├── stg_customers.sql
│   │   └── stg_orders.sql
│   ├── intermediate/
│   │   └── int_customer_orders.sql
│   └── marts/
│       ├── fct_customer_metrics.sql
│       └── dim_products.sql
├── macros/
│   ├── format_date.sql
│   └── cents_to_dollars.sql
├── tests/
│   ├── no_negative_amounts.sql
│   └── no_future_dates.sql
├── snapshots/
│   └── customers_snapshot.sql
├── data/
│   └── country_codes.csv
└── analyses/
    └── customer_analysis.sql
"""

# File: dbt_project.yml
"""
name: 'my_dbt_project'
version: '1.0.0'
config-version: 2

profile: 'my_profile'

model-paths: ["models"]
analysis-paths: ["analyses"]
test-paths: ["tests"]
seed-paths: ["data"]
macro-paths: ["macros"]
snapshot-paths: ["snapshots"]

target-path: "target"
clean-targets:
  - "target"
  - "dbt_packages"

models:
  my_dbt_project:
    staging:
      +materialized: view
      +schema: staging
    
    intermediate:
      +materialized: ephemeral
    
    marts:
      +materialized: table
      +schema: analytics
"""

# File: profiles.yml (in ~/.dbt/)
"""
my_profile:
  target: dev
  outputs:
    dev:
      type: snowflake
      account: my_account
      user: my_user
      password: my_password
      role: my_role
      database: dev_database
      warehouse: dev_warehouse
      schema: dev_schema
      threads: 4
    
    prod:
      type: snowflake
      account: my_account
      user: prod_user
      password: prod_password
      role: prod_role
      database: prod_database
      warehouse: prod_warehouse
      schema: prod_schema
      threads: 8
"""

# ============================================================================
# 12. BEST PRACTICES
# ============================================================================

"""
NAMING CONVENTIONS:
- Sources: raw_<source>_<table>
- Staging: stg_<source>_<table>
- Intermediate: int_<entity>_<verb>
- Facts: fct_<entity>
- Dimensions: dim_<entity>

MODEL ORGANIZATION:
1. Staging: Clean and standardize (1:1 with sources)
2. Intermediate: Business logic (ephemeral)
3. Marts: Analytics-ready (tables)

TESTING STRATEGY:
- Test all primary keys (unique, not_null)
- Test all foreign keys (relationships)
- Test business rules (custom tests)
- Test data freshness

INCREMENTAL MODELS:
- Use for large, append-only datasets
- Always specify unique_key
- Handle late-arriving data
- Test thoroughly

DOCUMENTATION:
- Document all models and columns
- Include business context
- Document assumptions
- Keep updated

MACROS:
- DRY principle (Don't Repeat Yourself)
- Reusable business logic
- Consistent transformations
- Version control

PERFORMANCE:
- Use appropriate materializations
- Partition large tables
- Use incremental models for large datasets
- Optimize SQL queries
- Use ephemeral for intermediate steps

DBT COMMANDS:
- dbt run: Build models
- dbt test: Run tests
- dbt run --select model_name: Run specific model
- dbt run --select +model_name: Run model and upstream
- dbt run --select model_name+: Run model and downstream
- dbt test --select model_name: Test specific model
- dbt docs generate: Generate documentation
- dbt docs serve: Serve documentation
- dbt seed: Load seed files
- dbt snapshot: Run snapshots
- dbt clean: Clean target directory
- dbt compile: Compile without running
- dbt debug: Debug connection
"""

# ============================================================================
# PYTHON MODELS IN DBT
# ============================================================================

"""
dbt supports Python models (dbt 1.3+)
"""

# File: models/python/customer_summary.py
"""
import pandas as pd

def model(dbt, session):
    # Configure materialization
    dbt.config(
        materialized="table",
        packages=["pandas"]
    )
    
    # Load source data
    customers_df = dbt.source("raw_data", "customers").to_pandas()
    orders_df = dbt.source("raw_data", "orders").to_pandas()
    
    # Perform transformation
    summary_df = orders_df.groupby("customer_id").agg({
        "order_id": "count",
        "order_amount": "sum"
    }).reset_index()
    
    summary_df.columns = ["customer_id", "total_orders", "total_spent"]
    
    # Join with customer data
    result_df = customers_df.merge(summary_df, on="customer_id", how="left")
    result_df["total_orders"] = result_df["total_orders"].fillna(0)
    result_df["total_spent"] = result_df["total_spent"].fillna(0)
    
    return result_df
"""

"""
================================================================================
END OF DBT INTERVIEW GUIDE
================================================================================
"""
