# Dimensions of state space:
ACTIONS = 5
FREQS = 19
FREQ_IN_STATE=1
LABELS = [ 	\
		#'BMPKI', 
		#'IPC_u', 
		#'usage',
		'IPC_p', 
		'MPKI', 
		#'DAPKI',
		'temp', 
		#'power'
		]

# +1 for frequency added on the end.
VARS = len(LABELS) + FREQ_IN_STATE

# Array of bools sets log scale if true:
SCALING_DICT = \
{
	'BMPKI':False,
	'IPC_u':False,
	'usage':False,
	'IPC_p':False,
	'MPKI' :False,
	'temp' :False,
	'power':False,
}
SCALING = [SCALING_DICT[k] for k in LABELS]
BUCKETS = \
	{
	'BMPKI':10,
	'IPC_u':15,
	'usage':10,
	'IPC_p':15,
	'MPKI' :15,
	'temp' :20,
	'power':10,
	}
# Min and max limits are in linear scale
MINS = \
	{
	# Note 0..1s to avoid domain error on log scaled stats:
	#'BMPKI':0.1,a
	'usage':0.01,
	'IPC_u':0.01,
	'IPC_p':0.01,
	'MPKI':0.05,
	'temp':40,
	'power':0.1
	}
MAXS = \
	{
	#'BMPKI':80,
	'usage':1.2,
	'IPC_u':3,
	'IPC_p':3,
	'MPKI':3,
	'temp':60,
	'power':4
	}

#big cluster frequencies
big_freqs = [200000, 300000, 400000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000]
# freq to bin indices:
freq_to_bucket = {big_freqs[i]:i for i in range(len(big_freqs))}

EPSILON = 0.15
# Discounting factor:
GAMMA = 0.95
# Lambda for multistep Q-learning updates:
#LAMBDA = 0.6
ALPHA = 0.1
# Update period in seconds
PERIOD = 0.100
# Limit in celsius
THERMAL_LIMIT = 50
# Thermal limit coefficient
RHO = 100
# Power penalty coefficient
THETA = 500

