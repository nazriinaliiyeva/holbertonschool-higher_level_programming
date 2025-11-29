-- join
SELECT cities.id, cities.name,states.name AS state 
FROM cities
JOIN states ON cities.state_id = states_id
ORDER BY cities.id ASC;
