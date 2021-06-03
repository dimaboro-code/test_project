import requests

url = 'https://stepic.org/media/attachments/course67/3.6.3/'
r = requests.get('https://stepic.org/media/attachments/course67/3.6.3/699991.txt')
print(r)
r = r.text
print(r)
c = 0
while True:
    r = requests.get(url + r).text
    print(r)
    if r.split()[0] == 'We':
        print(r)
        
        with open('out.txt', 'w') as ouf:
            for i in r.splitlines():
                ouf.write(i + '\n')
        
        break
    c += 1
    print(c)
