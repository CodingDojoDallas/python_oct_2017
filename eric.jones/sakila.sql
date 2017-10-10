SELECT c.first_name, c.last_name, c.email, a.address, a.address2, city.city, a.postal_code
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city on a.city_id = city.city_id
WHERE a.city_id = 312;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre
FROM film f
JOIN film_category fc on f.film_id = fc.film_id
JOIN category c on fc.category_id = c.category_id
WHERE c.name = "Comedy";

SELECT a.actor_id, a.first_name, a.last_name, f.title, f.description, f.release_year
FROM actor a
JOIN film_actor fa ON a.actor_id = fa.actor_id
JOIN film f on fa.film_id = f.film_id
WHERE a.actor_id = 5;

SELECT c.first_name, c.last_name, c.email, a.address, a.address2, city.city, a.postal_code
FROM customer c
JOIN address a ON c.address_id = a.address_id
JOIN city on a.city_id = city.city_id
WHERE a.city_id IN (1, 42, 312, 459) AND c.store_id = 1;

SELECT f.title, f.description, f.release_year, f.rating, "Behind the Scenes" AS special_feature
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.actor_id = 15 AND f.special_features LIKE "behind the scenes";

SELECT f.film_id, f.title, a.actor_id, CONCAT(a.first_name, " ", a.last_name) AS actor_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE f.film_id = 369;

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS genre
FROM film f
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.film_id  = c.category_id
WHERE c.name = "Drama" AND  f.rental_rate > 2.99; /* Changed rental_rate to > 2.99, as = 2.99 returned 0 rows */

SELECT f.title, f.description, f.release_year, f.rating, f.special_features, c.name AS Genre, CONCAT(a.first_name, " ", a.last_name) AS actor_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
JOIN film_category fc ON f.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
WHERE c.name = "Action" AND a.first_name = "SANDRA" AND a.last_name = "KILMER"