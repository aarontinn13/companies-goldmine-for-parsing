with open('naatp_urlsfinal.txt', 'r', encoding='utf-8-sig') as r:
    for i in r.readlines():
        print(i.split('/')[-1].replace('-', ' ').replace('\n', ' '))