# rdap-fetcher

A simple script written in Python with Flask to provide very basic information about an IP address or web domain.

Including:
* Country of Registration
* Owner of Domain
* Description
* Registration Address

## Download

To get the script, either download the .zip or:

```
git clone https://github.com/arunbarnard/rdap-fetcher
```

## Run

Navigate to the download location, and run with:

```
python rdapQuery.py
```

## Modification

You are able to modify the Python or HTML code by modifying the following files:
*rdapQuery.py - Main Python script
* templates
  * main.html - Default HTML page
  * return.html - Shown when querying IP/domain name
* static
  * data.txt - The downloadable JSON file for the queried website
  * css
    * main.css - CSS for all HTML files
