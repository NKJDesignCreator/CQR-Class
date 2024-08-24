#Q2. Given an integer array return the second largest and smallest elements

def find_len(list1):
    length = len(list1)
    list1.sort()
    print("Second Largest element is:", list1[length-2])
    print("Second Smallest element is:", list1[1])

list1=[12, 60, 24, 48, 36, 20, 84, 72, 4]
Largest = find_len(list1)
