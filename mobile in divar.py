#get model of mobile in divar esfahan
import re
import requests

response = requests.get('https://divar.ir/s/isfahan/mobile-phones')

source_of_page = response.text

result = re.findall(r'%s{1}class\=\"subtitle-16 post-card__title\"\>(.+)\<\/div\>$',source_of_page)

print(result)