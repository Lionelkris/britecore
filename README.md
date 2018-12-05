# britecore
feature request britecore app

The app is deployed on heroku and live https://polar-garden-63113.herokuapp.com/

To run locally, please do the following:
1.git clone
2.pip install -r requirements.txt
3.run "python app.py"

Tech stack used -
OS: Ubuntu
Server Side Scripting: Python 2.7+ or 3.6+
Server Framework: Flask
ORM: Sql-Alchemy
Frontend: html
database: sqlite

App behavior:
Accepts - title, description, client, priority, target date and product-area. All fields aare made mandatory.
Also by default saves the created_on time of each record. This is done for sorting the feature-requests in further enhancement.
A numbered priority according to the client (1...10000). Client Priority numbers will not repeat for the given client.
If there is a repeatation in priority for a specific client, it throws a error message and gives the instruction to user on how to proceed next.

Will update with new things over the next iterations.

