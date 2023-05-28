"""Main module."""
import random
import string
import ipyleaflet



class Map(ipyleaflet.Map):


    def __init__(self, center , zoom , ** kwargs) -> None:
        if "scroll_wheel_zoom" not in kwargs :
            kwargs["scroll_wheel_zoom"] =True

            print(kwargs)
        super().__init__(center=center,zoom=zoom,** kwargs)

        

    def add_search_control(self, position="topleft", **kwargs):
        """Adds a search control to the map.

        Args:
            kwargs: Keyword arguments to pass to the search control.
        """
        if "url" not in kwargs:
            kwargs["url"] = 'https://nominatim.openstreetmap.org/search?format=json&q={s}'
    

        search_control = ipyleaflet.SearchControl(position=position, **kwargs)
        self.add_control(search_control)

    def add_draw_control(self, **kwargs):
        """Adds a draw control to the map.

        Args:
            kwargs: Keyword arguments to pass to the draw control.
        """
        draw_control = ipyleaflet.DrawControl(**kwargs)

        draw_control.polyline =  {
            "shapeOptions": {
                "color": "#6bc2e5",
                "weight": 8,
                "opacity": 1.0
            }
        }
        draw_control.polygon = {
            "shapeOptions": {
                "fillColor": "#6be5c3",
                "color": "#6be5c3",
                "fillOpacity": 1.0
            },
            "drawError": {
                "color": "#dd253b",
                "message": "Oups!"
            },
            "allowIntersection": False
        }
        draw_control.circle = {
            "shapeOptions": {
                "fillColor": "#efed69",
                "color": "#efed69",
                "fillOpacity": 1.0
            }
        }
        draw_control.rectangle = {
            "shapeOptions": {
                "fillColor": "#fca45d",
                "color": "#fca45d",
                "fillOpacity": 1.0
            }
        }

        self.add_control(draw_control)

    

    

    




def generate_random_string(length=5):
    
    """
    Generate a random string of length 
    **enter the length of the string to generate the random string**

    Returns:
        string of length you entered
    """    
    letters = string.ascii_lowercase + string.digits + string.ascii_uppercase + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

def the_name(name):
    """write the name

    Args:
        name (string): just write the name you want 
        for testing
    """    
    print(name)
