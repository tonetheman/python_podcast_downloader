
# podcast puller

A script I wrote to download podcasts found on google podcasts.

The code is extremely simple and naive.

# how to install
download code

create a virtual env, I always put mine in a directory named env
`python3 -m venv env`

source it
`source env/bin/activate`

install beautifulsoup
`pip install beautifulsoup4`


# how to run this

Go find a podcast you want to download in google podcasts on the web

Get a list of the podcasts you want do download on the screen.
Usually I do this by clicking on the more episodes button.

Right click on the page and View Page Source for the page.

Select all of that page and save it in a file named `page.html`
I did it this way to alleviate the need to login to google. Just find the page in an already authorized browser... much easier.

Then run the program puller.py

# how does it work
It will read the file `page.html` that is sitting in the current directory.

It will find all the `div`s on the page with BeautifulSoup then loop through those divs looking for the jsdata attribute.

If there is a link in the jsdata attribute then the script will parse that link and download the file and save it in the current directory.

The code is SUPER SIMPLE and does not really do any error checking.

