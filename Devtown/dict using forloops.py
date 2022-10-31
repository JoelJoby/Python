from multiprocessing.sharedctypes import Value


cast = {
           "Joey Tribbiani": "Joey Tribbiani",
           "Monica Geller": "Chandler Bing",
           "Phoebe Buffay": "Mike Hannigan",
           "Ross Geller": "Rachel Green"
       }

for key in cast:
    print(key)

for key, value in cast.items():
    print("partner 1: {}  partner 2: {}".format(key,value))
