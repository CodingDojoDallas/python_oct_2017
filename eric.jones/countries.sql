SELECT c.Name, cl.Language, cl.Percentage
FROM countrylanguage AS cl
JOIN country AS c ON cl.CountryCode = c.Code
WHERE cl.language = "Slovene"
ORDER BY cl.Percentage DESC;

SELECT c.name, COUNT(city.ID) AS Cities
FROM country AS c
JOIN city ON c.Code = city.CountryCode
GROUP BY c.name
ORDER BY Cities DESC;

SELECT city.Name
FROM city
JOIN country ON city.CountryCode = country.Code
WHERE city.Population > 500000 AND country.Name = "Mexico"
ORDER BY city.Population DESC;

SELECT c.Name, cl.Language, cl.Percentage
FROM country c
JOIN countrylanguage cl ON c.Code = cl.CountryCode
WHERE cl.Percentage > .89
ORDER BY cl.Percentage DESC;

SELECT Name
FROM country
WHERE SurfaceArea < 501 AND Population > 100000;

SELECT Name
FROM country
WHERE GovernmentForm = "Constitutional Monarchy" AND Capital > 200 AND LifeExpectancy > 75;

SELECT c.Name, city.Name, city.District, city.Population
FROM country c
JOIN city ON c.Code = city.CountryCode
WHERE c.Name = "Argentina" AND city.District = "Buenos Aires" AND city.Population > 500000;

SELECT Region, COUNT(Code) AS CountryCount
FROM country
GROUP BY Region
ORDER BY CountryCount DESC;