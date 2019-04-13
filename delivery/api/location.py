from reservation.models import Branch
import googlemaps


# gmaps = googlemaps.Client(key='')

def get_traveltime(start, end):
    my_dist = gmaps.distance_matrix(start,end)['rows'][0]['elements'][0]
    return my_dist["duration"]["text"]

def get_lat_lon(address):
    geocode_result = gmaps.geocode(address)
    lat = geocode_result[0]['geometry']['location']['lat']
    lon = geocode_result[0]['geometry']['location']['lng']
    return lat,lon

def choose_closest(address_to):
    branches = Branch.objects.all()
    final = {"name":branches[0].name,"time":get_traveltime(branches[0].get_address(),address_to)}
    for branch in branches:
        address_from = branch.get_address()
        time = get_traveltime(address_from,address_to)
        if(time < final["time"]):
            final["name"] = branch.name
            final["time"] = time

    return final
