import pandas as pd
import numpy as np
from pathlib import Path

rng = np.random.default_rng(100)

reference_dir = Path("C:\\Users\\Utkarsh\\Desktop\\Data Projects\\ai_fintech\\data\\generation_reference_data")

# 1. Read the reference data

customers = pd.read_csv(reference_dir / "customers.csv",
                        parse_dates=["signup_date"])

merchants = pd.read_csv(reference_dir / "merchants.csv")

# 2.Generate Transactions data

n_transactions = 15000

# Generate transaction ids

transaction_ids = [f"TXN{i:08d}" 
                   for i in range(1, n_transactions + 1)]

# 3. Select existing customer and merchant ids

customer_indices = rng.integers(
    0, len(customers), size=n_transactions
)

selected_customer = customers.iloc[customer_indices].reset_index(drop=True)

# Merchants

merchant_indices = rng.integers(
    0, len(merchants), size=n_transactions
)

selected_merchant = merchants.iloc[merchant_indices].reset_index(drop=True)


# 4. Generate timstamps for transactions

signup_dates = selected_customer[
    "signup_date"].to_numpy(dtype = 'datetime64[ns]')

# Dynamic cutoff (End of today's date)

end_date = (
    np.
datetime64('today', 'D') 
+ np.timedelta64(1, 'D')
- np.timedelta64(1, 's')
)

# Calculate available seconds from signup date to cutoff date (end date)

available_seconds = (
    (end_date - signup_dates)
    / np.timedelta64(1, "s")
).astype("int64")


# Validate signup dates

if (available_seconds < 0).any():
    raise ValueError(
        "Customers have signup dates after the transaction cutoff date. Please check the data."

    )

# Generate random transactio  times

random_seconds = np.array([
    rng.integers(0, seconds + 1) 
    for seconds in available_seconds
])

# Create transaction timestamps 

transaction_timestamps = pd.to_datetime(
    
    signup_dates + random_seconds.astype("timedelta64[s]")
)


# 5. Generate transaction amounts

