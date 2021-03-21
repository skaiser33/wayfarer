# Wayfarer

## Deployed At:
http://wayfarer-cs.herokuapp.com

## Description

Wayfarer is an online hub for users ("wayfarers") to share city-specific reviews about locations around the world. 

Upon signing up / logging in, users are redirected to their personal profile page. Returning users who have submitted reviews will see a list of their most recent reviews. From the primary navigation bar, a user can search for a city name or go to a list of all cities sorted by the number of reviews.

By clicking on a specific city, the user will see a display of all existing reviews (including title, date added, and truncated content preview) and can add a review of their own. By clicking on an existing review, the user will be able to see the full review. Reviews can be edited or deleted by the author. 

The app features full user authentication and allows for the user to create an account for a unique username and login securely.

## Technologies Used
- Python
- Django
- Postgres
- CSS
- Boostrap
- HTML
- VSCode
- Google Chrome Developer Tools

## User Stories
As a user, I want to:

- Sign up for an account, log in if I already have an account, and be redirected to my profile page after logging in. The sign up and log in feature shoudl be available on the navigation bar prior to login.
- Log out when I am done using the app from a link in the nav bar.
- See my name, current city, join date, and profile photo on my public profile page, with the ability to edit name and current city from this page. A default profile photo will be displayed until I upload a profile photo.
- See a site-wide header on every page. 
- Search for a city or see a full list of available cities, with city names that redirect me to a photo of the city and a list of applicable reviews with author photo.
- Click on a review title and see the full review.
- Edit or delete my own reviews.


## Data Models and ERD

![Data Models and ERD](https://i.imgur.com/xjlh8Wu.jpg)


## Wireframes

Client Wireframes		

![Client Wireframes	](https://i.imgur.com/OFHvKd4.png)


Developer Wireframe - Profile Page

![Profile Page](https://i.imgur.com/PrVQvB4.jpg)


## Major Hurdles
- Getting stuck on certain aspects of an opinionated framework. 
- Using Django auth forms within modals. 
- Boostrap resistance to certain elements of CSS. 
- The .env folder and .env files. We will always name our virtual environment .venv moving forward.
- Debugging with many moving pieces at play. 

## Major Victories
- In the span of a week, we completed two sprints of an app that pleased our clients. 
- This was our first time really diving into Bootstrap, and we were overall very pleased with the results.
- Clarity through repetition. The django workflow now feels fairly natural. 
- Responsive design.
- Search functionality. 

## Future Goals
- Modals for all forms to provide a more modern design and user experience. 
- Full comment functionality.
- Further refinement of styling and responsive design.
- Pagination of reviews.
- Welcome email for new users.
- "Pretty" URLs for city and user names. 
- City markers on a map featured on the homepage.


## Screenshots

Home Page

![Home Page](https://i.imgur.com/KLYFjRQ.jpg)


City Show Page

![City Show Page](https://i.imgur.com/93KJsY8.jpg)


Mobile Navigation

![Mobile Navigation](https://i.imgur.com/83EFDvY.png)