import sys
import math
#sys.stdin=open("input.txt", "rt")
import heapq
import itertools
import re
from collections import deque

def solution(s):
    answer=[]
    delete_num=0
    n=0
    c=len(s) #s�ѱ��� = 12
    while s!="1":
        n+=1
        c=len(s)-s.count('0') #s����-0�ǰ���=6
        delete_num+=s.count('0'); #0�� ����=6
        s="{0:b}".format(c) #������ȯ

    return [n,delete_num]

s="110010101001"
solution(s)