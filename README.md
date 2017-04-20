# 'Property Mogul' Django App

## Overview

### What is this app for?

This was created for my Stream 3 Final Code Institute project.  It is crowd-funding app for property investment

### What does it do?

This app allows users to register as a member using Stripe Monthly subscription payments.  Membership gives you access to the blog with disqus commenting enabled, the members forum to allow topical discussions, the investment centre and the gift shop.  The Investment Centre and Gift Shop takes payments via PayPal.  You can also get in touch via the Contact section.

### How does it work?

- This app is built using the Python based Django framework which uses a variation on the Model-View-Controller (MVC) architecture called MTV (Model-Template-Views): 
	- Models: Represent the data model in the form of the relational database, in this case a MySQL database. Django uses the Django Object Relational Mapping (ORM) to create the tables and their relationships via Python objects, and to organise and manage the database
	- Templates: Visually represent the data model. This is the presentation layer and defines how information is displayed to the end user
	- Views: Define the business logic that links the templates to the models
- Django allows the app to maintain seperation of concerns:
	- separating application logic from presentation and markup

## Features

### Existing Features
- Members:
	- allows users to register using Stripe subscription payment functionality
	- stores member data in MySQL database to allow login/logout access to members only area
- Investment Centre:
	- Properties: makes use of PayPal Subscriptions to allow Members to invest a Monthly amount in featured Properties
	- Gift Shop: uses PayPal Payments system to allow Members to make purchases of related products
- Blog:
	- app enabling blogs to be posted, viewed and edited
	- displays timestamp, tags and records number of views
	- disqus embedded to allow user commenting
- Forum:
	- Multi-user, multi-thread forum for members to discuss property investments
- Poll:
	- Forum users can set up a poll with their Forum thread for other users to vote on specified topics
- Contact:
	- uses django-contact-form to collect name, email address and message


## Tech used

### Some of the tech used includes:
- [Django](https://www.djangoproject.com/)
	- Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design
- Further tech details coming soon!