def size_val(size_str): 
    if 'S' in size_str: 
        return -(size_str.count('X')+1) 
    elif 'M' in size_str: 
        return 0 
    elif 'L' in size_str: 
        return size_str.count('X')+1 

inv_num = int(input())
inventory = input().split(maxsplit=inv_num)
req_num = int(input())
request = input().split(maxsplit=req_num)

# convert string inputs to values
# e.g. M->0, L->1, S->-1 
inv_val = [size_val(i) for i in inventory]
req_val = [size_val(i) for i in request] 


flag = 1
# if no. of requests > no. of inventories, must no 
if req_num > inv_num: 
    flag = 0
else: 
    # the max size of requests > max size of inventory, must no 
    if max(inv_val) < max(req_val): 
        flag = 0 
    else: 
        for r in req_val: 
            # all possible inventories can fulfill that request 
            fulfills = [j for j in inv_val if j>=r ]
            # if can't find fulfills 
            if len(fulfills) == 0: 
                flag = 0 
                break 
            # the minimum size that can fulfill the request 
            min_fulfill = min(fulfills)
            inv_val.remove(min_fulfill)  

if flag == 0: 
    print('No')
else: 
    print('Yes')
