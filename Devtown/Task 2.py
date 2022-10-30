#Try your hand at working with nested dictionaries. Add another entry, 'is_noble_gas,' to each dictionary in the elements dictionary. After inserting the new entries you should be able to perform these lookups:

#print(elements['hydrogen']['is_noble_gas'])
#False

#print(elements['helium']['is_noble_gas'])
#True


elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H', 'Is_Noble': "False"},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He', "Is_Noble": "True"}}

print(elements['helium']["Is_Noble"])
print(elements['hydrogen']['Is_Noble'])


