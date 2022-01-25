# site_checker
Script to check if a site is operational - If not, script will send a notification

# Setup
1.) Clone the repository to your local machine  
2.) In the repository folder, create `api_secrets.py` and `sites.py` files  
3.) Populate your pushover details in `api_secrets.py` using the following format:  
  ```
  # Pushover Authentication Details
  pushover_api_token = '<insert_your_api_token>'
  pushover_user_key = '<insert_your_user_token>'
  ```
4.) Populate your site list in the `sites.py` file using the following format:
  ```
  site_list = ('https://blog.blakehyatt.com', 'https://blakehyatt.com')
  ```
5.) Add the execution of the script to your local machine's crontab file. I used the following parameters:
  ```
  0 7-22 * * * python3 /home/wendingtuo/site_checker/site_checker.py > /home/wendingtuo/logs/site_checker.log
  ```
