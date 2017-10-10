/*-- Query 1
Select first_name, last_name, email, address.address from customer
Join address on customer.address_id = address.address_id
Where city_id = 312
*/

-- Query 2
/*Select title, description, release_year, rating, special_features, category.name from film
Join film_category on film_category.film_id = film.film_id
Join category on film_category.category_id = category.category_id
Where name = 'Comedy'
*/

/*-- Query 3
Select title, description, release_year, actor.first_name, actor.last_name, actor.actor_id from film
Join film_actor on film.film_id = film_actor.film_id
Join actor on actor.actor_id = film_actor.actor_id
Where actor.actor_id = 5
*/

/*-- Query 4
Select first_name, last_name, email, address.address from customer
Join address on customer.address_id = address.address_id
Join store on customer.store_id = store.store_id
Where store.store_id = 1 And (city_id = 1 or city_id = 42 or city_id = 312 or city_id = 459)
*/

/*-- Query 5
Select title, description, release_year, rating, special_features from film
Join film_actor on film_actor.film_id = film.film_id
where rating = 'G' and special_features Like '%behind the scenes%' and film_actor.actor_id = 15
*/

/*-- Query 6
Select film.film_id, title, description, actor.actor_id, first_name, last_name from film
Join film_actor on film_actor.film_id = film.film_id
Join actor on film_actor.actor_id = actor.actor_id
Where film_actor.film_id = 369 
*/

/*-- Query 7
Select title, description, release_year, rating, special_features, category.name, rental_rate from film
Join film_category on film_category.film_id = film.film_id
Join category on film_category.category_id = category.category_id
Where name = 'Drama' and rental_rate = 2.99
*/

/*-- Query 8
Select title, description, release_year, rating, special_features, category.name, first_name, last_name from film
Join film_category on film_category.film_id = film.film_id
Join category on film_category.category_id = category.category_id
Join film_actor on film_actor.film_id = film.film_id
Join actor on film_actor.actor_id = actor.actor_id
Where first_name = 'Sandra' and name = 'Action' and last_name = 'Kilmer'
*/
