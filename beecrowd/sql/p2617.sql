-- Fornecedor Ajax SA

SELECT
    prod.name,
    prov.name
FROM
    products prod
    INNER JOIN providers prov ON prov.id = prod.id_providers
WHERE
    prov.name = 'Ajax SA';