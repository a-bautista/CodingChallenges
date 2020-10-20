import json

def validate_ipv4(ip):
    valid_ip_status = True
    valid_numbers = set(x for x in range(0,257))
    num_ip = ip.split(".")

    for value in num_ip:
        if int(value) not in valid_numbers:
            valid_ip_status = False
        elif len(value)>3:
            valid_ip_status = False
    #json_file['valid_ip'] = valid_ip_status
    return valid_ip_status

def validate_ipv6(ip):
    valid_values = '0123456789ABCDEFabcdef'
    valid_ip_status = True
    chunks = ip.split(":")
    for chunk in chunks:
        if len(chunk)>4 or len(chunk)==0 or not all(c in valid_values for c in chunk):
            valid_ip_status = False
    return valid_ip_status

def main():
    with open('json_ips.json') as f:
        json_file = json.load(f)

    for i, value in enumerate(json_file['ips']):
        print(value['ip'])
        if str(value['ip']).count('.')==3:
            valid = validate_ipv4(value['ip'])
            print(valid)
            #json.dump(valid, f, indent=2)
        elif str(value['ip']).count(':')==7:
            valid = validate_ipv6(value['ip'])
            print(valid)
        else:
            print("not valid IP")

main()