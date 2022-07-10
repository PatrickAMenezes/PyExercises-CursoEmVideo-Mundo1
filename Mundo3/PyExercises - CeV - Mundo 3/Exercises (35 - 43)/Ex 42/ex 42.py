from urllib import request
try:
    site = str(input('What site do you want to consult: ')).strip().lower()
    request.urlopen(site).getcode()
except:
    print('\033[1;31mSite not found.\033[m')
else:
    print('\033[1;32mSite found.\033[m')

