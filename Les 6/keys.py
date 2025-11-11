# Maak het dictionary
mijn_dictionary = {
    "product": "softijs",
    "aantal": 101,
    "smaak": "vanille"
}

# Vraag alle sleutels (keys) op
keys = mijn_dictionary.keys()

# Print de sleutels
print(keys)

# Loop door alle sleutels en print ze
for item in mijn_dictionary:
    print(item)

for item in mijn_dictionary:
    print(mijn_dictionary[item])

for k, v in mijn_dictionary.items():
    print(k, v)