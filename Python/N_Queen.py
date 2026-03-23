N = int(input())

def dfs(st):
    if len(check_list) == L:
        v = 0
        c = 0
        for i in check_list:
            if i in vowel:
                v+=1
            else:
                c+=1
        
        if v >= 1 and c >= 2:
            print("".join(check_list))
        return
        

    for i in range(st, len(C_list)):
        check_list.append(C_list[i])
        dfs(i+1)
        check_list.pop()

dfs(0)
