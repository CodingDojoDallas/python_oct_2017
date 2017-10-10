Delete from friendships where id > 0; 
Delete from users where id > 0;
ALTER TABLE users AUTO_INCREMENT = 1;
ALTER TABLE friendships AUTO_INCREMENT = 1;

Insert into users (first_name, last_name)
Values('Chris', 'Baker');
Insert into users (first_name, last_name)
Values('Diana', 'Smith');
Insert into users (first_name, last_name)
Values('James', 'Johnson');
Insert into users (first_name, last_name)
Values('Jessica', 'Davidson');

Insert into friendships (user_id, friend_id)
Values(1,4);
Insert into friendships (user_id, friend_id)
Values(1,3);
Insert into friendships (user_id, friend_id)
Values(1,2);
Insert into friendships (user_id, friend_id)
Values(2,1);
Insert into friendships (user_id, friend_id)
Values(3,1);
Insert into friendships (user_id, friend_id)
Values(4,1);

SELECT users.first_name, users.last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users as user2 ON friendships.friend_id = user2.id
Order by friend_last_name

