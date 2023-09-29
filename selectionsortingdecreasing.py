def sort(names, grades, first: int):
    """Sorts a list of grades from largest to smallest and 
    sorts the list of names according to the order defined by 
    the sorted grades

    Args:
        names : list of names
        grades: list of grades
        first (int): the list index atwhich the sort will begin 
    """      

    #Intialize loop counter variable named i 
    i = len(grades) - first - 1 

    # initialize loop counter variable named j to 0 
    j = 0 

    # Initialize variable named small that will be used 
    # to store the index of the smallest value 
    small = 0 

    # initialize varibale named temp that will be used 
    # to swap list values 
    tempgrades = 0 
    tempnames = 0 

    # loop through list as many times as specified by 
    # len(data) and first 
    # this loop represents the blue arrow 
    while (i > 0 ):
        # set small equal to first
        small = first  

        # set j equal to first + 1 
        j = (first + 1)

        while (j <= first + i ):
          
            if (grades[small] > grades[j]): 
                
                small = j 
            
            j += 1 

        # swap the data in first + i with the data in small 
        # set temp to value in data[first + i]
        tempgrades = grades[first + i]
        tempnames = names[first+ i]

        #set data[first+i] to value in data[small]
        grades[first+i] = grades[small]
        names[first+i] = names[small]  

        # set data[small] to value in temp
        grades[small] = tempgrades
        names[small] = tempnames
    
        # decrement i by 1
        i -= 1 
