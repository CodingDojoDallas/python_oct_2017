 
# Deployment Update

### Locally

1. Add all your local changes
2. Commit
3. Push to master

### In your EC2

1. Navigate into your repo folder
2. Add just your settings.py file
3. Commit just your settings.py file
4. Pull the changes from git
5. Restart gunicorn: ```sudo systemctl restart gunicorn```
6. Restart nginx: ```sudo service nginx restart```
 
