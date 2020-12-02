import xmltodict
import json
import requests

def json_read_api_request():
    r = requests.get("https://formulae.brew.sh/api/formula.json")
    # https://formulae.brew.sh/api/formula/a2ps.json

    package_json = r.json()
    #package_first_element = package_json[0]['name']

    package_str = json.dumps(package_json, indent=2)
    print(package_str)

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

def read_file(file):
    with open(file) as f:
        content = f.readlines()
    return content

def read_xml_file(xmlfile):
    with open(xmlfile) as fd:
        doc = xmltodict.parse(fd.read())

    for index in range(len(doc['CATALOG']['CD'])):
        print(doc['CATALOG']['CD'][index]['TITLE'])
        print(doc['CATALOG']['CD'][index]['TITLE'])



def main():
    read_xml_file('Sample-XML-Files.xml')
    #res = read_file('test.txt')
    #print(res)



main()