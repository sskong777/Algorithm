SELECT 
    HISTORY_ID,
    (DAILY_FEE * (END_DATE - START_DATE + 1)) * (1-NVL(discount_rate, 0)/100) FEE
FROM 
    CAR_RENTAL_COMPANY_CAR C JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY H
    ON C.CAR_ID = H.CAR_ID
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    ON C.CAR_TYPE = P.CAR_TYPE 
    AND P.DURATION_TYPE = (CASE
                            WHEN (END_DATE - START_DATE + 1) >= 90 THEN '90일 이상' 
                            WHEN (END_DATE - START_DATE + 1) >= 30 THEN '30일 이상' 
                            WHEN (END_DATE - START_DATE + 1) >= 7 THEN '7일 이상' 
                            ELSE NULL
                           END)
    
WHERE C.CAR_TYPE = '트럭'
ORDER BY 2 DESC, 1 DESC