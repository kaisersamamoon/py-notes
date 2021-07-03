
temes = [0]
tun = 1
while tun < 1001:
   if tun %3 ==0 or tun %17 ==0:
      temes.append(tun)
   tun =tun +1
print ( sum (temes))


tun = [0]
tee = 0
for i in range(0,1001) :
   if i %3 == 0 or i %17 == 0:
      tun.append(i)

print (sum(tun))

