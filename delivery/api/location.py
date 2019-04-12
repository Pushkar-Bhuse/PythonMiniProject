import googlemaps

gmaps = googlemaps.Client(key='AIzaSyBgrLgIKh5eh3TBIKuDVif9vnOjIANbstQ')

def get_distance(start, end):
    my_dist = gmaps.distance_matrix(start,end)['rows'][0]['elements'][0]
    print(my_dist)

def get_lat_lon():
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')
    lat = geocode_result[0]['geometry']['location']['lat']
    lon = geocode_result[0]['geometry']['location']['lng']
    return lat,lon