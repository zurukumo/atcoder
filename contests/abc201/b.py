N = int(input())
ST = [input().split() for _ in range(N)]

ST.sort(key=lambda x: int(x[1]), reverse=True)
print(ST[1][0])

# JS
# let st = [
#     ['Fuji', 3776],
#     ['Everest', 8849]
# ]
# st.sort((a, b) => a[1] - a[0])
# st.sort((a, b) => a[0] - a[1])  //逆順

# Ruby
# st = [
#     ['Fuji', 3776],
#     ['Everest', 8849]
# ]
# st.sort{ |a, b| a[1] > a[0] }
# st.sort{ |a, b| a[1] < a[0] } //逆順
