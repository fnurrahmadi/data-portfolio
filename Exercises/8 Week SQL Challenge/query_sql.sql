SELECT *
FROM members;

SELECT *
FROM menu;

SELECT *
FROM sales;

-- 1. What is the total amount each customer spent at the restaurant?
SELECT s.customer_id, SUM(me.price) total_amount
FROM sales s
JOIN menu me
ON s.product_id = me.product_id
GROUP BY 1
ORDER BY 1;

-- 2. How many days has each customer visited the restaurant?
SELECT s.customer_id, COUNT(DISTINCT s.order_date) visit_count 
FROM sales s
GROUP BY 1
ORDER BY 1;

-- 3. What was the first item from the menu purchased by each customer?
SELECT s.customer_id, me.product_name, MIN(s.order_date) first_order_date
FROM sales s
JOIN menu me
ON s.product_id = me.product_id
WHERE s.order_date = (SELECT MIN(s2.order_date) FROM sales s2 WHERE s.customer_id = s2.customer_id)
GROUP BY 1,2
ORDER BY 1;

-- 4. What is the most purchased item on the menu and how many times was it purchased by all customers?
SELECT me.product_name, s.customer_id, COUNT(1) AS purchase_count
FROM sales s
JOIN (SELECT product_id FROM sales GROUP BY 1 ORDER BY COUNT(1) DESC LIMIT 1) s1
ON s.product_id = s1.product_id
JOIN menu me
ON s.product_id = me.product_id
GROUP BY 1,2
ORDER BY 3 DESC, 2 ASC;

-- 5. Which item was the most popular for each customer?
-- 6. Which item was purchased first by the customer after they became a member?
-- 7. Which item was purchased just before the customer became a member?
-- 8. What is the total items and amount spent for each member before they became a member?
-- 9.  If each $1 spent equates to 10 points and sushi has a 2x points multiplier - how many points would each customer have?
-- 10. In the first week after a customer joins the program (including their join date) they earn 2x points on all items, not just sushi - how many points do customer A and B have at the end of January?

