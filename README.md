# customer_shopping_behavior_analysis
📂 Project Structure
customer_shopping_behavior_analysis/
│── customer_shopping_behavior.csv   # Raw dataset
│── PG Local.session.sql             # SQL queries for analysis
│── customers.py                     # Python data processing script
│── customer_behavior_dashboard.pbix # Power BI dashboard
│── README.md                        # Project documentation
📊 Dataset Information
Dataset Name: Customer Shopping Behavior Dataset
Format: CSV
Records: Customer transactions data
🔗 Raw Dataset Link

If you want to download the dataset separately:
👉 https://www.kaggle.com/datasets (search: customer shopping behavior dataset)

🧾 Key Columns
customer_id – Unique customer identifier
gender – Male/Female
age_group – Age category
item_purchased – Product name
category – Product category
purchase_amount – Amount spent
review_rating – Product rating
shipping_type – Standard/Express
discount_applied – Yes/No
subscription_status – Subscribed/Not Subscribed
previous_purchases – Number of past purchases
⚙️ Tools & Technologies Used
SQL (PostgreSQL) – Data analysis
Python (Pandas) – Data loading & preprocessing
Power BI – Data visualization & dashboard
🧠 SQL Analysis & Solutions
Q1. Total revenue by gender
SELECT gender, SUM(purchase_amount) AS revenue
FROM customer
GROUP BY gender;

✔️ Insight: Helps compare spending behavior between male and female customers.

Q2. Customers who used discount but spent above average
SELECT customer_id, purchase_amount
FROM customer
WHERE discount_applied = 'Yes'
AND purchase_amount >= (
    SELECT AVG(purchase_amount) FROM customer
);

✔️ Insight: Identifies high-value customers even after discounts.

Q3. Top 5 products by average rating
SELECT item_purchased, ROUND(AVG(review_rating::numeric),2)
FROM customer
GROUP BY item_purchased
ORDER BY AVG(review_rating) DESC
LIMIT 5;

✔️ Insight: Highlights best-performing products.

Q4. Average purchase: Standard vs Express shipping
SELECT shipping_type, ROUND(AVG(purchase_amount),2)
FROM customer
WHERE shipping_type IN ('Standard', 'Express')
GROUP BY shipping_type;

✔️ Insight: Shows how shipping choice impacts spending.

Q5. Do subscribed customers spend more?
SELECT subscription_status,
COUNT(customer_id),
ROUND(AVG(purchase_amount),2),
ROUND(SUM(purchase_amount),2)
FROM customer
GROUP BY subscription_status;

✔️ Insight: Measures value of subscription model.

Q6. Products with highest discount usage %
SELECT item_purchased,
ROUND(SUM(CASE WHEN discount_applied='Yes' THEN 1 ELSE 0 END)/COUNT(*),2)
FROM customer
GROUP BY item_purchased
ORDER BY 1 DESC
LIMIT 5;

✔️ Insight: Identifies products heavily dependent on discounts.

Q7. Customer segmentation
WITH customer_type AS (
  SELECT customer_id, previous_purchases,
  CASE
    WHEN previous_purchases = 1 THEN 'New'
    WHEN previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
    ELSE 'Loyal'
  END AS customer_segment
  FROM customer
)
SELECT customer_segment, COUNT(*)
FROM customer_type
GROUP BY customer_segment;

✔️ Insight: Segments customers into lifecycle stages.

Q8. Top 3 products in each category
WITH item_counts AS (
  SELECT category, item_purchased,
  COUNT(*) AS total_orders,
  ROW_NUMBER() OVER (PARTITION BY category ORDER BY COUNT(*) DESC) AS rank
  FROM customer
  GROUP BY category, item_purchased
)
SELECT * FROM item_counts WHERE rank <= 3;

✔️ Insight: Finds best-selling items per category.

Q9. Repeat buyers vs subscription
SELECT subscription_status, COUNT(*)
FROM customer
WHERE previous_purchases > 5
GROUP BY subscription_status;

✔️ Insight: Checks if loyal customers tend to subscribe.

Q10. Revenue contribution by age group
SELECT age_group, SUM(purchase_amount)
FROM customer
GROUP BY age_group
ORDER BY 2 DESC;

✔️ Insight: Identifies highest revenue-generating age segments.

🐍 Python Usage

The customers.py file is used to:

Load CSV dataset using Pandas
Clean and preprocess data
Connect to PostgreSQL (via SQLAlchemy)
📈 Power BI Dashboard

The .pbix file contains:

Revenue analysis
Customer segmentation visuals
Product performance insights
Interactive filters (gender, category, age group)
🚀 How to Run the Project
1. Python Setup
pip install pandas sqlalchemy psycopg2-binary
2. Load Data
import pandas as pd
df = pd.read_csv("customer_shopping_behavior.csv")
3. SQL Setup
Import dataset into PostgreSQL
Run queries from PG Local.session.sql
4. Power BI
Open .pbix file in Power BI Desktop
Refresh dataset
📌 Key Insights
Subscription customers generally generate higher revenue
Discounts attract customers but don’t always reduce spending
Loyal customers contribute significantly to total revenue
Certain products dominate within categories
📬 Contact

Name: V. Naresh
Skills: Python, SQL, Pandas, Power BI

⭐ Conclusion
