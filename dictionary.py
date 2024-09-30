#dictionary = a collection of {key:value} pairs ordered and changeable. no duplicates (Item;price)
capitals={"USA":"washington D.C.",
          "India": "Nerw delhi",
          "China": "Beijing",
          "Russia": "Moscow"}
#print(dir(capitals)) (DIR GIVES You the attributes of the motghods of the dictionary)
#print(help(capitals)) (help gives you bakc the documentatiuon)

#print(capitals.get("USA"))

#if capitals.get("Japan"):
    #print("That ca[ital exist")
#else:
    #print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") #(REMOVES THE ITEMS)
# capitals.popitem()#REMOVES LAST ITEM IN DICTIONARY
# capitals.clear()#CLEARS DICTIONARY
# keys= capitals.keys()#RETURNS ALL THE KEYS AND NOT THE VALUEABLES
# # values=capitals.values()
# # print(keys)
# # print(values)
# for key in capitals.keys():
#               print(key)
values=capitals.values()
for value in capitals.values():
    print(value)
items= capitals.items()
for key, value in capitals.items():
    print(f"{key}:{value}")