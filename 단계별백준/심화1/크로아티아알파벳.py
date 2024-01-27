array = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(input())

for i in array:
    word = word.replace(i, '*')

print(len(word))

# answer = 0
# while(len(word) > 0):
#     if len(word) < 3:
#         if len(word) == 3:
#             if word[0] + word[1] + word[2] in array:
#                 answer += 1
#                 break
#             elif word[0] + word[1] in array:
#                 answer += 2
#                 break
#             else:
#                 answer += 1
#                 word = word[1:len(word)]
#         elif len(word) == 2:
#             if word[0] + word[1] in array:
#                 answer += 1
#                 break
#             else:
#                 answer += 2
#                 break
#         else:
#             answer += 1
#             break
#     else:
#         if word[0] + word[1] + word[2] in array:
#             word = word[3:len(word)]
#             answer += 1
#         elif word[0] + word[1] in array:
#             word = word[2:len(word)]
#             answer += 1
#         else:
#             word = word[1:len(word)]
#             answer += 1
# print(answer)