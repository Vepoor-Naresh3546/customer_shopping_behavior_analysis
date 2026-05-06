select * from customer limit 20

select gender, SUM(purchase_amount) as revenue
from customer
group by gender

SELECT
   customer_id, 
   purchase_amount
FROM customer
WHERE discount_applied = 'Yes' 
AND purchase_amount >= (
    SELECT AVG(purchase_amount) 
    FROM customer
);

select item_purchased, ROUND(AVG(review_rating::numeric),2) as "Average Product Rating"
from customer
group by item_purchased
order by avg(review_rating) desc
limit 5;
