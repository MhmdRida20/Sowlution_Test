#objective smallest number divisible by secquence from 1 to n 
# first i tried to iterate througt all the list butthis is unefficient i think this theirwill be a more effifcient solution 
# so i choose to iterate througt only the prime numbers and add 2 three time using a loop so the complexity will 
# decrease to logn i think or something like this it takes very more time buut i this it is more efficient and functional :)
  
def is_prime(n : int):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
"""
Noting that it seems that i forgot to push the last edit and forgot to save so during the evaluation 
i constate that their are something that should be changed already so i didnt figure it in this short 
periode of time this is why i remake some light changes 
Sorry in advance for this issue and thanks for your consideration 
!! The only changes are in this file - you can check if you want from the commits in the profile / vs-extention!!
"""

def smallest_positive_number(n : int):
    l_prime_nums = []
    i = 0
    long_number = 1


    if not n:
        return
    if n == 0:
        return (1)
    for i in range(2,n + 1 ):
        if is_prime(i):
            l_prime_nums.append(i)
    # for i  in range(len(l_prime_nums)):
    #     print(l_prime_nums[i])
    i = 0
    num = 0
    while num < len(l_prime_nums):
        #print(num ," loop")
        prime_power = 1
        tmp_pow = l_prime_nums[num]
        while tmp_pow <= n:
            prime_power = tmp_pow 
            tmp_pow = tmp_pow * l_prime_nums[num]
        long_number = long_number * prime_power
        num = num + 1
    #print("end for loop")
    return (long_number)

"""#main test"""
n = int(input("enter the number"))
print("smallest : ",smallest_positive_number(n))


#first try
    # while not found:
    #     for i in range(n):
    #         if long_number % l[i] == 0 :
    #             long_number = long_number * l[i]
    #         else:
    #             break
    #         if i == n:
    #             return 
