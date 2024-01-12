import sys
input = sys.stdin.readline

N = input()
weight_limits = list(map(int, input().split()))

M = input()
weights = list(map(int, input().split()))

class Rail():
    weight_limit = 0
    num = 0
    assigned = 0
    
    def Rail(self, limit, num):
        self.weight_limit = limit
        self.num = num

def main():
    weight_limits.sort()
    weights.sort()
    
    if (weight_limits[-1] < weights[-1]):
        print("-1")
        return
    
    rails = []
    rails.append(Rail(weight_limits[0], 1))    
    for weight_limit in weight_limits[1:]:
        if weight_limit == rails[-1].weight_limit:
            rails[-1].weight_limit += 1
        else:
            rails.append(Rail(weight_limit, 1))
    
    idx = 0
    for weight in weights:
        while weight > rails[idx].weight_limit:
            idx += 1
        rails[idx].assigned += 1
    
    rails.reverse()
    time = 0
    remain = M
    while remain > 0:
        for rail in rails:
            if rail.num <= rail.assigned:
                rail.assigned -= rail.num
                remain -= rail.num
            else:
                remain -= rail.assigned
                # 크레인을 다음으로 옮기기!!
                
        time += 1

    
    print(time)

main()