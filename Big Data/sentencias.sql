SELECT * FROM `ivan-297304.babynames.names_2014` LIMIT 1000;


SELECT COUNT(name) AS conteo, name 
FROM `ivan-297304.babynames.names_2014` 
GROUP BY name
ORDER BY conteo DESC
LIMIT 5;

SELECT COUNT(name) AS conteo, name
from `ivan-297304.babynames.names_2014`
where gender = 'M'
and name like 'E%'
group by name 
order by conteo desc
limit 5;



SELECT COUNT(name) AS conteo, name
from `ivan-297304.babynames.names_2014`
where gender = 'F' and name like 'E%'
group by name
order by name
limit 5;


SELECT COUNT(DISTINCT(name)), name AS conteo
from `ivan-297304.babynames.names_2014`
where  gender = 'M'
group by name
order by name desc


SELECT COUNT(name) AS conteo, name
FROM `ivan-297304.babynames.names_2014`
GROUP BY name
HAVING COUNT(name) = 1
ORDER BY conteo desc
limit 5

select count FROM `ivan-297304.babynames.names_2014` t where t.count < 2
