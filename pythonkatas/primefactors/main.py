import sys
sys.path.append('~/workspace/CodeKatas/pythonkatas/src')
from src.primefactors import primeFactors

class main():
	int_to_factor = int(sys.argv[1])
	print (primeFactors(int_to_factor))
