-- 코드를 입력하세요
SELECT
    count(*)
FROM
    USER_INFO
WHERE 
    TO_CHAR(JOINED,'YYYY') = '2021'
    AND (AGE >= 20 AND AGE <=29)
