import re
import requests
import json


# Define function Web Service Request
# =====

# ```
# response = requests.post(base_url + '/' + function, data=payload, headers=headers)
# ```
# Where `payload` is the request JSON object, and `headers` is a dictionary of headers that,
# in our case, includes the content type of the body and the authentication key.
# Such a call returns a Response object that has three objects of interest:
# + the Response code: an HTTP code, 
#   * 200 means "ok"
#   * 404 is "not found, check the URL"
#   * 403 means "wrong key, probably you are not worthy of using the system"
#   * 401 means "invalid or utterly moronic request"
#   * 50X that something very bad occurred server side
# + the elapsed time;
# + the response object, which can be interpreted as a string or as a dictionary.

def call_restful_api(function, data={}, base_url="", key="", method='GET'):
    '''
    Calls a RESTful API
        Parameters:
            function (string): the name of the API method to invoke
            data (dictionary): the data payload
            bas_url (string):  the base addres of the API
            key (string):      the service key you registered
            method(string):    the HTTP method you want to use, defaults to POST

        Returns:
            service response (str or dictionary): Web service response, either a dictionary or a string.
    
    '''
    # set request headers    
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': key
    }

    # serialize request data into a json object
    payload  = json.dumps(data)
    response = None
    
    # invoke the Web Service
    if method == 'POST':
        response = requests.post(base_url + '/' + function, data=payload, headers=headers)
    else:
        response = requests.get( base_url + '/' + function, data=payload, headers=headers)
    if response.status_code == 200: # the 200 status means 'success'
        try:
            return response.json() 
        except:
            try:
                return response.text
            except:
                print('Unable to decode server response')
    else:
        print('Request failed with code ' + str(response.status_code))
    return None

def parse_wkt_point(geom_string):
    '''
    Parse the POINT (Lon Lat)
    '''
    try:
        m = re.search(r'(\d+\.?\d*)\s+(\d+\.?\d*)', geom_string)
        lon = m.group(1)
        lat = m.group(2)
        return lon, lat
    except:
        return None, None
