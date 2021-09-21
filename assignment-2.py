l = []
while True:
    x = input("Enter names :")
    if x == '':
        break
    else:
        l.append(x)

likes = {}

if len(l) == 0:
    likes[0] = "Nobody likes this"
if len(l) == 1:
    likes[1] = l[0]+ 'likes this'
if len(l) == 2:
    likes[2] = '{} and {} likes this'.format(l[0],l[1])
if len(l) == 3:
    likes[3] = '{} {} and {} likes this'.format(l[0],l[1],l[2])
if len(l)>3:
    likes[len(l)] = '{} {} and {} others likes this'.format(l[0],l[1],(len(l)-2))

print(likes[len(l)])
