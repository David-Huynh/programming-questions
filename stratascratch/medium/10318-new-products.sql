/*
Finds the difference in new product launches for each car brand from 2019 to 2020

*/
SELECT company_name, 
    sum(
    CASE 
    WHEN year=2019 
        THEN -1 
    WHEN year=2020 
        THEN 1 
    END) AS net_products 
FROM car_launches 
WHERE year IN (2019,2020) 
GROUP BY company_name
