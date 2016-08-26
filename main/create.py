from models import Compliment
f = open('comp.txt', "r")
str = f.read()
list = str.split()
for i in list:
    if len(i) > 3:
        Compliment.objects.create(compliment=i)
        print 'done'
print '//////////////DONE/////////////'
