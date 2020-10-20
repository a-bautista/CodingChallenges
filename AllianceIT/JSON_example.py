import json
import requests
from urllib.request import urlopen

json_file = '''
{
  "people": [
      {
          "name": "John Smith",
          "phone": "615-980-982",
          "emails": ["aa@hotmail.com","bb@hotmail.com","cc@hotmail.com"],
          "status": "True"
      },
      {
          "name": "Samantha",
          "phone": "615-980-111",
          "emails": ["zz@hotmail.com","yy@hotmail.com","xx@hotmail.com"],
          "status": "False"
      }
   ]
}
'''

json_file2 = '''
{
    "states":[
        {   
            "name": "Alabama",
            "abbreviation": "AL",
            "area_codes": ["205", "251", "256", "334", "938"],
            "status": "Ready"
        },
        {
            "name": "Alaska",
            "abbreviation": "AK",
            "area_codes": ["907"],
            "status": "Not ready"
            
        }
    ]
}
'''


def read_simple_json(json_file):
    loaded_json = []
    try:
        loaded_json = json.loads(json_file)
    except Exception as error:
        print(error)

    for state in loaded_json['states']:
        print(state['name'], state['abbreviation'])

    # modify the json
    for state in loaded_json['states']:
        del state['status']

    # store the results in the json
    modified_value = json.dumps(loaded_json, indent=2, sort_keys= True)
    print(modified_value)


def load_my_json_from_file():
    address = 'json_example.json'
    address_out = 'json_example_modified.json'

    # read the data
    with open(address) as f:
        data = json.load(f)

    for state in data['states']:
        print(state['name'], state['abbreviation'])

    # modify the json data
    for state in data['states']:
        del state['area_codes']

    # save the results
    with open(address_out, 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

def json_read_api_urlopen():

    with urlopen("https://formulae.brew.sh/api/formula/a2ps.json") as response:
        source = response.read()

    data = json.loads(source)
    print(data)

def json_read_api_request():
    r = requests.get("https://formulae.brew.sh/api/formula.json")
    # https://formulae.brew.sh/api/formula/a2ps.json

    package_json = r.json()
    #package_first_element = package_json[0]['name']

    package_str = json.dumps(package_json, indent=2)
    print(package_str)

    # because the data is a list with dictionaries, we can store the first element of the list

def json_read_api_request_specific_package():
    r = requests.get('https://formulae.brew.sh/api/formula.json')
    packages_json = r.json()
    package_name = packages_json[0]['name']
    print(packages_json)

    # the line from below works as a filter
    package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'
    r2 = requests.get(package_url)
    package_json = r2.json()

    package_str = json.dumps(package_json, indent=2)
    print(package_str)

    urls = package_json['analytics']['install_on_request']['30d']['a2ps']
    print(urls)

def json_read_api_request_all_packages():
    r = requests.get('https://formulae.brew.sh/api/formula.json')
    packages_json = r.json()

    for package in packages_json:

        package_name = package['name']
        package_desc = package['desc']

        # the line from below works as a filter
        package_url = f'https://formulae.brew.sh/api/formula/{package_name}.json'

        r2 = requests.get(package_url)
        package_json = r2.json()

        urls = package_json['analytics']['install_on_request']['30d'][package_name]
        print(urls)


def main():
    #read_simple_json(json_file2)
    #load_my_json_from_file()
    #json_read_api_urlopen()
    #json_read_api_request()
    #json_read_api_request_specific_package()
    json_read_api_request_all_packages()

main()

