from itertools import combinations

def solution(orders, course):
    answer = []
    order_combinations = [] #orders�迭�� �ߺ����� ������ ������ ����Ʈ
    order_dict = {} #����� ������ ������ ��ųʸ�

    for c in course: #�ڽ�[2,3,4]��� ���������� orders ������ ������ ������
        for order in orders:
            order_combinations.extend(list(map(''.join, combinations(order,c)))) # append��� extends�� �����ν� [[1,2],1,2]ó�� ������� �ʰ� []������ '[]'��ȣ�� �����Ͽ� ������

        for order_combination in order_combinations: #������ ����Ž���ϸ鼭 �ش� ������ ��ųʸ��� ������ 1�� �߰��ϰ� �ƴϸ� ��ųʸ��� �߰�
            if order_combination in order_dict:
                order_dict[order_combination]+=1
            else:
                order_dict[order_combination]=1
        answer.append(k for k,v in order_dict.items if max(order_dict.values()) == v)
    print(answer)  
    return answer

orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders,course)

'''
https://velog.io/@jwisgenius/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LV2-%EB%A9%94%EB%89%B4-%EB%A6%AC%EB%89%B4%EC%96%BC
'''