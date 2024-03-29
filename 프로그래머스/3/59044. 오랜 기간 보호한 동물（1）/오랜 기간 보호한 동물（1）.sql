-- 코드를 입력하세요
SELECT NAME, DATETIME
FROM
(SELECT 
    AI.NAME,
    AI.DATETIME
FROM 
    ANIMAL_OUTS AO
RIGHT JOIN
    ANIMAL_INS AI
ON 
    AO.ANIMAL_ID = AI.ANIMAL_ID
WHERE 
    AO.ANIMAL_ID IS NULL
ORDER BY DATETIME)
WHERE ROWNUM < 4

-- SELECT NAME, DATETIME
-- FROM (SELECT A.NAME, A.DATETIME
--       FROM ANIMAL_INS A, ANIMAL_OUTS B
--       WHERE A.ANIMAL_ID = B.ANIMAL_ID(+)
--       AND B.ANIMAL_ID IS NULL
--       ORDER BY A.DATETIME)
-- WHERE ROWNUM < 4;