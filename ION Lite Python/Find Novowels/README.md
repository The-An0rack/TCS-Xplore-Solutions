## Find Novowels

Create a function with the name **find\_Novowels** which takes a list of strings as input. The function checks each string of the list whether it has at least one vowel or not and returns another list containing the strings not having any vowel.

**Note:**

*   The check for the vowel should be case-insensitive .
*   You can use the below sample input and output to verify your solution.

**Sample Input:**

```plaintext
4
almost
vtyw
sound
prtwy
```

**Output:**

```plaintext
Strings without vowels:
vtyw
prtwy
```

The first line in the sample input is the count of strings to be included in the list to be passed to the method find\_Novowels .

The strings are then provided one by one as the next lines of input.

For more details, please refer to the below main section of code

You can use the below sample main section to test your code.

```python
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
```