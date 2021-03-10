"""
다리를 지나는 트럭
https://programmers.co.kr/learn/courses/30/lessons/42583
큐
"""
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    num_truck = len(truck_weights)
    index = 0
    
    while index < num_truck:
        time += 1
        weight += bridge.popleft()
        
        if truck_weights[index] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights[index])
            weight -= truck_weights[index]
            index += 1
    
    return time + bridge_length
