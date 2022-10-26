import sys

def Deadlock(res, req, alo):
    avail = res
    for i in range(len(req)):
        for j in range(len(res)):
            avail[j] -= alo[i][j]
    req_check = []
    for _ in range(len(req)):
        safe_check = True
        for i in range(len(req)):
            check = True
            for j in range(len(res)):
                if i in req_check or avail[j] < req[i][j]:
                    check = False
                    break
            if check:
                req_check.append(i)
                for j in range(len(res)):
                    avail[j] += alo[i][j]
                safe_check = False
                break
        if safe_check:
            print("System is not safe!")
            sys.exit()
    if len(req_check) == len(req):
        print("System is safe!")


len_p = int(input("Enter count of process: "))
len_r = int(input("Enter count of resource: "))

graph = [[0 for _ in range(len_r * 2)] for _ in range(len_p)]
resource = []

print("\nCount of Instance Resource: ")
print("----------------------------")
i = 0
while i < len_r:
    try:
        ins = int(input(f"R{i + 1} : "))
        resource.append(ins)
        i += 1

    except:
        print("input is wrong!!")

len_req = int(input("\nEnter count of requests: "))

print("Pi  -->  Rj")
print("-----------")
i = 0
while i < len_req:
    try:
        req = list(map(int, input("Pi Rj: ").split()))
        if len(req) != 2:
            print("input is wrong!!")
            continue
        i += 1
        graph[req[0] - 1][req[1] - 1] += 1

    except:
        print("input is wrong!!")

len_busy = int(input("\nEnter count of busy instance: "))

print("Ri  -->  Pj")
print("-----------")
i = 0
while i < len_busy:
    try:
        ins = list(map(int, input("Ri Pj: ").split()))
        if len(ins) != 2:
            print("input is wrong!!")
            continue
        i += 1
        graph[ins[1] - 1][len_r + ins[0] - 1] += 1

    except:
        print("input is wrong!!")

Deadlock(resource, [g[:len_r] for g in graph], [g[len_r:] for g in graph])

# sample
# 3
# 2
# 1
# 2
# 3
# 1 1
# 2 2
# 3 2
# 2
# 1 2
# 2 1

