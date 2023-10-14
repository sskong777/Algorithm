select 
    a.category,
    sum(b.sales)
from 
    book a
join
    book_sales b on a.book_id = b.book_id
where 
    TO_CHAR(b.SALES_DATE,'YYYY-MM') = '2022-01'
group by
    a.category
    
order by
    category 