from json import loads as json_to_obj


class GeoFenceGeoJSON(object):
    def __init__(self, json_obj):
        self.type = json_obj["type"]
        self.features = json_obj["features"]


example_location = json_to_obj("""
        { "type": "FeatureCollection",
        "features": [
          { "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [102.0, 0.5]},
              "properties": {
                "prop0": "value0"
              }
            },
          { "type": "Feature",
            "geometry": {
              "type": "LineString",
              "coordinates": [
                [102.0, 0.0], [103.0, 1.0], [104.0, 0.0], [105.0, 1.0]
                ]
              },
            "properties": {
              "prop0": "value0",
              "prop1": 0.0
              }
            },
          { "type": "Feature",
             "geometry": {
               "type": "Polygon",
               "coordinates": [
                 [ [100.0, 0.0], [101.0, 0.0], [101.0, 1.0],
                   [100.0, 1.0], [100.0, 0.0] ]
                 ]
             },
             "properties": {
               "prop0": "value0",
               "prop1": {"this": "that"}
               }
             }
           ]
         }
    """
)

locations = {
    1: GeoFenceGeoJSON(example_location)
}