## Check Palindrome

Create a function with the name `check_palindrome` which takes a list of strings as input. The function checks each string of the list whether it is a palindrome or not and returns another list containing the palindrome from the input string.

_**Note:**_  
_i. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam_  
_ii. The check for the string to be palindrome should be case-insensitive , e.g. madam and Madam both should be considered as palindrome._  
You can use the below sample input and output to verify your solution.

**Sample Input:**

```python
3
Hello
Malayalam
Radar
```

Output:

```plaintext
Malayalam
Radar
```

The first line in the sample input is the count of strings to be included in the list as the 1st input.  
The strings are then provided one by one as the next lines of input.  
For more details, please refer to the below main section of code  
You can use the below sample main section to test your code.

Sample Main Method:

```python
if name=='main':
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
```