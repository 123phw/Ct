import sys

def solution(places):
	answer = []
	start=[]
	for i in range(5):
		for j in range(5):
			if places=[i][j]='P':
				start.append([i,j])

	for s in start:
		queue= deque([s])
		visited=[[0]*5 for i in range(5)]


		while queue:



    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

'''
https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL2-%EA%B1%B0%EB%A6%AC%EB%91%90%EA%B8%B0-%ED%99%95%EC%9D%B8%ED%95%98%EA%B8%B0-Python
�������� ��ġ�� start�� �߰���Ŵ
start���� �湮�������� ���� �湮�ϸ鼭 �ٸ� �����ڸ� ã�´�
�ٸ������ڸ� ã������ ������ ��ġ�� �ľ��Ѵ�. ���̰Ÿ��� 2�����̸� 0�� ��ȯ
start���� x�� ������ ���θ������̹Ƿ� �����
'''