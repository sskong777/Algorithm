-- 코드를 입력하세요
SELECT
name
FROM
(SELECT
name
FROM
ANIMAL_INS
ORDER BY DATETIME ASC)
where 
rownum <= 1
