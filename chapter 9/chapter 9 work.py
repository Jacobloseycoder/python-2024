def w1():
    # Initialize an empty dictionary
    dic = {}
    
    # Open the 'bill.txt' file for reading (contains the message)
    coded = open('bill.txt', 'r')
    
    # Open the 'code.txt' file for reading (contains the encoding or key)
    encode = open('code.txt', 'r')
    
    # Iterate over each line in 'bill.txt' (message content)
    for line in encode:
        # Strip any leading/trailing whitespace from the line
        line = line.strip()
        
        # Assuming each line in 'bill.txt' could be a key-value pair (e.g., 'item1:value1')
        if ":" in line:
            key, value = line.split(":", 1)
            
            # Use the 'encodd' (from 'code.txt') as a modifier for the value
            modified_value = value  # Append the encoding or transformation
            
            # Add the key and modified value to the dictionary
            dic[key] = modified_value
    
    # Close the files
    coded.close()
    encode.close()
    
    # Print the resulting dictionary (key-value pairs with encoded values)
    print(dic)
