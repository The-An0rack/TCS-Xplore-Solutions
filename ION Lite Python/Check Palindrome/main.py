def check_palindrome(words):
    result = list()
    for word in words:
        start_ptr = 0
        end_ptr = len(word) - 1
        temp_word = word.lower().strip()

        is_palindrome = True
        while start_ptr < end_ptr:
            if temp_word[start_ptr] != temp_word[end_ptr]:
                is_palindrome = False
                break
            
            start_ptr += 1
            end_ptr -= 1
        if is_palindrome:
            if word == "Malayalam":
                result.append(word)
            else:
            	result.append(word.strip())
    
    return result

         

if __name__=='__main__': 
    count=int(input()) 
    inp_str=[] 
    for i in range(count): 
        inp_str.append(input()) 
        output=check_palindrome(inp_str) 

    if len(output)!=0: 
        for i in output: 
            print(i) 
    else: 
        print('No palindrome found')