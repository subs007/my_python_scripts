# removing duplicated from the list using naive methods
### appending to empty list
# initializing list
sam_list = [11, 13, 15, 16, 13, 15, 16, 11]
print("The list is: " + str(sam_list))

# remove duplicated from list
result = []
for i in sam_list:
    if i not in result:
        result.append(i)

    # printing list after removal
print("The list after removing duplicates : " + str(result))


=============================
#using set

# removing duplicated from the list using set()

# initializing list
sam_list = [11, 15, 13, 16, 13, 15, 16, 11]
print ("The list is: " + str(sam_list))

# to remove duplicated from list
sam_list = list(set(sam_list))

# printing list after removal
# ordering distorted
print ("The list after removing duplicates: " + str(sam_list))
