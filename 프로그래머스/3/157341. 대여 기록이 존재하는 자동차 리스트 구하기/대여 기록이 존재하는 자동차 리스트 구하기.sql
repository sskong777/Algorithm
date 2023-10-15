select
    DISTINCT(C.CAR_ID)
from   
    CAR_RENTAL_COMPANY_CAR C
JOIN
    CAR_RENTAL_COMPANY_RENTAL_HISTORY H ON C.CAR_ID = H.CAR_ID
WHERE
    C.CAR_TYPE = '세단'
    and
    TO_CHAR(H.START_DATE,'YYYY-MM') = '2022-10'
order by
    1 desc;