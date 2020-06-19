import re
str = '''the price of oil is 70$ for 3Boskeh for yesterday
the price of oil is 65$ for 3Boskeh for today
the price of oil is 80$ for 3Boskeh for wednesday
'''

result = re.findall(r'the price of oil is (\d+)\$ for (\d+)Boskeh for (.*)',str)

for price,boshkeh,day in result:
    print(price,boshkeh,day)

    
