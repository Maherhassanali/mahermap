"""Main module."""
import random
import string
import ipyleaflet
import geopandas



class Map(ipyleaflet.Map):


    def __init__(self, center=[25,32] , zoom=5 , ** kwargs) -> None:
        if "scroll_wheel_zoom" not in kwargs :
            kwargs["scroll_wheel_zoom"] =True

            
        super().__init__(center=center,zoom=zoom,** kwargs)
        if "layers_control" not in kwargs:
            kwargs["layers_control"] = True

        if "fullscreen" not in kwargs:
            kwargs["layers_control"]=True

        self.add_draw_control()
        self.add_search_control()
        self.add_layers_control()


        

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

    def add_layers_control(self, position='topright'):
        """Adds a layers control to the map.
        Args:
            kwargs: Keyword arguments to pass to the layers control.
        """
        layers_control = ipyleaflet.LayersControl(position=position)
        self.add_control(layers_control)

    def add_fullscreen_control(self, position="bottomright"):
        """Adds a fullscreen control to the map.
        Args:
            kwargs: Keyword arguments to pass to the fullscreen control.
        """
        fullscreen_control = ipyleaflet.FullScreenControl(position=position)
        self.add_control(fullscreen_control)

    def add_tile_layer(self, url, name="Google_maps", attribution="", **kwargs):
        """Adds a tile layer to the map.
        Args:
            url (str): The URL of the tile layer.
            name (str): The name of the tile layer.
            attribution (str, optional): The attribution of the tile layer. Defaults to "".
        """
        tile_layer = ipyleaflet.TileLayer(
            url=url,
            name=name,
            attribution=attribution,
            **kwargs
        )
        self.add_layer(tile_layer)
    def add_basemap(self, basemap="satellite", **kwargs):

        import xyzservices.providers as xyz

        if basemap.lower() == "roadmap":
            url = 'http://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, name=basemap, **kwargs)
        elif basemap.lower() == "satellite":
            url = 'http://mt0.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}'
            self.add_tile_layer(url, name=basemap, **kwargs)
        else:
            try:
                basemap = eval(f"xyz.{basemap}")
                url = basemap.build_url()
                attribution = basemap.attribution
                self.add_tile_layer(url, name=basemap.name, attribution=attribution, **kwargs)
            except:
                raise ValueError(f"Basemap '{basemap}' not found.")
            
    def add_geojson(self, data, name='GeoJSON', **kwargs):
        """Adds a GeoJSON layer to the map.
        Args:
            data (dict): The GeoJSON data.
        """

        if isinstance(data, str):
            import json
            with open(data, "r") as f:
                data = json.load(f)

        geojson = ipyleaflet.GeoJSON(data=data,name=name, **kwargs)
        self.add_layer(geojson)

    def add_shp(self, data, name='Shapefile', **kwargs):
        """Adds a Shapefile layer to the map.
        Args:
            data (str): The path to the Shapefile.
        """
        import geopandas as gpd
        gdf = gpd.read_file(data)
        geojson = gdf.__geo_interface__
        self.add_geojson(geojson, name=name, **kwargs)



    

    




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
