-- 코드를 입력하세요
SELECT
    CAR_ID,
    (case when car_id in(
        select car_id 
        from
            CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            TO_CHAR(START_DATE,'YYYY-MM-DD') <= '2022-10-16'
        AND
            TO_CHAR(END_DATE,'YYYY-MM-DD') >= '2022-10-16')
     then '대여중'
     else '대여 가능'
     end)
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY
    CAR_ID
order by
    car_id desc