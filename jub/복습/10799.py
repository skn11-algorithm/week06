
stick = input()
stack = []
cnt = 0

# () 일때 레이저로 잘림
# ( 가 나올 때 마다 스택에 추가 push
# ) 일 때 스택의 top이 ( 일 경우 레이저 있음 -> 레이저인 ( 제거후 남은 ( 개수만큼 조각 증가가
# ) 때 top 이 (가 아니면 쇠막대기 끝남 (를 pop하고 1 더함


for i in range(len(stick)):
    if stick[i] == "(":
        stack.append("(")
    else:
        if stick[i-1] == '(':
            stack.pop()
            cnt +=len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)
