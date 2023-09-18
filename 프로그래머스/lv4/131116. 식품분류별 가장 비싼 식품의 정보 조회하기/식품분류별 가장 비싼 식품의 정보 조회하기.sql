SELECT b.CATEGORY, b.MAX_PRICE, a.PRODUCT_NAME
FROM FOOD_PRODUCT a JOIN (
    SELECT CATEGORY, max(PRICE) AS MAX_PRICE
    FROM FOOD_PRODUCT
    GROUP BY CATEGORY
) b ON a.CATEGORY = b.CATEGORY AND a.PRICE = b.MAX_PRICE
WHERE a.CATEGORY IN ('과자', '국', '김치', '식용유')
ORDER BY 2 DESC


-- -- 코드를 입력하세요
-- SELECT
--     category,
--     max(price),
--     max(product_name)
-- FROM
--     FOOD_PRODUCT
-- GROUP BY
--     CATEGORY
-- having
--     category in ('과자', '국', '김치', '식용유')
-- order by 
--     max(price) desc