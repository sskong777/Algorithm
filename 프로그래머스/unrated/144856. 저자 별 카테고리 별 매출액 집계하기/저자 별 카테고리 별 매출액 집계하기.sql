-- 코드를 입력하세요
SELECT
    A.AUTHOR_ID,
    A.AUTHOR_NAME,
    B.CATEGORY,
    sum(S.SALES*B.PRICE) 
from
    AUTHOR A
JOIN 
    BOOK B ON A.AUTHOR_ID = B.AUTHOR_ID
JOIN
    BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID 
WHERE 
    TO_CHAR(S.SALES_DATE, 'YYYY-MM') = '2022-01'
GROUP BY 
    A.AUTHOR_ID, A.AUTHOR_NAME, B.CATEGORY
ORDER BY
    A.AUTHOR_ID, CATEGORY DESC