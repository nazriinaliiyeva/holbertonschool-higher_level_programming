-- cities of california
SELECT id, name FROM  cities 
WHERE id = (
	SELECT id FROM STATES WHERE name = 'California'
)
ORDER BY id ASC;
