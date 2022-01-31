# 오아시스 재결합(3015번)
###############################################
    # 문제: https://www.acmicpc.net/problem/3015
    # 스택
    # 평범한 스택 문제라고 생각하고 덤볐다가 시간 엄청 깨졌다.
    # 현재 스택의 마지막에 들어있는 키보다 지금 들어오는 키가 클 경우, 작은 키가 나올 때까지 스택에서 요소들을 뺀다.
    # 빼면서 카운트+=1을 해주고, while문을 빠져나왔을 때, 스택이 비어있지 않을 경우에 추가적으로 카운트+=1을 해준다.(왜냐하면 스택의 마지막에 있는 키가 더 크기 때문에 한 쌍이 만들어지기 때문)
    # 그후, 스택에 현재 들어오려는 키를 append해준다(스택의 상태는 항상 오름차순을 유지하는 셈이다.)
    # 여기까지는 아무 문제 없으나, 문제는 키가 같은 값이 연속적으로 들어올 경우에 어떻게 처리해주느냐이다. 연속적으로 들어오는 값들에 대한 처리를 제대로 해줘야 문제를 통과할 수 있다.
    # 만약, 스택의 끝에서 부터 매번 연속적인지 판단하기 위해 완전 탐색을 진행한다면 분명 시간 초과가 날 것이다.
    # 하지만, 스택에 키에 대한 값만 넣는 것이 아니라, 연속적인 숫자가 몇번 나왔는지도 같이 넣어준다면, 그럴 필요 없이 추적이 가능하다.
    # 연속적인 숫자는 다 남길 필요없이 1번만 남기고 몇번 등장했는지만 체크해줌으로써, 나중에 그보다 큰 값이 들어올 경우, 누적 연속 등장횟수를 카운트에 +해주는 것이다.
###############################################
import sys
input=sys.stdin.readline
N=int(input())
stack=[]
cnt=0
for i in range(N):
    h=int(input()) # 현재 들어오려는 키
    tmp_cnt=1 # 연속 등장 횟수
    if not stack:
        stack.append([h,1])
    else:
        while stack and stack[-1][0]<=h: # 만약 stack[-1][0]의 값보다 현재 들어오려는 키의 값이 크거나 같은 동안
            last=stack.pop()
            cnt+=last[1] # 최종 횟수에 (누적) 등장 횟수를 더해줌(연속 누적이 없다면 해당값은 당연히 1임)
            if last[0]==h: # 만약 stack[-1][0]의 값이 현재 들어오려는 값과 같다면
                tmp_cnt+=last[1] # 연속 등장 횟수를 누적해줌
        if stack: # 스택이 비어있지 않다면 최종 횟수에 +1을 해줌(왜냐하면 남아있는 값고 들어오려는 값이 쌍을 이룰 수 있기 때문)
            cnt+=1
        stack.append([h,tmp_cnt])

print(cnt)
