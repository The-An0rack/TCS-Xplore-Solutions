def check_prime(num):
    if num <= 1:
        return 0
    elif num <= 3:
        return 1
    else:
        i = 2
        while i < num:
            if num % i == 0:
                return 0
            i += 1
        
        return 1

def prime_composite_list(inp):
    prime_list = []
    composite_list = []

    for num in inp:
        if check_prime(num) == 1:
            prime_list.append(num)
        else:
            composite_list.append(num)
    
    return [prime_list, composite_list]


if __name__=='__main__':
    inp=[]
    count=int(input())
    for i in range(count):
        inp.append(int(input()))
    print(check_prime(inp[1]))
    result=prime_composite_list(inp)
    print(result)