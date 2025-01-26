import requests
from geopy.geocoders import OpenCage
from geopy.exc import GeocoderServiceError
from geopy.adapters import RequestsAdapter
import ssl

# List of lat/lon points
geopoints = [
    (40.9356239090198, -87.9393230124372),
    (42.21340200309749, -83.5910788728212),
    (40.219213256931695, -74.0679949599861),
    (35.25123982693762, -84.89834227809764),
    (40.10537826764666, -83.05943855018312),
    (39.28976321130925, -83.99000560872628),
    (38.90956588728545, -75.42995059319149),
    (42.90752665439783, -85.72227814324116),
    (33.01589544085433, -79.88625917583704),
    (41.53453543120288, -71.31001695618579),
    (44.99618493049925, -93.19960524771011),
    (40.99783561196271, -111.93055059771233),
    (43.19549653110771, -70.59675031482759),
    (33.14467549505811, -117.31661874060299),
    (42.60424328461873, -72.55224360778328),
    (39.56179154759331, -76.33050537255211),
    (33.01589544085433, -79.88625917583704),
    (-34.52566261727184, -58.546261102632656),
    (33.24933463708528, -111.78785819471766),
    (34.154404201864374, -118.44695687956661),
    (32.866733905593286, -117.22193674753488),
    (44.79498242899726, -68.75768984236962),
    (39.585009598708986, -84.18169752036881),
    (49.285870112921984, -123.06060093410342)
]

# Replace 'YOUR_API_KEY' with your actual OpenCage API key
api_key = 'YOUR_API_KEY'

# Create a custom RequestsAdapter with SSL verification disabled
class InsecureRequestsAdapter(RequestsAdapter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.session.verify = False
        self.session.mount('https://', InsecureAdapter())

class InsecureAdapter(requests.adapters.HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE
        kwargs['ssl_context'] = context
        return super().init_poolmanager(*args, **kwargs)

    def build_response(self, req, resp):
        response = super(InsecureAdapter, self).build_response(req, resp)
        response.content
        return response

geolocator = OpenCage(api_key, adapter_factory=InsecureRequestsAdapter)

def reverse_geocode(geopoints):
    locations = []
    for lat, lon in geopoints:
        try:
            location = geolocator.reverse((lat, lon), exactly_one=True)
            address = location.raw['components']
            city = address.get('city', address.get('town', ''))
            county = address.get('county', '')
            state = address.get('state', '')
            locations.append((city, county, state))
        except GeocoderServiceError as e:
            print(f"Error retrieving data for ({lat}, {lon}): {e}")
            locations.append((None, None))
    return locations

# Get locations
locations = reverse_geocode(geopoints)
for loc in locations:
    print(loc)
