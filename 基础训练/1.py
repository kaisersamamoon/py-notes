temes = []
for i in range(1,5):
   for e in range(1,5):
      for h in range(1,5):
         if i != e and i != h and e != h:
            print (i,e,h)
            temes = temes.append (int(i,e,h))
