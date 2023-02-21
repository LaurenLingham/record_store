# Table of Contents
1. [Brief](#brief)
2. [My App](#my_app)
3. [Technologies Used](#technologies-used)
4. [Setup Instructions](#setup-instructions)
<br>

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

My app is for a record store which tracks which albums they have in stock.  The user has the ability to view, create, edit and delete Artists and Albums.


## Technologies Used

* Python
* HTML
* CSS
* Flask
* PostgreSQL and the psycopg


## Setup Instructions

### PostGreSQL database

Change directory into `project` and run the following commands:

```bash
# terminal
createdb shop_manager
psql -d record_store -f db/record_store.sql 
```

```bash
# terminal
python3 seeds.py
```

```bash
# terminal

pip3 install Flask
```

```bash
# terminal
flask run
```
You should see the following:

```bash
* Serving Flask app "app.py"
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://localhost:4999/ (Press CTRL+C to quit)
```

Click on the link to open the app in your browser.