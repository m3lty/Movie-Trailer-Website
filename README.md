# Movie Trailer Website

An adaptive python script to create an HTML file containing a list of Movies, including a movie poster and trailer.

## Getting Started

All required files are included, as well as several Movie objects within entertainment_center.py to provide a base for the generated HTML.


### Installing
Running the entertainment_center.py script will provide an example of the HTML generated. The code has been pre-populated with a few of our favorite films.
This can be accomplished using several methods.

Using the command prompt in windows, navigate to the directory where the files are located. This can be done by using the 'cd' command.
For example, if the folder is located on the C: drive, in the Users folder you would type the following command:

```
cd c:\Users

```
Assuming you have Python installed you will then type the following command:

```
py entertainment_center.py

```
(If you do not have Python, you can get it [here](https://www.python.org/downloads/))

In order to add a list of your own movies, the media.Movie() method should be called. This method requires four attributes.
Here is an example of the minimum code needed to generate the object:

```
movie_title = media.Movie("Movie Name",
                          "Synopsis of the movie",
                          "Link to poster or box art for the movie.",
                          "Link to a Youtube trailer of the film.")
```

The movie objects should then be added to the list 'movies' near the end of the file.

```
movies = [movie1, movie2, movie3 ...]
```

## Authors

* **Adam Hoffman** -  [M3lty](https://github.com/M3lty)
* Source code for fresh_tomatoes.py provided by [Udacity](https://github.com/udacity/ud036_StarterCode)


## Acknowledgments

* Thanks to Udacity for providing the source code and lessons to help create this app.
* A special thanks to Krissy for always believing in me.
