def find_Novowels(inp_str):
    result = list()
    vowels = ["a", "e", "i", "o", "u"]

    for word in inp_str:
        contains_vowel = False
        for char in word:
            if char in vowels:
                contains_vowel = True

        if not contains_vowel:
            result.append(word)
    
    return result



if __name__=='__main__':
    count=int(input())
    inp_str=[]
    for i in range(count):
        inp_str.append(input())
    output=find_Novowels(inp_str)
    if len(output)!=0:
        print('Strings without vowels:')
        for i in output:
            print(i)
    else:
        print('No string found')
              