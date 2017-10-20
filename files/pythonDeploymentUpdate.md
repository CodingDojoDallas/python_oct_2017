 
# Deployment Update

### Locally

1. Add all your local changes
2. Commit
3. Push to master

### In your EC2

1. Navigate into your repo folder
2. Remove your db.sqlite3 
3. Pull the changes from git
4. wget your db.sqlite3 from git
```
wget https://raw.githubusercontent.com/<username>/<repo>/master/db.sqlite3
```
5. Restart gunicorn: ```sudo systemctl restart gunicorn```
6. Restart nginx: ```sudo service nginx restart```
 
