--ejercicio 1
select FirstName, LastName from customers where Country = "Brazil";
--ejercicio 2
select FirstName, LastName, Title from employees where Title = "Sales Manager";
--ejercicio 3
select Composer from tracks where Composer = "AC/DC";
--ejercicio 4
select * from customers where not Country = "USA";
--ejercicio 5
select * from employees where Title = "Sales Manager";
--ejercicio 6
select distinct BillingCountry from invoices where BillingCountry is not null order by BillingCountry;
--ejercicio 7
select State, count(distinct CustomerId) as total_clientes from customers where Country = "USA" and State is not null group by State order by total_clientes desc;
--ejercicio 8
select sum(Quantity) as articulos from invoice_items where InvoiceId = 37;
--ejercicio 9
select count(TrackId) as canciones from tracks where Composer = "AC/DC";
--ejercicio 10
select InvoiceId, sum(Quantity) as articulos_totales from invoice_items group by InvoiceId;
--ejercicio 11
select BillingCountry, count(InvoiceId) as factura_pais from invoices group by BillingCountry order by factura_pais desc;
--ejercicio 12
SELECT count(InvoiceId) AS facturas_09 FROM invoices WHERE InvoiceDate >= "2009-01-01" AND InvoiceDate < "2010-01-01";
SELECT count(InvoiceId) AS facturas_11 FROM invoices WHERE InvoiceDate >= "2011-01-01" AND InvoiceDate < "2012-01-01";
--ejercicio 13
SELECT count(InvoiceId) AS factudas_09_11 FROM invoices WHERE InvoiceDate >= "2009-01-01" AND InvoiceDate <= "2011-01-01";
--ejercicio 14
SELECT Country, count(CustomerId) AS clientes_SP_BRZ FROM customers WHERE Country IN ("Brazil", "Spain") GROUP BY Country;
--ejercicio 15
SELECT * FROM tracks WHERE Name LIKE "You%";