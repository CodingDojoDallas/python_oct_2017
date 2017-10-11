/*-- Query 1
Select date_format(charged_datetime, '%M') as month, sum(amount) as revenue from billing
Where billing.charged_datetime between '2012-03-01 00:00:00' and '2012-04-01 00:00:00'
*/

/*-- Query 2
Select client_id, sum(amount) as revenue from billing
Where client_id = 2
*/

/*-- Query 3
Select domain_name, sites.client_id from clients
Join sites on sites.client_id = clients.client_id
Where clients.client_id = 10
*/

/*-- Query 4
Select date_format(created_datetime, '%M') as month, date_format(created_datetime, '%Y') as year, count(*) as number, client_id from sites
Where client_id = 1 -- or 20 gives only 1
Group by month, year
*/

/*-- Query 5
Select domain_name, count(*) as leads_generated, date_format(registered_datetime,'%M %D, %Y') as date_generated from sites
Join leads on sites.site_id = leads.site_id
Where leads.registered_datetime between '2011-01-01 00:00:00' and '2011-02-15 00:00:00'
group by domain_name
*/

/*-- Query 6
Select	clients.first_name, clients.last_name, count(*) as total_leads from clients
Join sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Where leads.registered_datetime between '2011-01-01 00:00:00' and '2011-12-31 00:00:00'
Group by clients.client_id
*/

/*-- Query 7
Select clients.first_name, clients.last_name, date_format(registered_datetime, '%M') as month, count(*) as total_leads from clients
Join sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Where (month(registered_datetime) between 1 and 6) and (year(registered_datetime) = 2011)
Group by clients.client_id, month
*/

/*-- Query 8a
Select concat(clients.first_name,' ' , clients.last_name) as client_name, domain_name, count(*) as total_leads from clients
Join sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Where registered_datetime between '2011-01-01 00:00:00' and '2011-12-31 00:00:00'
Group by domain_name
Order by clients.client_id
*/

/*-- Query 8b (for all time)
Select concat(clients.first_name,' ' , clients.last_name) as client_name, domain_name, count(*) as total_leads from clients
Join sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Group by domain_name
Order by clients.client_id
*/

/*-- Query 9
Select first_name, last_name, sum(amount) as revenue, date_format(charged_datetime, '%M') as month, date_format(charged_datetime, '%Y') as year from clients
Join billing on billing.client_id = clients.client_id
Group by billing.client_id, month, year
Order by clients.client_id
*/

/*-- Query 10
Select concat(clients.first_name, ' ', clients.last_name) as client_name, group_concat(sites.domain_name) as 'sites' from clients
left join sites on clients.client_id = sites.client_id
group by clients.client_id;
*/
