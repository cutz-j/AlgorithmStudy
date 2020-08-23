def solution(numbers, hand):
    coord = {1:(0, 0), 2:(0, 1), 3:(0, 2), 
             4:(1, 0), 5:(1, 1), 6:(1, 2),
             7:(2, 0), 8:(2, 1), 9:(2, 2),
             '*':(3, 0), 0:(3, 1), '#':(3, 2)}
    
    left, right = coord['*'], coord['#']
    left_list, right_list = [1,4,7], [3,6,9]
    answer = ''
    for n in numbers:
        if n in left_list:
            left = coord[n]
            answer += 'L'
        elif n in right_list:
            right = coord[n]
            answer += 'R'
        else:
            target = coord[n]
            left_dist = abs(left[0] - target[0]) + abs(left[1] - target[1])
            right_dist = abs(right[0] - target[0]) + abs(right[1] - target[1])
            if left_dist == right_dist:
                if hand == 'left':
                    left = target
                    answer += 'L'
                else:
                    right = target
                    answer += 'R'
            elif left_dist < right_dist:
                left = target
                answer += 'L'
            else:
                right = target
                answer += 'R'
    return answer