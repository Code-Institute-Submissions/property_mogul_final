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
- [Arrow](https://pypi.python.org/pypi/arrow)
	- Arrow is a Python library that offers a sensible, human-friendly approach to creating, manipulating, formatting and converting dates, times, and timestamps
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/)
	- Beautiful Soup is a Python library for pulling data out of HTML and XML files
- [TinyMCE](https://www.tinymce.com/)
	- (Tiny Moxiecode Content Editor) is a platform-independent, browser-based WYSIWYG editor control, written in JavaScript and has the ability to convert HTML textarea fields or other HTML elements to editor instances.  It is used here for users to format their posts easily
- [Pillow](https://python-pillow.org/)
	- Python Imaging Library (PIL or Pillow) is a Python library that adds support for opening, manipulating, and saving many different image file formats
- [Bootstrap](http://getbootstrap.com/)
	- We use **Bootstrap** to give our project a simple, responsive layout

## Testing

- A number of tests were conducting using Django's testing framework and can be viewed in the associated tests.py files for each app
- Extensive in-browser testing was also utilised throughout its development

## Acknowledgements

### Some of the UI is thanks to the freely available Flatfy Theme by [Andrea Galanti](http://andreagalanti.it/portfolio/flatfy-theme/)
- I highly modified the theme, mainly for the landing page, which in turn uses the below:
- [Magnific Popup](http://dimsemenov.com/plugins/magnific-popup/)
	- a responsive lightbox & dialog script with focus on performance and providing best experience for users with any device
	- used here for the Screenshot Carousel allowing users to click on and enlarge individual screenshots
- [Animate.css](https://daneden.github.io/animate.css/)
	- used here for a number of CSS3 animations throughout the project
- [jQuery Morph Button](http://www.jqueryscript.net/lightbox/jQuery-Plugin-For-Popup-Window-with-Morphing-Button-Morph-Button.html)
	- Morph Button is a small jQuery modal plugin that reveals any HTML content by morphing the action button using CSS3 animations
	- used here for the Contact Form to 'morph' out when the button is clicked