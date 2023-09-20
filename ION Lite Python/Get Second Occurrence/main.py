# write your code here
def getIndex(inp_list, num):
    has_occurred = False

    for i in range(len(inp_list)):
        if inp_list[i] == num:
            if not has_occurred:
                has_occurred = True
            else:
                return i
    return 0

if __name__ == "__main__":
    count = int(input())
    inp_list = []

    for _ in range(count):
        inp_list.append(int(input()))
    
    num = int(input())
    print(getIndex(inp_list, num))