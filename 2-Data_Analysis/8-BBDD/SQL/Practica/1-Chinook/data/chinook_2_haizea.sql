--ejercicio 1
SELECT
    customers.FirstName,
    customers.LastName,
    invoices.InvoiceId,
    invoices.InvoiceDate,
    invoices.BillingCountry
FROM customers
INNER JOIN invoices
    ON customers.CustomerId = invoices.CustomerId
WHERE customers.Country = 'Brazil';
--ejercicio 2
SELECT
    invoices.InvoiceId,
    employees.FirstName,
    employees.LastName
FROM invoices
INNER JOIN customers
    ON invoices.CustomerId = customers.CustomerId
INNER JOIN employees
    ON customers.SupportRepId = employees.EmployeeId;
--ejercicio 3
SELECT
    customers.FirstName AS nombre_cliente,
    customers.LastName AS apellido_cliente,
    customers.Country AS pais,
    employees.FirstName AS nombre_agente,
    employees.LastName AS apellido_agente,
    invoices.Total AS total_factura
FROM customers
INNER JOIN employees
    ON customers.SupportRepId = employees.EmployeeId
INNER JOIN invoices
    ON invoices.CustomerId = customers.CustomerId;
--ejercicio 4
SELECT 