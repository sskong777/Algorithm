select 
    car_id, round(avg(end_date-start_date+1),1)
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by 
    car_id
having
    round(avg(end_date-start_date+1),1) >= 7
order by
    2 desc,
    1 desc;