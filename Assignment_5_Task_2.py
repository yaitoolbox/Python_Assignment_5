
#Creating a list of numbers from 1 to 10

numbers = list(range(1, 11))

#Extracting the first five elements from the list

extract_list = numbers[:5]
reverse_list = extract_list[::-1]

#printing original list, extracted list and reversed list

print('Original List    >>', numbers)
print('\nExtracted List   >>', extract_list)
print('\nReversed List    >>', reverse_list)