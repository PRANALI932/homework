# Using function
# def prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# for num in range(2, 101):
#     if prime(num):
#         print(num)

#Using square root method
# import math

# for num in range(2, 101):
#     for i in range(2, int(math.sqrt(num)) + 1):
#         if num % i == 0:
#             break
#     else:
#         print(num)

#Using all() function
# for num in range(2, 101):
#     if all(num % i != 0 for i in range(2, num)):
#         print(num)

# Using any() function
for num in range(2, 101):
    if not any(num % i == 0 for i in range(2, num)):
        print(num)