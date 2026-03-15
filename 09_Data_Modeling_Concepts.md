# Data Modeling - Data Engineer Interview Guide

## Table of Contents
1. [Star Schema vs Snowflake Schema](#star-schema-vs-snowflake-schema)
2. [Normalization](#normalization)
3. [Fact Tables vs Dimension Tables](#fact-tables-vs-dimension-tables)
4. [Slowly Changing Dimensions (SCD)](#slowly-changing-dimensions-scd)
5. [Data Vault Modeling](#data-vault-modeling)
6. [Kimball vs Inmon](#kimball-vs-inmon)
7. [Surrogate Keys](#surrogate-keys)
8. [Conformed Dimensions](#conformed-dimensions)
9. [Junk Dimensions](#junk-dimensions)
10. [Degenerate Dimensions](#degenerate-dimensions)

---

## Star Schema vs Snowflake Schema

### Star Schema
```
         Dimension_Product
                |
                |
Dimension_Time -- FACT_Sales -- Dimension_Customer
                |
                |
         Dimension_Store
```

**Characteristics:**
- Denormalized dimension tables
- Single level of dimensions
- Simpler queries (fewer joins)
- Better query performance
- More storage due to redundancy
- Easier to understand and maintain

**Example:**
```sql
-- Fact Table
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    store_key INT,
    quantity INT,
    amount DECIMAL(10,2),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (customer_key) REFERENCES dim_customer(customer_key),
    FOREIGN KEY (store_key) REFERENCES dim_store(store_key)
);

-- Dimension Table (Denormalized)
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    subcategory VARCHAR(50),
    brand VARCHAR(50),
    supplier_name VARCHAR(100),
    supplier_country VARCHAR(50)
);
```

### Snowflake Schema
```
                    Dimension_Subcategory
                            |
         Dimension_Category |
                |           |
                |    Dimension_Product
                |           |
Dimension_Time -- FACT_Sales -- Dimension_Customer -- Dimension_City
                |                                           |
         Dimension_Store                          Dimension_State
```

**Characteristics:**
- Normalized dimension tables
- Multiple levels of dimensions
- More complex queries (more joins)
- Slower query performance
- Less storage (no redundancy)
- Better data integrity

**Example:**
```sql
-- Normalized Product Dimension
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    subcategory_key INT,
    FOREIGN KEY (subcategory_key) REFERENCES dim_subcategory(subcategory_key)
);

CREATE TABLE dim_subcategory (
    subcategory_key INT PRIMARY KEY,
    subcategory_name VARCHAR(50),
    category_key INT,
    FOREIGN KEY (category_key) REFERENCES dim_category(category_key)
);

CREATE TABLE dim_category (
    category_key INT PRIMARY KEY,
    category_name VARCHAR(50)
);
```

---

## Normalization

### Normal Forms

**1NF (First Normal Form):**
- Atomic values (no repeating groups)
- Each column contains single value
- Each row is unique

```sql
-- Not in 1NF
CREATE TABLE orders_bad (
    order_id INT,
    customer_name VARCHAR(100),
    products VARCHAR(500)  -- 'Product1, Product2, Product3'
);

-- In 1NF
CREATE TABLE orders (
    order_id INT,
    customer_name VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INT,
    product_name VARCHAR(100)
);
```

**2NF (Second Normal Form):**
- Must be in 1NF
- No partial dependencies (all non-key attributes depend on entire primary key)

```sql
-- Not in 2NF (partial dependency)
CREATE TABLE order_items_bad (
    order_id INT,
    product_id INT,
    product_name VARCHAR(100),  -- Depends only on product_id
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

-- In 2NF
CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100)
);
```

**3NF (Third Normal Form):**
- Must be in 2NF
- No transitive dependencies (non-key attributes don't depend on other non-key attributes)

```sql
-- Not in 3NF (transitive dependency)
CREATE TABLE employees_bad (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT,
    department_name VARCHAR(100),  -- Depends on department_id
    department_location VARCHAR(100)  -- Depends on department_id
);

-- In 3NF
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INT
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    department_location VARCHAR(100)
);
```

**BCNF (Boyce-Codd Normal Form):**
- Must be in 3NF
- Every determinant is a candidate key

---

## Fact Tables vs Dimension Tables

### Fact Tables

**Characteristics:**
- Contains measurable, quantitative data (metrics)
- Foreign keys to dimension tables
- Large, grows quickly
- Narrow (few columns)
- Many rows

**Types of Facts:**
1. **Additive**: Can be summed across all dimensions (e.g., sales amount)
2. **Semi-Additive**: Can be summed across some dimensions (e.g., account balance)
3. **Non-Additive**: Cannot be summed (e.g., ratios, percentages)

**Example:**
```sql
CREATE TABLE fact_sales (
    sale_key BIGINT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    store_key INT,
    -- Additive facts
    quantity INT,
    sales_amount DECIMAL(10,2),
    cost_amount DECIMAL(10,2),
    profit_amount DECIMAL(10,2),
    -- Semi-additive facts
    inventory_level INT,
    -- Non-additive facts
    discount_percentage DECIMAL(5,2),
    profit_margin DECIMAL(5,2)
);
```

### Dimension Tables

**Characteristics:**
- Contains descriptive attributes
- Relatively static
- Smaller than fact tables
- Wide (many columns)
- Fewer rows

**Example:**
```sql
CREATE TABLE dim_customer (
    customer_key INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(200),
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    postal_code VARCHAR(20),
    customer_segment VARCHAR(50),
    registration_date DATE,
    effective_from DATE,
    effective_to DATE,
    is_current BOOLEAN
);
```

---

## Slowly Changing Dimensions (SCD)

### Type 0: Fixed Dimension
- Never changes
- Original value retained forever

```sql
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    day_of_week VARCHAR(10),
    month_name VARCHAR(10),
    year INT,
    quarter INT
);
```

### Type 1: Overwrite
- Update existing record
- No history maintained
- Simple, saves space

```sql
UPDATE dim_customer
SET 
    email = 'new.email@example.com',
    phone = '555-1234',
    updated_at = CURRENT_TIMESTAMP
WHERE customer_id = 123;
```

### Type 2: Add New Row
- Insert new record for changes
- Full history maintained
- Most common approach

```sql
CREATE TABLE dim_customer_scd2 (
    customer_key BIGINT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(200),
    effective_from DATE,
    effective_to DATE,
    is_current BOOLEAN,
    version INT
);

-- Insert new version
BEGIN TRANSACTION;

-- Expire current record
UPDATE dim_customer_scd2
SET 
    effective_to = CURRENT_DATE - 1,
    is_current = FALSE
WHERE customer_id = 123 AND is_current = TRUE;

-- Insert new record
INSERT INTO dim_customer_scd2 (
    customer_id, customer_name, email, phone, address,
    effective_from, effective_to, is_current, version
)
VALUES (
    123, 'John Doe', 'john.new@example.com', '555-9999', '123 New St',
    CURRENT_DATE, '9999-12-31', TRUE, 2
);

COMMIT;
```

### Type 3: Add New Column
- Add column for previous value
- Limited history (one previous value)

```sql
CREATE TABLE dim_customer_scd3 (
    customer_key INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    current_email VARCHAR(100),
    previous_email VARCHAR(100),
    email_change_date DATE
);

-- Update with previous value
UPDATE dim_customer_scd3
SET 
    previous_email = current_email,
    current_email = 'new.email@example.com',
    email_change_date = CURRENT_DATE
WHERE customer_id = 123;
```

### Type 4: History Table
- Separate table for historical data
- Current table has latest values

```sql
-- Current table
CREATE TABLE dim_customer_current (
    customer_key INT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- History table
CREATE TABLE dim_customer_history (
    history_key BIGINT PRIMARY KEY,
    customer_key INT,
    customer_id INT,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    effective_from DATE,
    effective_to DATE
);
```

### Type 6: Hybrid (1+2+3)
- Combines Type 1, 2, and 3
- Current, previous, and historical values

```sql
CREATE TABLE dim_customer_scd6 (
    customer_key BIGINT PRIMARY KEY,
    customer_id INT,
    customer_name VARCHAR(100),
    current_email VARCHAR(100),
    historical_email VARCHAR(100),
    previous_email VARCHAR(100),
    effective_from DATE,
    effective_to DATE,
    is_current BOOLEAN
);
```

---

## Data Vault Modeling

Data Vault 2.0 is a modeling methodology for enterprise data warehouses.

### Components:

**1. Hubs** - Business keys
```sql
CREATE TABLE hub_customer (
    customer_hub_key BIGINT PRIMARY KEY,
    customer_id VARCHAR(50),
    load_date TIMESTAMP,
    record_source VARCHAR(50)
);
```

**2. Links** - Relationships between hubs
```sql
CREATE TABLE link_order (
    order_link_key BIGINT PRIMARY KEY,
    customer_hub_key BIGINT,
    product_hub_key BIGINT,
    order_date DATE,
    load_date TIMESTAMP,
    record_source VARCHAR(50)
);
```

**3. Satellites** - Descriptive attributes
```sql
CREATE TABLE sat_customer (
    customer_hub_key BIGINT,
    load_date TIMESTAMP,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address VARCHAR(200),
    hash_diff VARCHAR(32),
    record_source VARCHAR(50),
    PRIMARY KEY (customer_hub_key, load_date)
);
```

---

## Kimball vs Inmon

### Kimball (Bottom-Up)
- **Approach**: Dimensional modeling, star schema
- **Focus**: Business processes
- **Design**: Denormalized
- **Build**: Incremental, by business area
- **Time**: Faster to implement
- **Query**: Optimized for queries
- **Users**: Business users, analysts

### Inmon (Top-Down)
- **Approach**: Normalized, 3NF
- **Focus**: Enterprise-wide
- **Design**: Normalized
- **Build**: Complete enterprise model first
- **Time**: Longer to implement
- **Query**: More complex queries
- **Users**: IT, data stewards

---

## Surrogate Keys

Artificial keys with no business meaning.

**Benefits:**
- Performance (integer vs string)
- Consistency across systems
- Handles changes in natural keys
- Simplifies SCD Type 2

**Example:**
```sql
CREATE TABLE dim_product (
    product_key INT PRIMARY KEY,  -- Surrogate key
    product_id VARCHAR(50),        -- Natural/business key
    product_name VARCHAR(100),
    category VARCHAR(50)
);
```

---

## Conformed Dimensions

Dimensions shared across multiple fact tables.

**Example:**
```sql
-- Shared dimension
CREATE TABLE dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE,
    year INT,
    quarter INT,
    month INT,
    day INT
);

-- Used by multiple facts
CREATE TABLE fact_sales (
    sale_key BIGINT PRIMARY KEY,
    date_key INT,
    -- other columns
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);

CREATE TABLE fact_inventory (
    inventory_key BIGINT PRIMARY KEY,
    date_key INT,
    -- other columns
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key)
);
```

---

## Junk Dimensions

Combines low-cardinality flags and indicators.

**Example:**
```sql
-- Instead of multiple flag columns in fact
CREATE TABLE dim_transaction_flags (
    flag_key INT PRIMARY KEY,
    is_online BOOLEAN,
    is_gift BOOLEAN,
    is_express_shipping BOOLEAN,
    is_promotional BOOLEAN
);

CREATE TABLE fact_sales (
    sale_key BIGINT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    flag_key INT,  -- Reference to junk dimension
    amount DECIMAL(10,2)
);
```

---

## Degenerate Dimensions

Dimension attributes stored in fact table (no separate dimension table).

**Example:**
```sql
CREATE TABLE fact_sales (
    sale_key BIGINT PRIMARY KEY,
    date_key INT,
    product_key INT,
    customer_key INT,
    order_number VARCHAR(50),  -- Degenerate dimension
    invoice_number VARCHAR(50), -- Degenerate dimension
    quantity INT,
    amount DECIMAL(10,2)
);
```

---

## Best Practices

1. **Use surrogate keys** for all dimensions
2. **Implement SCD Type 2** for tracking history
3. **Create conformed dimensions** for consistency
4. **Denormalize for performance** in dimensional models
5. **Use date dimension** for all time-based analysis
6. **Keep fact tables narrow** (only keys and measures)
7. **Make dimensions wide** (all descriptive attributes)
8. **Use junk dimensions** for flags and indicators
9. **Document grain** of each fact table
10. **Maintain referential integrity** with foreign keys

---

**End of Data Modeling Guide**
