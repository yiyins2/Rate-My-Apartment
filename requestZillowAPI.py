import requests
from xml.etree.ElementTree import fromstring, ElementTree
import xml.dom.minidom
from classApartment import Apartment
#zws-id: X1-ZWz1g0tbpxip6z_86zet

# parameters = {'zws-id': 'X1-ZWz1g0tbpxip6z_86zet', 'address': '1109 W \
#     Stoughton St', 'citystatezip': '61801', 'rentzestimate': True}
# response = requests.get("http://www.zillow.com/webservice/GetSearchResults.htm", params=parameters)

parameters = {'zws-id': 'X1-ZWz1g0tbpxip6z_86zet', 'zpid': 89056297, 'count': 10, 'rentzestimate': True}
response = requests.get("http://www.zillow.com/webservice/GetComps.htm", params=parameters)


# This root contains only the request house info
# Or the request house info and all 10 comparables around it
root = fromstring(response.content)

# xmlOfRoot = xml.dom.minidom.parseString(response.content)
# prettyXml = xmlOfRoot.toprettyxml()

# Lists of elements of each info type
zpidList = root.findall('.//response//zpid')
addressList = root.findall('.//response//address')
rentList = root.findall('.//response//rentzestimate/amount')

# Testing
print('The length of zpidList is ', len(zpidList))

# Create a list of apartments
apartmentList = []
for i in range(len(zpidList)):
    zpid = int(zpidList[i].text)
    rent = int(rentList[i].text)
    address = addressList[i].find('street').text + ', ' \
        + addressList[i].find('zipcode').text + ', ' + addressList[i].find('city').text + ', ' + addressList[i].find('state').text
    apartmentList.append(Apartment(zpid))
    apartmentList[i].set_rate(rent)
    apartmentList[i].set_address(address)


# Testing
print('The length of apartmentList is ',len(apartmentList))

# print(apartmentList[0].zpid,apartmentList[0].rentPerMonth)
for i in range(len(apartmentList)):
    apartmentList[i].display_info()
