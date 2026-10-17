# Import Libraries
import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(42)

output_dir = Path("C:\\Users\\Utkarsh\\Desktop\\Data Projects\\ai_fintech\\data\\generation_reference_data")
output_dir.mkdir(parents=True, exist_ok=True)

# Generate Customers data
n_customers = 3000

customers = pd.DataFrame({
    'customer_id':[
        f"CUST{i:05d}" for i in range(1, n_customers + 1)
    ],
    'customer_segment': rng.choice(
        ['Standard', 'Premium', 'Business'], size=n_customers
    ),
    'signup_date' : pd.to_datetime(
        rng.choice(
            pd.date_range("2023-01-01", "2026-10-01"),
            size=n_customers
        )
    ),
     'country': rng.choice(
        ["GB"],
        size=n_customers
    ),
    'customer_status': rng.choice(
        ["Active", "Inactive", "Suspended"],
        size=n_customers
    )
})

# Merchants data

n_merchants = 250

merchants = pd.DataFrame({
    'merchant_id': [
        f"MERCH{i:04d}" for i in range(1, n_merchants + 1)
    ],
    'merchant_category': rng.choice(
        ['Fashion', 'Travel', 'Grocery', 'Electronics', 'Digital Services'], size=n_merchants
    ),
    'country': rng.choice(
        ["GB"],
        size=n_merchants
    ),
    'risk_segment': rng.choice(
        ["Low", "Medium", "High"],
        size=n_merchants,
        p=[0.6, 0.3, 0.1]
    )
})


# Save the cleaned generated data

customers.to_csv(output_dir / "customers.csv", index=False)
merchants.to_csv(output_dir / "merchants.csv", index=False)


# Initial data validation

assert customers['customer_id'].is_unique, "Customer IDs are not unique"
assert merchants['merchant_id'].is_unique, "Merchant IDs are not unique"


print("Customers:",customers.shape)
print("Merchants:",merchants.shape)
print("Data generation completed successfully. Files saved in:", output_dir)

