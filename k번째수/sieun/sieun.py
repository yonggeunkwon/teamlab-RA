array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

for i in commands:
    left = i[0] - 1
    right = i[1]
    num = i[2] - 1

    arr = array[left:right]
    arr.sort()

    answer.append(arr[num])

print(answer)
