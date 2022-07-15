import sys
from collections import deque


def bfs(p):
	start=[]
	for i in range(5):
		for j in range(5):
		    if p[i][j]=='P':
		        start.append([i,j])

	for s in start:
        queue= deque([s])
        visited = [[0]*5 for i in range(5)]   # �湮 ó�� ����Ʈ
        distance = [[0]*5 for i in range(5)]  # ��� ���� ����Ʈ
        visited[s[0]][s[1]] = 1

		while queue:
            x,y=queue.popleft()
            
            dx=[0,0,-1,1]
            dy=[-1,1,0,0]

            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]

                if 0<=nx<5 and 0<=ny<5 and visited[nx][ny]==0: #��ǥ�� �������� �ش�Ǹ�

                    if p[nx][ny]=='O':
                        queue.append([nx,ny])
                        visited[nx][ny]=1
                        distance[nx][ny]=distance[x][y]+1

                    if p[nx][ny]=='P' and distance[x][y]<=1:
                        return 0
    return 1

def solution(places):
    answer=[]

    for i in places:
        answer.append(bfs(i))

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)

'''
https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
�������� ��ġ�� start�� �߰���Ŵ
start���� �湮�������� ���� �湮�ϸ鼭 �ٸ� �����ڸ� ã�´�
�ٸ������ڸ� ã������ ������ ��ġ�� �ľ��Ѵ�. ���̰Ÿ��� 2�����̸� 0�� ��ȯ
start���� x�� ������ ���θ������̹Ƿ� �����
'''