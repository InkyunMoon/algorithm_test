n = int(input())
n = 3

d = [0] * 1000

d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, 1000):
    d[i] = 2 * (d[i-1] + 1)
    print(d[i])

d[3:10]

#
n = 3

d = [0] * 1000
d[0] = 0
d[1] = 1
d[2] = 3

for i in range(3, 1000):
    d[i] = (d[i-1] + d[i-2]*2) % 796796

d[3]