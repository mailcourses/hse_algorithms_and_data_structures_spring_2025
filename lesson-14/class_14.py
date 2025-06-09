
import time


def Fibonacci_rec(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return Fibonacci_rec(n-1) + Fibonacci_rec(n-2)


# start_time = time.time()
# Fibonacci_rec(35)
# stop_time = time.time() - start_time
# print(stop_time)


# n = 3

def Fibonacci_rec_memo(n, data_structure = None):
    if data_structure is None:
        data_structure = {0: 0, 1: 1}

    if n in data_structure:
        return data_structure[n]
    
    cur = Fibonacci_rec_memo(n-1, data_structure) + Fibonacci_rec_memo(n-2, data_structure)
    data_structure[n] = cur
    return data_structure[n]

# start_time = time.time()
# print(Fibonacci_rec_memo(900))
# stop_time = time.time() - start_time
# print(stop_time)




# ladder
def ladder(n: int, current: int = 1):
    if current == n:
        return 1
    if current > n:
        return 0
    return ladder(n, current + 1) + ladder(n, current + 2)


assert ladder(3) == 2
assert ladder(4) == 3
assert ladder(5) == 5
assert ladder(6) == 8
assert ladder(7) == 13

print("ladder ok")



# [1, 4, 0, 5, 1, 0, 0] -> True
# [1, 4, 0, 1, 1, 0, 0] -> False
# [1, 0, 0, 5, 1, 0, 0] -> False

def last_el_finder(data):
    cur = 0
    for i in range(len(data)):
        if cur >= i:
            cur = max(cur, i + data[i])
        else:
            break
            
    return True if cur >= len(data) - 1 else False 
    
    
assert last_el_finder([1, 4, 0, 5, 1, 0, 0])
assert not last_el_finder([1, 4, 0, 1, 1, 0, 0])
assert not last_el_finder([1, 0, 0, 5, 1, 0, 0])


print("jumps ok")



# [1,8,6,2,5,4,8,3,7] == 49

def max_A(data: list) -> int:
    n = len(data)
    left = 0
    right = n - 1
    max_sq = 0
    while left < right:
        max_sq = max(max_sq, min(data[left], data[right]) * (right - left))
        if data[left] < data[right]:
            left += 1
        else:
            right -= 1
    return max_sq



assert max_A([1,8,6,2,5,4,8,3,7]) == 49

print("max_A ok")


# [1,8,6,2,5,4,8,3,7], k=10




# [1, 2, 10, 3] - [60, 30, 6, 20]
# [1, 2, 10, 3, 0] - [0, 0, 0, 0, 60]
# [0, 2, 10, 3, 0] - [0, 0, 0, 0, 0]

def multiple_calcalations(data):
    general_multiple = 1
    zero_counter = 0
    for i in data:
        if i == 0:
            zero_counter += 1
            continue
        
        general_multiple *= i

    res = []
    
    for i in data:
        if i != 0:
            if zero_counter == 0:
                res.append(general_multiple // i)
            else:
                res.append(0)
        elif zero_counter > 1:
            res.append(0)
        else:
            res.append(general_multiple)
    return res



assert multiple_calcalations([1, 2, 10, 3]) == [60, 30, 6, 20]
assert multiple_calcalations([1, 2, 10, 3, 0]) == [0, 0, 0, 0, 60]
assert multiple_calcalations([0, 2, 10, 3, 0]) == [0, 0, 0, 0, 0]

print("mult ok")



def multiple_calcalations_ver_2(data):
    cur_multiple = 1
    multiplies = []
    for i in range(len(data)):
        multiplies.append(cur_multiple)
        cur_multiple *= data[i]
    
    cur_multiple = 1
    for i in range(len(data)-1, -1, -1):
        multiplies[i] *= cur_multiple
        cur_multiple *= data[i]
    
    return multiplies
        
        

assert multiple_calcalations_ver_2([1, 2, 10, 3]) == [60, 30, 6, 20]
assert multiple_calcalations_ver_2([1, 2, 10, 3, 0]) == [0, 0, 0, 0, 60]
assert multiple_calcalations_ver_2([0, 2, 10, 3, 0]) == [0, 0, 0, 0, 0]

print("mult ok v2")







    