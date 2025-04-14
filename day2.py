
#list
friends = ["anup","pradip","nabin"]

friends.append("samip")     #add element in last only
print(friends)

friends.insert(1,"bikram")    #add element
print(friends)

friends.pop()       #delete last element
print(friends)

friends.pop(1)      # delete specific emelent 
print(friends)

print(friends[0:2])     #if want two element print at one time

print(len(friends))     #for finding how many elements are in List

# dictionary
friend = {
    'name': 'Aakash',
    'age': 22
}

# key/value add 
friend['isNepali'] = True

# value access and check 
print(friend['isNepali'] == True)

print(friend)

print(friend.keys())   #to find keys of a dictionary
print(friend.values())   #to find values of a dictionary

del friend['isNepali']    #to delete key of a dictionary
print(friend)

if "name" in friend :
    print("name exists")




#Tuples

my_tuple = (1,2,"Apple", "Orange","Guava")
print(my_tuple[1])

thistuple = ("apple", "banana", "cherry")
print(thistuple)