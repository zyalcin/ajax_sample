# ajax_sample
This app implements Ajax which allows a front-end to communicate with the back-end by just transmitting the necessary changes and updating the database and front-end to a movie data base. 


This app does that by:

- A movie ratings page that works with your copy of a movie data base created internally
- Allows users to login and rate movies, but with re-rendering the whole thing, then
- Allows users to replace that behavior with incremental updates of particular movies
- Allows users to rate movies on a 1-5 star scale. 

The web application displays a selection of movies along with their current ratings and a way for the user to rate that movie. 
When the movie is rated, just the minimum data is sent to the back end.
The back end stores the rating, re-calculate the movie's average rating, store that, and send the updated average rating to the front end. 

The front end then displays the updated average rating.
