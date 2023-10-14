SELECT
    animal_type,
    NVL(name,'No name'),
    sex_upon_intake
FROM
    ANIMAL_INS
ORDER BY animal_id