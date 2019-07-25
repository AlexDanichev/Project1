#
our_range = range(100)
our_list = []
for x in our_range:
    if x%2==0:
        our_list.__add__(x)
        x=x+1;
        continue
###################
print(our_list)//
numbers = range (100)
our_list = list()
for n in numbers:
    if n % 2 == 0:
        our_list.append(n)
print(our_list)
##########################
our_list=[n for n in range(100) if n % 2 == 0]
print(our_list)
#############
new_list = [1, 2, 3, 4, 5, 10, 20]
if 10 in new_list():
    print("yep 10 is really there")


countries_dict= {"Ukraine":"Kiev","Poland":"Warsaw", "Russia":"Moscow", "Canada":"Ottava", "Belarus":"Minsk" }
countries_list= ["USA", "Mexica", "Australia", "Germany" , "United Kingdom"]
for c in countries_list:
    if c in countries_dict:
        print{countries_dict[c]}


#print(countries_dict.__getitem__("Ukraine"))


try:
    a=1/0

except:
    print("Exception was caught")