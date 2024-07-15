for x in range(1,4):
	print(('+' + '-'*10)*3 + '+')
	for y in range(1,10):	
		print("|", end='')	
		for z in range(x, 10, 3):
			print(f"{z} x {y} = {y*z:>2}", end='|')
		print()
print(('+' + '-'*10)*3 + '+')