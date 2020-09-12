# Make a Lambda function for capitalizing the whole sentence passed using arguments.
# And map all the sentences in the List, with the lambda functions

lst = ["hey this i sagar","i am from thane"]

print("\nOriginal list : \n")

print(lst)

result = list(map(lambda words: " ".join([word.capitalize() for word in words.split( )]) ,lst))

print("\nCapitalized list is : \n")

print(result)