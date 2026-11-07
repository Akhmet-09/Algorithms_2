import random
# n = int(input())
# numbers = [
#     random.randint(1,100) for _ in range(n)
# ]
# target = int(input())
# for i in range(len(numbers)):
#     if numbers[i] == target :
#         print(f"Found at index : {i}")
#         break
#     else:
#         print(numbers) 
# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target :
#             return i 
#     return -1 
# numbers = [1,2,3,4,5,6,7,8,9]   
# print(linear_search(numbers,10)) 



# def binary_search(arr,target):
#     left = 0 
#     right = len(arr) - 1 
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid] == target :
#             return mid 
#         elif arr[mid] < target :
#             left = mid + 1
#         else:
#             right = mid -1 
#     return -1
# numbers = [518,48,561984,189]        
# print(binary_search(numbers,48))          

# def binary_search(arr,target):
#     left = 0 
#     right = len(arr) - 1
#     while left <= right :
#         mid = (left+right)//2
#         if arr[mid] == target :
#             return mid 
#         elif arr[mid] < target :
#             left = mid +1 
#         else:
#             right = mid -1 
#     return -1
# numbers = [random.randint(1,100) for _ in range(9)]
# print(binary_search(numbers,36))        



# Ex 1 
# def linear_search(arr,target):
#     for i in range(len(arr)):
#         if arr[i] == target :
#             return i 
#     return -1
# numbers = [1,2,4,5,6,7,8,9]
# print(linear_search(numbers,5))

# Ex 2 
# def count_target(arr,target):
#     count = 0 
#     for i in range(len(arr)):
#         if arr[i] == target : 
#             count += 1 
#     return count 
# numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,89,1,5,1,45,1,] 
# print(count_target(numbers,1))   

# Ex 3 unsolved 
# def find_max(arr,largest):
#     left = 0 
#     right = len(arr) - 1
#     while left <= right :
#         mid = (left+right)//2
#         if arr[mid] == largest:
#             largest = mid 
#         elif arr[mid] < largest :
#             left = mid +1
#         else:
#             right = mid -1 
#     return largest 
# numbers = [1,2,3,4,5,6,7]        
# print(find_max(numbers,5))

# Ex 4 
# def binary_search(arr,target):
#     left = 0
#     right = len(arr) - 1 
#     while left <= right :
#         mid = (left+right)//2
#         if arr[mid] == target :
#             return mid
#         elif arr[mid] < target : 
#             left = mid + 1
#         else:
#             right = mid - 1 
#     return -1
# numbers = sorted([1568,5618,32184,184,318,21,1654,54])        
# print(binary_search(numbers,21))
# print(numbers)

# Ex 3 
# def find_max(arr):
#     largest = arr[0]
#     largest_index = 0
#     for x in range(1,len(arr)):
#         if arr[x] > largest:
#             largest = arr[x]
#             largest_index = x
#     return f"Largest Number : {largest}\nIndex : {largest_index}" 
# numbers = [51,5158,151,0,651,11,20651]  
# print(find_max(numbers))      


# Ex 5 
# def find_min(arr):
#     smallest = arr[0]
#     index = 0
#     for i in range(1,len(arr)):
#         if arr[i] < smallest : 
#             smallest = arr[i]
#             index = i 
#     return f"Smallest : {smallest}\nIndex : {index}"        
# numbers = [141,189,129841,129841,1984,15109,4]
# print(find_min(numbers))

# Ex 6 
# def first_occurrence(arr, target):
#     left = 0
#     right = len(arr) - 1
#     result = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             result = mid
#             right = mid - 1
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return result
# arr = [1, 2, 5, 5, 5, 7, 9]
# print(first_occurrence(arr, 4))

# def even_div(n):
#     divissors = []
#     even = []
#     for i in range(1,n+1):
#         if n % i == 0 : 
#             divissors.append(i)
#             for div in divissors :
#                 if div % 2== 0:
#                     even.append(div)
#                     return len(even)+1
# print(even_div(8))

# ex 6 
# def duplicate_target(arr,target):
#     left = 0 
#     right = len(arr) -1
#     result = -1 
#     while left<=right:
#         mid = (left+right)//2
#         if arr[mid] == target :
#             result = mid 
#             right = mid - 1 
#         elif arr[mid] < target :
#             left = mid + 1 
#         else:
#             right = mid - 1
#     return result 

# numbers = [1,2,3,5,4,1,1,5,1,5,4,9]        
# print(duplicate_target(numbers,1))

# # Ex 7 
# def last_target(arr,target):
#     left = 0
#     right = len(arr) - 1 
#     result = - 1
#     while left <=right :
#         mid = (left+right)//2
#         if arr[mid] == target :
#             result = mid 
#             left = mid +1 
#         elif arr[mid] < target :
#             left = mid  + 1 
#         else:
#             left = mid - 1 
#     return result 
# arr = [1, 2, 5, 5, 5, 7, 9]        
# print(last_target(arr,5))

# First Occurance 
def first_target(arr,target):
    left = 0 
    right = len(arr) - 1 
    result = -1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target :
            result = mid 
            right = mid - 1 
        elif arr[mid]<target:
            left  = mid + 1
        else:
            right = mid - 1
    return result 
numbers = [1,2,3,4,5,6,4,5,6,8]        
print(first_target(numbers,4))








