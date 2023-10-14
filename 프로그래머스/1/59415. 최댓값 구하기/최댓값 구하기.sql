-- -- 코드를 입력하세요
-- SELECT DATETIME AS 시간
-- FROM ANIMAL_INS
-- WHERE DATETIME = 
-- (SELECT MAX(DATETIME) FROM ANIMAL_INS)


select datetime
from 
(select * from animal_ins order by datetime desc)
where rownum <= 1