# 문제) 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력) 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력) 첫째 줄에 A+B를 출력한다.

A, B = input().split()  # 한 번에 두 가지를 입력 받을 때는 split()를 함께 쓰면 됨.

A = int(A)
B = int(B)

if A < 0 and B < 10:
    print("A는 0보다 큰 수를 입력해주세요.")
elif A < 0 and B > 10:
    print("A는 0보다 큰 수, B는 10보다 작은 수를 입력해주세요.")
elif A > 0 and B > 10:
    print("B는 10보다 작은 수를 입력해주세요.") 
else:
    print(A + B)

# split() -> 공백을 기준으로 나눔