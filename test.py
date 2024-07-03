# a = [1, 2, 3, 4]

# def call_by_ref(l):
#     l[0] = 5

# call_by_ref(a)
# print(a)

a = (5, 3)
def call_by_val(l):
    l = 3
call_by_val(a)
print(a)