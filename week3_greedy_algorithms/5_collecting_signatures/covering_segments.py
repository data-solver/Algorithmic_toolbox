# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


"""
start from furthest point to the left
go right on this line, till you arrive at the right edge of this line,
or till you arrive at the right edge of another line
draw a point at this location
remove all lines covered by this point from the list
repeat till all line segments are covered

pseudocode
sort segments by left value of each line segment from lowest to biggest
while loop
    start with first entry of sorted line segment loop
    put point at min(b0,b1...,bn)
    
    


#"""
#def optimal_points(segments):
#    points = []
#    #write your code here
#    for s in segments:
#        points.append(s.start)
#        points.append(s.end)
#    return points

def optimal_points(segments):
    points = []
    segments.sort()
    while True:
        a0 = segments[0][0]
        b0 = segments[0][1]
        point = a0
        old_point = a0
        indices = []
        for i, seg in enumerate(segments):
            if seg[0] >= a0 and seg[0] <= b0:
                point = seg[0]
                if seg[1] < b0:
                    b0 = seg[1]
#                print(f"point ={point}")
#                print(f"seg, a0, b0: {seg}, {a0}, {b0}")
            else:
                indices.append(i)
        points.append(point)
        temp = [segments[i] for i in indices]
        segments = temp
        if len(segments) == 0:
            break
    return points


def test_points(segments, points):
    wee_woo_list = []
    for seg in segments:
        passed = False
        for point in points:
            if point >= seg[0] and point <= seg[1]:
                passed = True
        if not passed:
            wee_woo_list.append(seg)
    return wee_woo_list
            

if __name__ == '__main__':
    input1 = sys.stdin.read()
    n, *data = map(int, input1.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#    segments1 = [[1, 3], [2, 5], [3, 6]]
#    segments2 = [[4, 7], [1, 3], [2, 5], [5, 6]]
    points = optimal_points(segments)
    print(len(points))
    print(*points)
