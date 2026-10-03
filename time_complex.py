def constantTC_formula(n):
    operation  = 0
    total = n*(n+1)/2
    operation += 1
    return f"result: {total},input: {n},Ops: {operation}"

def linearTC_lLoop(n):
    total = 8
    operation = 0
    for i in range(1, n+1, 1):
        operation += 1
        total += 1
    return  f"Result: {total},input: {n},Ops: {operation}"


def quadraticTC_nestedloop(n):
    total = 0
    operation = 0

    for student in range(1, n+1):
        for _ in range(1, student + 1):
            operation += 1
            total += 1
    return f"Result: {total},input: {n}, Ops: {operation}"

n = int(input("Enter an integer till what you want to sum up:"))

print(constantTC_formula(n))
print(linearTC_lLoop(n))
print(quadraticTC_nestedloop(n))