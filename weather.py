from requests_html import HTMLSession

s = HTMLSession()
query = input("Enter the name of a city to check the weather. ")
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'})

temp = r.html.find('span#wob_tm',first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
condition = r.html.find('div#wob_dcp span#wob_dc', first=True).text

print(f"{query.title()}: {temp}{unit} {condition}")