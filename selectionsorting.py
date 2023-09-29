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
    j= 0 

    # Initialize variable named big that will be used 
    # to store the index of the biggest value 
    big = 0 

    # initialize varibale named temp that will be used 
    # to swap list values 
    tempgrades = 0 
    tempnames = 0 

    # loop trhrough list as many times as specified by 
    # len(data) and first 
    # this loop represents the blue arrow 
    while (i > 0 ):
        # set big equal to first
        big = first  

        # set j equal to first + 1 
        j = first + 1 

        # loop through list starting with element at
        # first + 1 and continue until reach first + i 
        # this loop represents the yellow arrow 
        while (j <= first + i ):
            # if the value in data[big] is less than 
            # data[j]
            if (grades[big] > grades[j]): 
                # set big equal to j 
                big = j 
            # Increment j by 1 
            j += 1 

        # swap the data in first + i with the data in big 
        # set temp to value in data[first + i]
        tempgrades = grades[first+ i]
        tempnames = names[first+ i]

        #set data[first+i] to value in data[big]
        grades[first+i] = grades[big]
        names[first+i] = names[big]  

        # set data[big] to value in temp
        grades[big] = tempgrades
        names[big] = tempnames
    
        # decrement i by 1
        i -= 1 



