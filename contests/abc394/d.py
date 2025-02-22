S = input()

queue = []
for c in S:
    if queue and c == ")" and queue[-1] == "(":
        queue.pop()
    elif queue and c == "]" and queue[-1] == "[":
        queue.pop()
    elif queue and c == ">" and queue[-1] == "<":
        queue.pop()
    else:
        queue.append(c)

if len(queue) == 0:
    print("Yes")
else:
    print("No")
