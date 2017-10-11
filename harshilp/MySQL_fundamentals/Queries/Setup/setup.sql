-- Ascending Order
Select * from users
Order by birthday;

-- Descending order born before 1980 with tweets
Select first_name, last_name, handle, birthday, tweet from users
Join tweets on users.id = tweets.user_id
Where Year(birthday) < 1980
Order by birthday DESC;

-- favorite tweets ordered by last name
Select first_name, last_name, handle, tweet from users
Join faves on users.id = faves.user_id
Join tweets on faves.tweet_id = tweets.id
Order by last_name;

-- Shows the followers of each user ordered by descending last name
Select concat(users.first_name, ' ', users.last_name) as user_name, followers.first_name as follower from users
Join follows on users.id = follows.followed_id
Join users as followers on follows.follower_id = followers.id
Order by users.last_name DESC;

-- Shows number of followers greater than 2
Select concat(users.first_name, ' ', users.last_name) as user_name, handle, count(*) as followers from users
Join follows on users.id = follows.followed_id
Group by user_name
Having followers > 1