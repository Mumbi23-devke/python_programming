#defined using squared brackets

friends = ["Janet", "Mitchele", "Natasha", " Mike", "Faith" , "Susie"]

#you can modify data in a list (add,remove or update)

friends.append('Kelly')
friends.append("Bob")
friends.append("Gill")

print(friends)

#counting starts from index zero

print(friends[5])
print(friends[6])
print(friends[-5])
friends.remove("Janet")
print(friends)