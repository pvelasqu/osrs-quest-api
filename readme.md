# GitHub Repository for OSRS Quests API
## Sample API Calls
### To get a list of all of the quests
https://osrs-api.appspot.com/api/quest
### To get a quest by name
https://osrs-api.appspot.com/api/quest/<quest_name>
### To get a list of quests that a user has requirements for
https://osrs-api.appspot.com/api/user/<user_name>
# Setup Instructions
1.  Clone the Repository
2.  pip install -r requirements.txt
3.  Setup Google Cloud SQL Databases
4.  Setup your proxy so you can access your google Cloud SQL database through your local computer
5.  Set your local environment variable for SQLALCHEMY_DATABASE_URI to your connection string to your database
6.  Create your tables to match the tables which the code requires.