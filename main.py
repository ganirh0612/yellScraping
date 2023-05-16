import requests
import pandas
import bs4

url = 'https://www.yell.com/ucs/UcsSearchAction.do?'

parameter = {
    'keywords': 'Hospitals',
    'location': 'london',
    'scrambleSeed': '1136827959'
}

header = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
base_url = 'https://www.yell.com/'

result = []

req = requests.get(url, params=parameter, headers=header)
print(req.status_code)
soup = bs4.BeautifulSoup(req.text, 'html.parser')

#Scraping Process
headerContent = soup.find_all('div', 'row bussinessCapsule--mainRow')

for content in headerContent:
    title = content.find('h2', 'bussinessCapsule--name.text-h2').text
    classification = content.find('span', 'bussinessCapsule--classification').text
    webLink = base_url + content.find('div', 'bussinessCapsule--ctas').find('a')['href']

    #Sorting Data
    data_dict = {
        'title': title,
        'classification': classification,
        'website': webLink
    }

    print(data_dict)
    result.append(data_dict)

print('Jumlah Datanya Adalah ', len(result))