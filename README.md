# travel_site

Here is the code for the travel site I was talking about, the logic is all contained in src/pages if you want to check that out.
It's pretty simple but basically what's going on is the user enters a destination, that string is sent to the teleport API which returns a list of cities or
neighborhoods they may trying to find. Once the user selects the correct city/neighborhood from that list, the latitutude and longitude
coordinates are sent to the zomato and darksky API's to return a slew of information such as current and future weather, popular restaurants 
and clubs, nightlife ratings, etc. The user can view all of this, as well as a google maps plugin showing their desired destination.

I originally wrote is as just a command line program, but wanted some practice with front end development so adapted the logic/code from that 
original program and created a website using the django web framework and that's what this is.


I never published it, so you'd need to set up a django development environemt to actually run the 
site on a local development server. I never really thought about sharing it when I was developing it so theres probably some
bugs/hiccups I'm not anticipating, but if you have the right environment you can get it going by doing the following:

from the root directory 
> source bin/activate
Now the virtual environment should be running and you can activate the server 
> cd src
> python3 manage.py runserver
Now you should be able to access it at http://127.0.0.1:8000/

Also, if you get it running the spinning icon on the search bar has nothing to do with the connection speed or anything, I was just trolling lol.
