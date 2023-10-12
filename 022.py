with open('projecteuler.net_resources_documents_0022_names.txt') as f :
    data = f.read()
    data = data.split(',')

for i in range(len(data)) :
    data[i] = data[i][1:len(data[i]) - 1]

data.sort()
ans = 0 

def val(word) :
    s = 0 
    for i in word : 
        s += ord(i) - 64
    return s 


for idx , i in enumerate(data) :
    ans += (idx + 1) * val(i)

print(ans)