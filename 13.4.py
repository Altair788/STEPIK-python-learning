def quick_merge(list1, list2):
    result = []
    p1 = 0
    p2 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append((list2[p2]))
            p2 += 1
    if p1 < len(list1):
        result += list1[p1:]
    if p2 < len(list2):
        result += list2[p2:]

    return result

list1 = []
list2 = []

n = int(input())
for i in range(n):
    s = [int(i) for i in input().split()]
    list2.extend(s)
    list1 = quick_merge(list1, list2)
    list2 = []
print(*list1)