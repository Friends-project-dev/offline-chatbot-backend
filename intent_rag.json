[
  {
    "question": "gross sales today",
    "sql": "SELECT SUM(total) as gross_sales FROM sales WHERE date = DATE('now');"
  },
  {
    "question": "number of orders today",
    "sql": "SELECT COUNT(*) FROM sales WHERE date = DATE('now');"
  },
  {
    "question": "top 5 products",
    "sql": "SELECT product, SUM(quantity) as qty FROM sales GROUP BY product ORDER BY qty DESC LIMIT 5;"
  }
]
