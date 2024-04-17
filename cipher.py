user_string = input("Please enter a message to find the frequency of words: ").lower()


# removes punctuation
user_string = "".join(filter(lambda x: x.isalpha() or x.isspace(), user_string)).split()

# empty dictionary data base
db = {}

# removes duplicates as a constraint
new_string = set(user_string)
    
for i in new_string:
    
    # adds frequencies to the database dictionary
    db[i] = user_string.count(i)

# grabs second value in dict to sort by min, then reverse to switch to max
for i, j in sorted(db.items(), key = lambda x: x[1], reverse = True):

    # display's sorted dict
    print(f"{i} : {j}")


