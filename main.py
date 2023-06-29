# #dictionary program
# # syntax = key:value
# #example = name:Alice, age: 25
# #always use brackets, key can have same syntax as string

# person = {"name" : "Paul", "age" : 25, "height" : 1.75 }

# print(person["name"])

# person["name"] = "Brian"

# print(person["name"])

# #add new keys in dic

# person["job"] = "Developer"
# person["purchases"] = ("chocolate", "butter", "cheese")
# # print(person)

# #use collection in loop

# for i in person:
#     # print(i)
#     # print(person[i])
#     print(f"key: {i} - value: {(person[i])}")

#---PART 2 --- 
#using dic w/ large amount of data

#list of persons

persons = [
    ("Alice", 25, 1.6),
    ("Brian", 25, 1.10),
    ("Paul", 20, 2.2),
    ("Brianna", 21, 1.3)
]

#search for paul
def get_info(name, l):
    for i in l:
        if i[0] == name:
            return i
    return None

#info = get_info("Batman", persons)
#print(info)

#using dictionary
persons_dict = {
    "Alice" : (25, 1.6),
    "Brian" : (25, 1.10),
    "Paul" : (20, 2.2),
    "Brianna" : (21, 1.3)
    
}

# info = persons_dict["Paul"]
#for not in list:
info = persons_dict.get("Jack") #()because its a function
if not info:
    print("Key not found")
else:
    print(info)


#for lists you have to go through entire list
#for dictionaries, get direct 