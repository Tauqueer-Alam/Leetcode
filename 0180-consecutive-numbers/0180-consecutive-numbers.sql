# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums FROM (SELECT num,LAG(num) OVER(ORDER BY id) AS lag_num,LEAD(num) OVER(ORDER BY id) AS lead_num
FROM Logs) AS t
WHERE num=lead_num AND num=lag_num;