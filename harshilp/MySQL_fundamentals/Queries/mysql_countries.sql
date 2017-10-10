/*-- Query 1
Select countries.name, language, percentage
FROM languages
LEFT JOIN countries
ON countries.id = languages.country_id
WHERE language = 'slovene'
ORDER BY percentage DESC
*/
/*-- Query 2
Select countries.name, count(*) as cities
From cities
Left Join countries
On cities.country_id = countries.id
Group by country_id
Order by cities DESC
*/

/*-- Query 3
Select name, population from cities
Where country_code = "MEX"
Having population > 500000
Order by population DESC
*/

/*-- Query 4
Select countries.name, language, percentage
FROM languages
LEFT JOIN countries
ON countries.id = languages.country_id
Having percentage > 89
ORDER BY percentage DESC
*/

/*-- Query 5
Select name, surface_area, population from countries
Where population > 100000 and surface_area < 501
*/

/*-- Query 6
Select name, government_form, capital, life_expectancy from countries
Where life_expectancy > 75 and capital > 200
Having government_form = 'Constitutional Monarchy'
*/

/*-- Query 7
Select cities.name, countries.name, district, cities.population from cities
Join countries on cities.country_id = countries.id
Where country_code = "ARG" and district = 'Buenos Aires'
Having cities.population > 500000
Order by cities.population DESC
*/

/*-- Query 8
Select region, count(*) as countries from countries
Group by region
Order by countries DESC
*/
