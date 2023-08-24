# 백준 1251 단어 나누기

word = list(input())
answer = []
tmp = []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word) ):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(a + b + c)



for a in tmp:
    answer.append(''.join(a))

print(answer)
print(sorted(answer))

print(sorted(answer)[0])


# n = list(map(str, input()))

# arr = []
# arr2 = []
# arr3 = []

# value = []

# # print(n)

# for i in range(len(n)):
#     if  i < 3:
#         arr.append(n[i])

#     elif i >=3 and i < 6:
#         arr2.append(n[i])
    
#     else:
#         arr3.append(n[i])

# arr.reverse()
# arr2.reverse()
# arr3.reverse()

# for i in range(len(arr)):
#     value.append(arr[i])

# for i in range(len(arr2)):
#     value.append(arr2[i])

# for i in range(len(arr3)):
#     value.append(arr3[i])


# for i in value:
#     print(i, end = "")