#objective smallest number divisible by secquence from 1 to n 
# first i tried to iterate througt all the list butthis is unefficient i think this theirwill be a more effifcient solution 
# so i choose to iterate througt only the prime numbers and add 2 three time using a loop so the complexity will 
# decrease to logn i think or something like this it takes very more time buut i this it is more efficient and functional :)
  
def is_prime(n : int):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def smallest_positive_number(n : int):
    l_prime_nums = []
    i = 0
    j = 0
    long_number = 1
    tmp_n = n

    if not n:
        return
    if n == 0:
        return (1)
    for i in range(1,n):
        if is_prime(i):
            l_prime_nums.append(i)
            j = j + 1
    # for i  in range(len(l_prime_nums)):
    #     print(l_prime_nums[i])
    i = 0
    num = 1
    while num < len(l_prime_nums):
        #print(num ," loop")
        if(tmp_n % l_prime_nums[num] == 0):
            while tmp_n % l_prime_nums[num] == 0:
                tmp_n = tmp_n / l_prime_nums[num]
                long_number = long_number * l_prime_nums[num]
                #print("longNum" , long_number)
            #print("end while loop")
        else:
            #print("not divisible by ", l_prime_nums[num])
            long_number = long_number * l_prime_nums[num]

        num = num + 1
    #print("end for loop")
    return (long_number)

"""#main test

n = int(input("enter the number"))
print("smallest : ",smallest_positive_number(n))
"""

#first try
    # while not found:
    #     for i in range(n):
    #         if long_number % l[i] == 0 :
    #             long_number = long_number * l[i]
    #         else:
    #             break
    #         if i == n:
    #             return 
