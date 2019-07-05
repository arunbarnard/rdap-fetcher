# -- Web-Based RDAP fetcher --
# By Arun Barnard on 04/07/2019

from flask import Flask, render_template, request
from ipwhois import IPWhois
import json
import socket

app = Flask(__name__)

# Default
@app.route('/')
def home():
    # Return the default HTML site when the website loads.
    return render_template('main.html')


def lookup(ip):
    # Import locally as to not interfere with other lookup functions
    from emojiflags.lookup import lookup
    ip = IPWhois(ip)
    # Lookup IP address for domain name
    output = ip.lookup_rdap(depth=1)
    # Save JSON data to a local file
    with open('static/data.txt', 'w', encoding='utf-8') as outfile:
        json.dump(output, outfile, ensure_ascii=False, indent=2)
    config = json.loads(open('static/data.txt').read())
    # Find the unique website name so it can be used to call specific data from the JSON file
    name = str(config["entities"])
    name = name.replace("[", "")
    name = name.replace("]", "")
    name = name.replace("'", "")
    # Retrieve some relevant data from the JSON file
    ipaddress = config["query"]
    country = (config["asn_country_code"])
    # Get the emoji flag for the country
    countryflag = lookup(country)
    owner = config["objects"][name]["contact"]["name"]
    description = config["asn_description"]
    address = config["objects"][name]["contact"]["address"]
    # Remove unnecessary or irrelevant characters from the address in order to be readable
    address = str(address[0]).replace("{'type': None, 'value': '", "")
    address = address.replace("'}", " ")
    # Combine details into a list to return
    details = [ipaddress, country + " " + countryflag, owner, description, address]
    return details


@app.route('/', methods=['POST'])
def my_form_post():
    # Request domain name from the main HTML page form
    domain = request.form['number']
    # Use a library to get the IP address of the domain name
    ip = socket.gethostbyname(domain)
    details = lookup(ip)
    # Return all the relevant details to the HTML page.
    return render_template('return.html', ipaddress=details[0], country=details[1], owner=details[2],
                           description=details[3], address=details[4])


if __name__ == "__main__":
    # Setup data
    app.run(debug=True, port=8080)
