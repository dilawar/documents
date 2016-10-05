import pandas 
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
try:
    mpl.style.use( 'seaborn-talk' )
except Exception as e:
    pass
mpl.rcParams['axes.linewidth'] = 0.1
plt.rc('text', usetex=True)
plt.rc('font', family='serif')



def main( ):
    filename = './Buggy Usage in October 2016.xlsx'
    data = pandas.read_excel( filename, sheetname = None )
    newData = []
    for sheet in data:
        sheetData = data[sheet]
        count = sheetData['Count']
        # Add two entries together since buggy has to come back
        yvec = []
        for i in range( len(count) / 2 ):
            yvec.append( count[2*i] + count[2*i+1] )
        newData.append( yvec )
    
    newData = np.vstack( newData )

    dayData = []
    for i in range( 7 ):
        dayidata = newData[i::7]
        dayData.append( np.sum( dayidata, axis = 1 ) )

    boxes = []
    for i, vec  in enumerate(newData.T):
        boxes.append( vec ) 

    plt.subplot( 2, 1, 1 )
    plt.boxplot( dayData )
    plt.title( 'Weekly usage' )
    plt.xticks( range(1,8), ('Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'))

    plt.subplot( 2, 1, 2 )
    plt.boxplot( boxes )
    plt.xlabel( 'Time, Buggy leaving NCBS (to/fro together)' )
    plt.ylabel( 'No of people (in to/fro trips combined)' )
    plt.xticks( range(1,14), data['oct1']['Time'] )
    plt.title( 'Trip-wise usage' )

    plt.suptitle( 'Total days = %d' % len(data) )
    plt.savefig( 'buggy_in_october.png' )
    print( 'Wrote figure to ./buggy_in_october.png' )

if __name__ == '__main__':
    main()
