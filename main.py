import time, sys, math

primes = [2]

def isPrime(x):
  for n in range(2, int(math.sqrt(x)) + 1):
      if x % n == 0:
          return False
  return True

print('Prime number claculator, by Asa Alaniz.')
print('Please enter the prime number you would like to calculate:')
num = int(input())
iteration = 3
start_time = time.time()
while True:
    if isPrime(iteration):
        primes.append(iteration)
        if len(primes) == num:
            print('Calculated in', round(time.time() - start_time, 5), 'seconds. Your number:', primes[len(primes)-1])
            sys.exit()
    iteration += 2

# Calculated the 100,000nth prime number in 5.07701 seconds.
# Calculated the 1000th prime number in 0.00489 seconds.
# Calculated the 10,000th prime number in 0.14055 seconds.