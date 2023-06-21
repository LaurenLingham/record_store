# Table of Contents
1. [Brief](#brief)
2. [My App](#my_app)
3. [Setup Instructions](#setup-instructions)

## Brief

### Shop Inventory

Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers.

#### MVP

* The inventory should track individual products, including a name, description, stock quantity, buying cost, and selling price.
* The inventory should track manufacturers, including a name and any other appropriate details.
* The shop can sell anything you like, but you should be able to create and edit manufacturers and products separately.
  * This might mean that it makes more sense for a car shop to track makes and models of cars. Or a bookstore might sell books by author, or by publisher, and not by manufacturer. You are free to name classes and tables as appropriate to your project.
* Show an inventory page, listing all the details for all the products in stock in a single view.
* As well as showing stock quantity as a number, the app should visually highlight "low stock" and "out of stock" items to the user.


## My App

My app is designed for a record store which stores albums held in stock.  The user has the ability to view, create, edit and delete albums as well as artists.

#### Technologies Used

* Python
* HTML
* CSS
* Flask
* PostgreSQL and the psycopg driver


## Setup Instructions

Install pip dependencies
```bash
pip install flask
pip install psycopg2
pip install python-dotenv
```

Add the Postgres credentials as environment variables to allow the psql commands to be executed
```bash
$env:PGUSER='<enter-your-postgres-username>'
$env:PGPASSWORD='<enter-your-postgres-password>'
```

Create the database
```bash
createdb record_store
psql -d record_store -f db/record_store.sql 
```

Populate the data
```bash
python seeds.py
```

Run the app
```bash
python -m flask run
```
You should see the following:

```bash
 * Serving Flask app 'app.py'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://localhost:4999/
```

Click on the link to open the app in your browser