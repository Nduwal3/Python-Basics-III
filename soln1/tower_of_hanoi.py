def TowerOfHanoi(num , from_rod, to_rod, aux_rod):
   if num == 1:
      print ("Move disk 1 from rod",from_rod,"to rod",to_rod)
      return
   TowerOfHanoi(num-1, from_rod, aux_rod, to_rod)
   print ("Move disk",num,"from rod",from_rod,"to rod",to_rod)
   TowerOfHanoi(num-1, aux_rod, to_rod, from_rod)


num = 3
TowerOfHanoi(num, 'rod_a', 'rod_c', 'rod_b')
