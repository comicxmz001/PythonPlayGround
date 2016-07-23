# convert xx.yy to xx dollars and yy cents
def convert(var):
    dollar = int(var)
    cents = int(100*(var-dollar))
    print dollar,"Dollars","and",cents,"cents"
    return "" 
# Tests
print convert(117.23)
print convert(11.20)
print convert(1.12)
print convert(12.01)
print convert(1.01)
print convert(0.01)
print convert(1.00)
print convert(0)
print convert(-1.40)
print convert(12.55555)