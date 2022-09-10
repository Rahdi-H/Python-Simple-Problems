def MergeTwoSortedArray(a, b):
    i = 0
    j = 0
    len1 = len(a)
    len2 = len(b)
    result = []
    while((i < len1) & (j > len2)):
        if(a[i] < b[j]):
            result.append(a[i])
            i += 1
        else: 
            result.append(b[j])
            j += 1
    while(i < len1):
        result.append(a[i])
        i += 1

    while(j < len2):
        result.append(b[j])
        j += 1
    return sorted(result)

a = [3, 4, 5, 2]
b = [8, 1, 7, 9]
c = MergeTwoSortedArray(a, b)
d =  sorted(a.join(b))
print(c)
print(d)
