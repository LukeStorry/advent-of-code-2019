asteroid_locations = [(x,y) for y, line in enumerate(open('./input.txt').read().split('\n')) for x, char in enumerate(line) if char=="#"]

def detections(a):
    return len(set(math.atan2(a[1]-y,a[0]-x) for x,y in asteroid_locations))

print(max(map(detections, asteroid_locations)))

