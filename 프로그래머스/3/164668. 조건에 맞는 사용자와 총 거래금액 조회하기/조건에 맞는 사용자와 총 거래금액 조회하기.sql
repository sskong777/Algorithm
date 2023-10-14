select 
    a.WRITER_ID,
    b.NICKNAME,
    sum(a.PRICE)
from 
    USED_GOODS_BOARD a
JOIN
    USED_GOODS_USER b ON a.WRITER_ID = b.USER_ID
WHERE 
    a.STATUS = 'DONE'
GROUP BY a.WRITER_ID, b.nickname
HAVING sum(a.PRICE) >= 700000
order by sum(a.PRICE)