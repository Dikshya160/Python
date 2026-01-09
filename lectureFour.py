# marks= {
#     "name":"DIkshya",
#     "age" : 22,
#     "subject": ["java", "c", "c++", "python"],
#     "topics" : ("coding", "theory"),
#     "is adult": "True"
# }
# print(type("name"))

# print(marks["name"])
# print(marks["topics"])
# marks["age"]= 35
# marks["class"]= "bachelor"
# print(marks)



# dict={}
# dict["name"]= "diksha" 
# dict["mood"]= "anger"
# print(dict)



              #Dictionary Method
marks= {
    "name":"DIkshya",
    "age" : 22,
    "subject": ["java", "c", "c++", "python"],
    "topics" : ("coding", "theory"),
    "is adult": "True"
}

# print(marks.keys())             
# print(list(marks.keys()))
# print(len(list(marks.keys())))


#print(marks.values())  


# print(marks.items())
# pairs =(list(marks.items()))
# print(pairs[2])
# #print(type(marks.items()))



# print(marks.get("subject"))



# new_dict={"city":"butwal", "num":9847}
# marks.update(new_dict)
# print(marks)


                           #SETS
# sets={1,2,3,4,2,1,"hello","true", "world", 3, "world"}
# print(sets)
# print(len(sets))   -> unordered form ma output dinxa, 
#                        no dublication allowed


# collection = set ()   #create empty set; syntax
# print(collection)
# print(type(collection))




                       #Method of set
# collection= set()
# # add
# collection.add(1)
# collection.add(2)
# collection.add(1)
# collection.add("hello")  # string
# collection.add("true")   #BOOLEAN
# collection.add((1,2,3,4))
# print(collection)

# remove
#ollection.remove("true")
#print(collection)


#clear
#collection.clear()
#print(collection)


#    pop

# collection.pop()
# print(collection)

# collect={"hello", "world", 4,6, 7}
# print(type(collect))
# print(collect.pop())
# print(collect.pop())
# print(collect.pop())



#    UNION
# set1={1,2,3,4}
# set2={3,4,5,6}
# print(set1.union(set2)) -> {1,2,3,4,5,6}
# print(set1)              -> no change in value
# print(set2)


#intersection
# set1={1,2,3,4}
# set2={2,3,5,6}
# print(set1.intersection(set2))






# QUE
# dict={}
# a=int(input("Enter the marks of phy:"))
# b=int(input("Enter the marks of che:"))
# c=int(input("Enter the marks od bio:"))
# new_dict={"phy":a, "che": b, "bio":c}
# print(dict.update(new_dict))
# print((dict))


#value= {9, "9.0"}
# values={
#     ("float", 9.0),
#     ("int", 9)
# }

# print(values)

