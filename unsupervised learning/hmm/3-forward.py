import numpy as np

def forward(Observation, Emission, Transition, Initial):
    T = Observation.shape[0] # Total time steps
    N = Emission.shape[0]    # Number of Hidden States
    
    # F[i, t] is the probability of being in state i at time t
    F = np.zeros((N, T))

    # 1. Initialization (t = 0)
    # Probability of starting in state i AND seeing the first observation
    for i in range(N):
        F[i, 0] = Initial[i] * Emission[i, Observation[0]]
    
    # 2. Recursion (t = 1 to T-1)
    for t in range(1, T):
        for i in range(N):
            # Sum the probabilities of coming from any previous state j
            prev_prob_sum = 0
            for j in range(N):
                prev_prob_sum += F[j, t-1] * Transition[j, i]
            
            # Multiply by the probability of the current observation
            F[i, t] = prev_prob_sum * Emission[i, Observation[t]]

    # 3. Termination
    # The total probability of the sequence is the sum of the last column
    P = np.sum(F[:, T-1])
    
    return P, F