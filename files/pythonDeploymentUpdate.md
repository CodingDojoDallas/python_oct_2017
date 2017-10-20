 
# Deployment Update

### Locally

1. Add all your local changes
2. Commit
3. Push to master

### In your EC2

1. Navigate into your project folder
2. Add just your settings.py file: ```git add settings.py```
3. Commit
4. Stash all db changes: ```git stash```
4. Pull the changes from git
5. Restart gunicorn: ```sudo systemctl restart gunicorn```
6. Restart nginx: ```sudo service nginx restart```
 
