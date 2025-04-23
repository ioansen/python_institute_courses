def is_prime(num):
    for d in range(2, num):
       if num % d == 0:
            return False
	
    return True

for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()