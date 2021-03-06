'''
# State space:
Core 4 branch misses per instruction
Core 4 instructions per cycle
Core 4 L2 misses per instruction
Core 4 temperature
Core 5 branch misses per instruction
Core 5 instructions per cycle
Core 5 L2 misses per instruction
Core 5 temperature
Core 6 branch misses per instruction
Core 6 instructions per cycle
Core 6 L2 misses per instruction
Core 6 temperature
Core 7 branch misses per instruction
Core 7 instructions per cycle
Core 7 L2 misses per instruction
Core 7 temperature
Big cluster power
Estimated big cluster leakage power
'''

# Dimensions of state space:
BUCKETS = 19
VARS = 18
FREQS = 19
# Epsilon
E = 0.01
# Update period in seconds
PERIOD = 0.050
# Limit in celsius
THERMAL_LIMIT = 68
RHO = 0.0

# Defined names for state space indices:
c4bm = 0 
c4ipc = 1
c4mpi = 2
c4dmemapi = 3
c5bm = 4 
c5ipc = 5
c5mpi = 6
c5dmemapi = 7
c6bm = 8 
c6ipc = 9
c6mpi = 10
c6dmemapi = 11
c7bm = 12 
c7ipc = 13
c7mpi = 14
c7dmemapi = 15
pwr = 16
lkpwr = 17

# Estimated ranges for each value type:
bmiss_MIN = 0.0
bmiss_MAX = 100.0 
ipc_MIN = 0.0
ipc_MAX = 3.0
mpi_MIN = 0.0
mpi_MAX = 50
dmemi_MIN = 0.0
dmemi_MAX = 4000
temp_MIN = 35.0
temp_MAX = 80.0
pwr_MIN = 0.00
pwr_MAX = 15.0

# Compute width of each bucket for each state dimension:
bmiss_width = (bmiss_MAX - bmiss_MIN) / BUCKETS
ipc_width = (ipc_MAX - ipc_MIN) / BUCKETS
mpi_width = (mpi_MAX - mpi_MIN) / BUCKETS
dmemi_width = (dmemi_MAX - dmemi_MIN) / BUCKETS
temp_width = (temp_MAX - temp_MIN) / BUCKETS
pwr_width = (pwr_MAX - pwr_MIN) / BUCKETS

def freq_to_bucket(freq):
	big_freqs = [2000000,1900000,1800000,1700000,1600000,1500000,1400000,1300000,1200000,1100000,1000000,900000,800000,700000,600000,500000,400000,300000,200000]	
	return big_freqs.index(int(freq))
