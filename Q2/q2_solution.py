class Record(object):  # defind record class 
    def __init__(self, id, is_valid, error_message): 
        self.id = id 
        self.is_valid = is_valid  
        self.error_message = error_message

records = [] 
with open('./Q2/input.txt', 'r') as f:
    n = int(f.readline())
    for _ in range(n): 
        line = f.readline() 
        tmp = line.replace('\n','').split(' ')
        if tmp[1] == 'true': 
            is_valid = True 
        if tmp[1] == 'false': 
            is_valid = False
        if len(tmp) == 3: 
            # print(tmp[0],is_valid,tmp[2])
            rec = Record(tmp[0],is_valid,tmp[2])
        elif len(tmp) == 2: 
            # print(tmp[0],is_valid,None)
            rec = Record(tmp[0],is_valid,None)
        records.append(rec)

all_valid = True
error_codes = []
for rec in records:
    if rec.is_valid is not True:
        all_valid = False
        error_codes.append(rec.error_message)

if all_valid is True:
    print("Yes")
else:
    print("No")
    print(*error_codes, sep = ' ')