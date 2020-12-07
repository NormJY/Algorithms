# programmers coding test practice:
# 연습문제 - 직사각형 별찍기

# 너무 간단한 문제라 부연설명은 하지 않아도 될 것 같습니다.
# 단지 입력을 받는 줄인 첫 번째 줄을 잘 기억해 두면 좋을 것 같습니다.

n, m = map(int, input().split(' '))

for i in range(m):
    print('*' * n)