
import pandas as pd
df = pd.read_csv(r"C:\Users\nares\Downloads\customer_shopping_behavior.csv")
print(df.info())
print(df.describe(include="all"))
print(df.isnull().sum())
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(lambda x: x.fillna(x.median()))
print(df.isnull().sum())
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})
print(df.columns)
#create a column age_group
labels = ["Young Adult", "Adult", "Middle-aged","Senior"]
df["age_group"] = pd.qcut(df["age"], q=4, labels =labels)
print(df[["age", "age_group"]].head(10))
#create column purchase_frequency_days
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Anually": 365,
    "Every 3 months": 90
}
df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)
print(df[["purchase_frequency_days", "frequency_of_purchases"]].head(10))
print(df[["discount_applied", "promo_code_used"]].head(10))
print((df["discount_applied"] ==df["promo_code_used"]).all())
df = df.drop("promo_code_used", axis=1)
print(df.columns)

from sqlalchemy import create_engine
# Define variables properly
host = "localhost"
port = "5432"
database = "demo"
username = "postgres"
password = "admin"

# Create engine
engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Insert dataframe
df.to_sql("customer", engine, if_exists="replace", index=False)
print("Data inserted successfully!")


  
  
