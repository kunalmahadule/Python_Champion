def Print_First_k_element():
    a = [1, 7, 4, 3, 4, 8, 7, 7, 3, 1, 4]
    n = len(a)
    k = 3
    dic = {}

    for i in a:
        if i not in dic:
            dic[i] = 1
            if dic.get(i) == k:
                return i

        else:
            dic[i] += 1
            if dic.get(i) == k:
                return i
    return -1


out = Print_First_k_element()
print(out)
