# this is used to print sentense N times.

# input the sentence you want to repeat
s = raw_input('Please input the sentence which you want to repeat:\n')

# input the times by which you want the sentence to repeat.
N = int(raw_input('How many times do you want to repeat:\n'))

f = open('helloworld','w')

for x in range(1,N+1):
    if  x%10 == 1:
        print >> f,'%s%dst'%(s,x)
	print '%s%dst'%(s,x)
	#f.write()
    elif  x%10 == 2:
        print >> f,'%s%dnd'%(s,x)
	print '%s%dnd'%(s,x)
    elif  x%10 == 3:
        print >> f,'%s%drd'%(s,x)
	print '%s%drd'%(s,x)
    else:
        print >> f,'%s%dth'%(s,x)
	print '%s%dth'%(s,x)

f.close()

