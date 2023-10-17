-- 코드를 입력하세요
SELECT 
    ANIMAL_ID,
    NAME
FROM (
    SELECT
        OUTS.ANIMAL_ID,
        OUTS.NAME
    FROM
        ANIMAL_OUTS OUTS
    JOIN 
        ANIMAL_INS INS ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
    ORDER BY (OUTS.DATETIME - INS.DATETIME) DESC
    )
WHERE ROWNUM <= 2



-- select animal_id, name
-- from (
--     SELECT i.ANIMAL_ID, i.NAME
--     from ANIMAL_INS i
--     join ANIMAL_OUTS o
--     on i.ANIMAL_ID = o.ANIMAL_ID
--     order by o.DATETIME - i.DATETIME desc
-- )
-- where rownum <= 2