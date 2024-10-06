import requests
from lxml import html

url_dirs = ['new-zealand', 'australia', '', 'south-africa', 'united-states', 'united-kingdom', 'canada']

base_url = 'https://ahrefs.com/top/'

for dir in url_dirs:
    
    if dir == '':
         url = f'{base_url}'
         dir = 'worldwide'
    else:
        url = f'{base_url}{dir}'
    
    response = requests.get(url)
    tree = html.fromstring(response.content)
    
    urls = []
    
    for i in range(1, 100):
        xpath = f'/html/body/div/div[1]/section[2]/div/div/div/section/div/div/div/table/tbody/tr[{i}]/td[3]/a'
        element = tree.xpath(xpath)

        if element:
            text = element[0].text_content().strip()
            urls.append(text)
        else:
            print(f'Element not found for {dir}, row {i}')
    
    file_name = f'Allowlists/{dir}.txt'
    with open(file_name, 'w') as file:
        for url in urls:
            file.write(f'{url}\n')

    print(f'{file_name} created with top 100 domains.')
