# N = int(input())

# schedule = []
# for i in range(N):
#     start, end = map(int, input().split())
#     schedule.append((start, end))

test_case = open("./1931.txt", "r")
lines = test_case.readlines()
N = int(lines[0].strip())
schedule = []
for line in lines[1:]:
    start, end = [int(t) for t in line.strip().split()]
    schedule.append((start, end))
    
schedule.sort(key=lambda x: x[0])

last_time = max([time[1] for time in schedule])

storage = [-1 for _ in range(last_time + 1)]
storage[-1] = 0

def get_meeting_starts_at(t):
    return list(filter(lambda meeting: meeting[0] == t, schedule))
    
def max_after_time(t):
    if storage[t] != -1:
        return storage[t]
    meeting_list = get_meeting_starts_at(t)
    candidates = list(map(lambda meeting: max_after_time(meeting[1]) + 1, meeting_list))
    candidates.append(max_after_time(t + 1))
    max_meetings = max(candidates)
    storage[t] = max_meetings
    return max_meetings

print(max_after_time(0))
    
    
        
    
    
    
    