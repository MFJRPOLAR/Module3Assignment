from selectionsortingdecreasing import * 

def main():
    i = 0 
    first = 0 
    names = ['Emma', 'Brian', 'Evelyn', 'Franks', 'Alex', 'Felecia', 'Carl']
    grades = ['A','B','D','C','A','F','B']


    print('ORIGINAL LISTS')
    print('Names \t Grades')
    for i in range(len(names)): 
        print(f"{names[i]}\t   {grades[i]}")

    # call sort method
    sort(names,grades,first)

    print()

    print('SORTED LISTS')
    print('Names \t Grades')
    for i in range(len(names)): 
        print(f"{names[i]}\t   {grades[i]}")

if __name__ == "__main__":
    main()