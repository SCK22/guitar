import sys
import numpy as np
from constants import guitar_notes

def generate_sequence(num_sequences):
    seq = []
    for _ in range (num_sequences):
        n_notes = np.random.choice(range(4,13), 1)[0]
        seq.append([np.random.choice(guitar_notes) for i in range(n_notes)])
    return seq
    
for s in generate_sequence(int(sys.argv[1])):
    print(s)