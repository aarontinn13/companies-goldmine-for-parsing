aux = set()

with open('Companies Goldmine.csv', 'r') as r:
    with open('final_information2.txt', 'w') as w:
        for i in r:
            #print(i.split('~')[0])
            name = i.split('~')[0]
            if name not in aux:
                aux.add(name)
                #print(aux)
                w.write(i)
                #print(name)
            elif name == 'Cannot find data':
                continue
            else:
                continue