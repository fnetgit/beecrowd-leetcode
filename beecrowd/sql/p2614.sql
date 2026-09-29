-- Locações de Setembro

SELECT
    cust.name,
    rent.rentals_date
FROM
    customers cust
    INNER JOIN rentals rent ON cust.id = rent.id_customers
WHERE
    rent.rentals_date BETWEEN '2016-09-01' AND '2016-09-30';