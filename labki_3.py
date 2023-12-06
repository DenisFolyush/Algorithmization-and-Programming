# 012345
# ("cat   ", 0
#  " salad", 1
#  " kiwi ", 2
#  "  r   ") 3

C = ("cat   ",
     " salad",
     " kiwi ",
     "  r   ")
C_max = len(C)

print(f"C_max = {C_max}")
result_list = []
result_letter = ""
i = 0

W_max = len(C[0])

# print(C[0][0])
for i in range(W_max):
    for row in range(C_max):
        # for stowp in range(W_max):
        letter = C[row][i]
        if letter == " ":
            pass
        else:
            print(f"ахуєть не пробел, а буква: {letter}")
            result_letter = result_letter + letter
    i = + 1
    result_list.append(result_letter)
    result_letter = ""
print(result_letter)
print(result_list)
a = max(result_list)
print(a)
# for word in C:
#     word_len = len(word)
#     letter = word[i]
#     if letter == " ":
#         pass
#     else:
#         print(f"ахуєть не пробел, а буква: {letter}")
#     if i <= word_len:
#         i += 1
