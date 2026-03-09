import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic data for 1000 customers
n_customers = 1000

data = {
    "customer_id": range(1001, 1001 + n_customers),
    "avg_spend_per_visit": np.random.uniform(10, 100, n_customers),
    "visit_frequency_per_month": np.random.poisson(3, n_customers),
    "menu_engagement_score": np.random.uniform(
        1, 10, n_customers
    ),  # High score = tries new items
    "online_order_ratio": np.random.beta(
        2, 5, n_customers
    ),  # Higher means more online vs in-store
    "loyalty_years": np.random.randint(0, 10, n_customers),
}

df = pd.DataFrame(data)

# Define "High-Value" (Target): Spending > $60 AND frequent visits OR long loyalty
df["is_high_value"] = (
    (df["avg_spend_per_visit"] > 60) & (df["visit_frequency_per_month"] > 3)
    | (df["loyalty_years"] > 7)
).astype(int)

# Save to CSV
df.to_csv("synthetic_retail_customers.csv", index=False)
print("File 'synthetic_retail_customers.csv' created successfully.")
