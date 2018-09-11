aux = []

with open('information.csv','r') as file1:
    for i in file1.readlines():
        i = i.split()
        #i = ''.join(i)
        aux.append(i)

with open('list_of_main_html.txt','w') as filewrite:
    for i,j in aux:
        i = int(i)
        j = j[:-1]
        for a in range(1,i+1):
            #print(a)
            #print(j+str(a))
            filewrite.write(j+str(a)+'\n')