# # # Roy and Profile Picture

# # # # L = int(input())
# # # # N = int(input())

# # # # for i in range(N):
# # # #     W, H = map(int, input().split())
    
# # # #     if W < L or H < L:
# # # #         print("UPLOAD ANOTHER")
# # # #     elif W == H:
# # # #         print("ACCEPTED")
# # # #     else:
# # # #         print("CROP IT")





# # Monk and Rotation
# T = int(input())

# for i in range(T):
#     N, K = map(int, input().split())
#     arr = list(map(int, input().split()))
    
#     K = K % N   
    
#     result = arr[N-K:] + arr[:N-K]
    
#     print(*result)





# Toggle String
# s = input()
# ans = ""

# for x in s:
#     if x.isupper():
#         ans += x.lower()
#     elif x.islower():
#         ans += x.upper()

# print(ans)





# arr = [1,2,3,4,5,6]

# temp = arr[-1]   # last element

# for i in range(len(arr)-1, 0, -1):
#     arr[i] = arr[i-1]

# arr[0] = temp

# print(arr)