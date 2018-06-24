import numpy as np
import random
import matplotlib.pyplot as plt
from neurodynex.hopfield_network import network, pattern_tools, plot_tools

add_extra = False

# the letters we want to store in the hopfield network
letter_list = ['N', 'C', 'B', 'S', 'X', 'Y' ]
extra = [ 'P', 'Q' ]
if add_extra == True:
    letter_list += extra

nRows, maxCols = 4, len(letter_list)
abc_dictionary = pattern_tools.load_alphabet()

def add_noise( letter, noise_level = 0.2 ):
    pat = abc_dictionary[letter]
    print( "[INFO ] Adding noise (level=%f) to %s" % (noise_level, letter))
    #  input( "Press any key to continue" )
    #  print( "  to %s" % letter )
    for (i, j), v in np.ndenumerate(pat):
        if random.random() < noise_level:
            pat[i, j] = random.choice( [-1, 1] )
    return pat

def main( plot = True ):
    # set a seed to reproduce the same noise in the next run
    # numpy.random.seed(123)
    
    # access the first element and get it's size (they are all of same size)
    pattern_shape = abc_dictionary['A'].shape

    # create an instance of the class HopfieldNetwork
    hopfield_net = network.HopfieldNetwork( 
            nr_neurons = pattern_shape[0]*pattern_shape[1]
            )
    
    pattern_list = [abc_dictionary[key] for key in letter_list ]

    if plot:
        plt.figure( figsize=(12, 6) )
        for i, a in enumerate(pattern_list):
            ax = plt.subplot( nRows, maxCols, i+1)
            ax.imshow( a )
            ax.axis('off')
    
    # store the patterns
    hopfield_net.store_patterns(pattern_list)
    print( "[INFO ] Saved patterns into hopfield network." )
    
    # create a noisy version of a pattern and use that to initialize the network
    l = random.choice( letter_list )

    noise_level = 0.5
    if add_extra:
        noise_level = 0.1
        print( '[INFO] More patterns than net can handle. Catastrophic'
            ' forgetting going to happen.'
        )
    noisy_init_state = add_noise( l, noise_level= noise_level)

    hopfield_net.set_state_from_pattern(noisy_init_state)
    
    # from this initial state, let the network dynamics evolve.
    states = hopfield_net.run_with_monitoring(nr_steps=4)

    # each network state is a vector. reshape it to the same shape used to create the patterns.
    states_as_patterns = pattern_tools.reshape_patterns(states, pattern_list[0].shape)

    if plot:
        for i, pat in enumerate( states_as_patterns ):
            overlap_list = pattern_tools.compute_overlap_list(pat, pattern_list)
            ax = plt.subplot( nRows, maxCols, maxCols+i+1 )
            ax.imshow( pat )
            ax.axis('off')
            ax1 = plt.subplot( nRows, maxCols, 2*maxCols+i+1)
            ax1.bar( range(len(overlap_list)), overlap_list )
            #  ax1.set_ylim( -1, 1 )
            ax1.set_xticks( range(len(overlap_list)) )
            ax1.set_xticklabels( letter_list )

        plt.tight_layout()
        outfile = 'figures/final_%s.png' % l
        plt.savefig( outfile )
        print( '|| Saved to %s' % outfile )
        plt.show()
        plt.close()

    return pattern_list, noisy_init_state, states_as_patterns

if __name__ == '__main__':
    main()
