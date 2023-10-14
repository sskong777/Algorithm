SELECT
    EXTRACT(YEAR FROM S.SALES_DATE),
    EXTRACT(MONTH FROM S.SALES_DATE),
    I.GENDER,
    COUNT(DISTINCT(I.USER_ID))
FROM 
    USER_INFO I
INNER JOIN
    ONLINE_SALE S ON S.USER_ID = I.USER_ID
GROUP BY
    EXTRACT(YEAR FROM S.SALES_DATE), EXTRACT(MONTH FROM S.SALES_DATE), I.GENDER
HAVING 
    I.GENDER IS NOT NULL
ORDER BY
    1,2,3