msg = ["Hello World","Shit","OMG"]
print msg
print msg[0][1]

l = [msg,[1,2,3],[4,5,6]]
print l
print len(msg)
print len(l)

msg.sort()
print msg

msg.insert(1,"WTF")
print msg

print msg.count("WTF")
print ""

msg1 = [1,2,1,3,1,4,1]
print msg1

msg1.remove(4) #remove the 1st match content
print msg1

msg1.insert(5,4) 
print msg1

msg1.pop(2) #remove an element in specific position 
print msg1
msg1.sort()
print msg1
msg1.reverse()
print msg1

msg2 = list("123")
print msg2
