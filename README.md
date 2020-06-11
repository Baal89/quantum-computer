[![Build Status](https://travis-ci.com/Baal89/quantum-computer.svg?branch=master)](https://travis-ci.com/Baal89/quantum-computer)

# Quantum Computer

Quantum Computer is a full-stack online eCommerce site where the users can look and buy for any new cool components for their computer.
The site allowed the users to buy, leave a review and check for prices for a lot of different computer components.

Live site [here](https://quantum-computer.herokuapp.com/)

GitHub repository [here](https://github.com/Baal89/quantum-computer)

## UX

This website is for all those people who need a new component for their PC or even a new whole computer. Thanks to this site they can look and check for different prices and brands.

- as a user, I want to know more about specific computer components, so I can buy the best option for me.
- as a user, I want to search for an array of components categories, so I can see all the different options for the same product category.
- as a user, I want to safely purchase components, so I am sure my money is protected from fraud or problems.
- as a user, I want to login to the site, so a can retrieve my pieces of information and I can do it quickly after the first registration.
- as a user, I want to add a selected product to the cart, so I can then proceed to the transaction only for the selected item.
- as a user, I want to modify the item quantity selected, so I can amend any error I made.
- as a user, I want to know the price of each product, so I can easily check what is more affordable for me.
- as a user, I want to know all the products I have purchased, so I can always check the amount, the date and the item I have bought.
- as a user, I want to update my user information, so I can modify my data in the case they have changed during the time.
- as a user, I want to leave a review for the product I have purchased, so I can let other users and the site owner know if that specific product is good or not.
- as a user, I want to know the product average score, so I can immediately see if that product is a valid choice or not.
- as a user, I want to get in touch with the company, so I can ask them some extra information not provided on the site.

### Design
The possibility to leave a review only from the purchase history it is intentional, in this way I can prevent the users to leave a review on the product they have not bought.

The user cannot modify or remove any already submitted review, in order to do that they have to contact the site owner with the contact us page. 
This is also a part of the protection scheme for fake reviews.

The template prevents not logged in users to access many parts of the site. For example is not possible for a not logged user to add a product to the cart, or to access the checkout page,
with an empty basket.

I used as Wireframes base the [third milestone project](https://github.com/Baal89/recipe-app)

## Features


### Existing Features

- `navbar`- allows the user to navigate throughout the site, by clicking on it.
- `navbar categories` - allows the user to see all the different options for the same type of categories, by clicking on it.
- `product details` - allows the user to see the features of the selected product, by clicking on the product image or in the product button.
- `add to cart` - allows the user to add the selected product to the cart, by clicking on it.
- `checkout` - allows the user to pay for the selected product/products, by having them fill out the checkout form.
- `register` - allows the user to create a new account to the site in order to make a purchase, by having them fill out the registration form.
- `login` - allows the user to login to the site with their already existing account, by having them fill the login form.
- `profile` - allows the user to check and update their user profile information, by having them modify the registration form and clicking on the button update.
- `purchase history` - allows the user to check all the transactions made on the site ordered by date, by clicking on the profile button.
- `leave a review` - allows the user to leave a review only for the purchased item shown in the purchase history, by having them fill out the review form.
- `see the reviews` - allows the user to see all the review made for one product from all the different users, by clicking on the product in the categories list.
- `review rating` - allows the user in a more immediate way to see the product average rating as a result of all the different reviews made, by clicking on the product in the categories list.
- `search bar` - allow the user to search for a specific product or to return a list of products for a keyword, by typing a keyword in the search bar.
- `forgot the password` - allows the user to reset its account and submit a new password.
- `modify quantity` - allows the user to modify the product quantity in the cart, by modifying the quantity and clicking on the modify button.
- `contact us` - allows the user to get in touch with the site owner, by having them fill out the contact us form

### Features Left To Implement
I tried to meet the project criteria for this project so the overall result is far away to a real-world business site. I underestimated the time needed to complete the project
and also the learning step to learn this framework, considering also the pandemic we are all living at the moment and the fact that I been enrolled in the new
Django3 course, I found myself at the end of the time for this course, so I deliberately left the project extremely simple.
This project has taken a lot of time but it has given me a strong foundation for the framework.
After said that, I can say that there are a lot of features to implement for the future:
1. the model used for the product is extremely simple and does not include any kind of validation so the database can be easily corrupt. I would like
   to create a more complex model maybe one for each category of product sold on the site.
2. The new and more complex model also means an increasing number of pieces of information for each product can be displayed with a much more rich visual complexity of the site.
3. the main purpose of every eCommerce site is the delivery system. Prices due to the far and information about the date and time of the delivery should be provided.
4. A tracking parcel app should be also created.
5. A stock quantity counter should also be available to check the disponibility of the product in real-time in the site. 

## Technologies Used

* [HTML5]()
* [CSS]()
* [javaScript](https://www.javascript.com/)
* [PYthon](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
    * Django is the framework used to built the structure of the site, along side with HTML5 and the Jinja template.
* [PostgreSQL](https://www.postgresql.org/)
    * PostgreSQL is the database used by Heroku.
* [Heroku](https://dashboard.heroku.com/)
    * Heroku is the platform used to deploy the site.
* [Bootsrap 4](https://getbootstrap.com/)
    * Bootstrap is used for the grid system and for some front-end features like the navbar and the cards used for the products.
* [Google Fonts](https://fonts.google.com/)
    * some part of the site used fonts like `Roboto` and `Orbitron`.
* [Font Awesome](https://fontawesome.com/)
    * Font Awesome is used to add icon throughout the project.
* [Amazone AWS](www.amazon.com)
    * Amazon AWS is used to store all the static files and media of the site.
* [Stripe](https://stripe.com/ie)
    * Stripe allows the user to make secure payments.

## Testing

For a matter of time, there are not any automated tests for this site unfortunately.

The HTML code has been tested using the [W3C Markup Validation Service](https://validator.w3.org/)

The CSS code has been tested using the [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)

Because the product model and the way I structured the database is very simple the home page has not any working link, except for the navbar.

All automated test was done using [Travis-CI](https://travis-ci.com/). Travis was used throughout the unit testing of this project to provide continuous
integration with the deployed site. Travis documentation provides all the information needed to set it up.

1. navbar:
    1. Select any navbar link and verify that they return to the correct page

2. forms: 
    1. Try to submit the empty form and verify that an error message about the required fields appears.
    2. Try to submit a form with an invalid email address and verify that a relevant error message appears.

3. product details:
    1. Verify that all the products in the database return the correct product details.

4. purchase history:
    1. Verify that the purchase history is representative only of the current logged in user.
    2. Verify that the user if has never made any purchase should see a message in the purchase history says `nothing bought yet`

5. add to cart:
    1. Try to add an item to the cart while not logged in and verify to be redirected to the login page.
    2. Try to increase the quantity of the products in the cart and verify that the total is correctly updated.
    3. Try to remove a product from the cart and verify that the quantity and the total price are modified.

6. checkout:
    1. Try to click on the checkout button with an empty cart and verify that the button is disabled.
    2. Try to click on the checkout button with some item in the cart and verify that the checkout form is correctly loaded.
    3. Try to leave the checkout form empty and verify that an error message appears.
    4. Try to fill the checkout form and verify that a success message appears.

7. login:
    1. Try to register with the same credentials of another user and verify that an error message appears.
    2. Log in with your current detail and verify that a success message appears.

8. review:
     1. Try to submit the empty form and verify that an error message about the required fields appears.
     2. Verify that each product shows all the reviews related to it.
     3. verify that the average score for the product is the correct average for the product itself.

The superuser `admin` is the only one who made some purchase.

The review functionality can be seen for this product:

- [Gigabyte GeForce GTX 1660 Super OC 6GB Graphics Card](https://quantum-computer.herokuapp.com/products/get_product/18)

The site is fully responsive at all different resolution thanks to the implementation of the bootstrap framework and has been tested using the google dev tool.

### Known issue/Bugs

After countless of trying has been impossible for me to send an email to my personal email address, this has resulted in an SMPT authentication error, 
even in the deployed version.

I have been told from the tutoring service that is not possible to enter your either email address or username for the login functionality, but only the email address.
this is a known issue with the used version of Django. 

## Deployment

This project has been deployed on Heroku.

- To run the code locally:
    1. clone or download the [repository](https://github.com/Baal89/quantum-computer)
    2. open the repository with your favourite IDE.
    2. add an allowed host in the `settings.py` in the `eCommerce app`.
    3. then run the server with the help of the console with `python3 manage.py runserver`.
    4. you will get an error as you are missing the environmental variable.
    5. create an `env.py` at the top level of the project and inside it `import os`.
    6. import the `env.py` inside the `settings.py`.
    7. the `env.py` should contain the following key, value in quotes:
        1. `os.environ.setdefault` (`EMAIL_ADDRESS`, value)
        2. `os.environ.setdefault`(`EMAIL_PASSWORD`, value)
        3. `os.environ.setdefault`(`SECRET_KEY`, value)
        4. `os.environ.setdefault`(`STRIPE_PUBLISHABLE`, value)
        5. `os.environ.setdefault`(`STRIPE_SECRET`, value)
        6. `os.environ.setdefault`(`DATABASE_URL`, value)
        7. `os.environ.setdefault`(`AWS_ACCESS_KEY_ID`, value)
        8. `os.environ.setdefault`(`AWS_SECRET_ACCESS_KEY`, value)

- To deploy my project I have done the following steps:

    1. Created a new repository on Github where the project will be deployed unto at each commit. 
    At first, use a git remote command to link the project with the new repo. Then use the `git push -u origin master` command to push codes and every change into the new repo.
    Using the CLI in terminal to call `git init` to start git initialization on the project. 
    This allows a file/files to be added to the Github repo by calling a `git add` command. 
    Then any added file/files are being committed with a `git commit -m "commit message"` command. 
    Afterwards, the file is been pushed with `git push` where Github username + password is required. 
    Once successful, the code will be deployed into your repo and `git status` command should indicate branch tree clean.
    
    2. Created a new app on Heroku where the app is hosted live. At first, to allow Heroku locate application we login into the CLI 
    using `heroku login -interactive` command. 
    You will be requested to input username and password for Heroku account. After which you can request Heroku Apps via CLI.
    Knowing the apps you need to pass deployment into then we can use heroku `git:remote -a` to allow Git automatically update deployment in Heroku. Once this has been remotely passed.
    To host the app unto Heroku pass the IP and PORT config to match the route main config.
    To allow git to `push` to Heroku the command `git push heroku master` must be called for a final push. 
    For a successful and healthy push it needs to have the `requirement.txt` and `Procfile files` installed or updated. 
    The requirement.txt requires to be updated along with any installed packages so it can deploy successfully.
    Also, you need to set `COLLECT_STATIC = 1` in the Heroku variable.
    
To prevent the publication of sensitive data on a public repository in GitHub, I created a gitignore file with the following file to ignore:
- `*.sqlite3`
- `__pycache__`
- `/.c9/`
- `env.py`

## Credit

### Content

- the product details have been taken from this [site](https://www.novatech.co.uk/)
- I have taken inspiration for the site from the following site:
    1. [Novatech](https://www.novatech.co.uk/)
    2. [Tom's Hardeware](https://www.tomshw.it/)

- I found an incredible help on the resources provided from StackOverflow
- Also, I found a lot of tutorials on youtube about the framework that has proven themselves incredibly useful.

### Media 
- the images used on the site are been taken from Google.

### Acknowledgements
- I have received inspiration for this project from CodeInsinstitute.

