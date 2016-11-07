import pandas 
import datetime
import numpy as np

import matplotlib as mpl

import matplotlib.pyplot as plt
try:
    mpl.style.use( 'ggplot' )
except Exception as e:
    pass
mpl.rcParams['axes.linewidth'] = 0.1
plt.rc('text', usetex=True)
plt.rc('font', family='serif')

from collections import defaultdict 
daysData = defaultdict( list )

def weekday( sheetname ):
    day = sheetname[3:]
    day = datetime.datetime.strptime( '2016-10-%s'%day, '%Y-%m-%d' )
    dayName = day.strftime( "%a" )
    return dayName


def main( ):
    filename = './Buggy Usage in October 2016.xlsx'
    data = pandas.read_excel( filename, sheetname = None )
    newData = []
    days = []
    for sheet in sorted(data, key=lambda x: int(x[3:])):
        sheetData = data[sheet]
        count = sheetData['Count']
        # If there was a buggy breakdown at any day. Do not count the day.
        if '-' in count.values:
            print( '[INFO] Breakdown on %s .. Not counting this day' %
                    sheet )
            continue
        # Add two entries together since buggy has to come back
        yvec = []
        for i in range( int(len(count) / 2) ):
            yvec.append( count[2*i] + count[2*i+1] )

        daysData[ weekday( sheet ) ].append( np.sum(yvec) )
        newData.append( yvec )
    
    newData = np.vstack( newData )

    boxes = []
    for day in [ 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri' 
            ]:
        print( 'Processing for day %s' % day )
        boxes.append( daysData[ day ] ) 

    plt.subplot( 2, 1, 1 )
    plt.boxplot( boxes )
    plt.title( 'Weekly usage' )
    plt.xticks( range(1,8), ('Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'))

    plt.subplot( 2, 1, 2 )
    plt.boxplot( newData )
    plt.xlabel( 'Time, Buggy leaving NCBS (to/fro together)' )
    plt.ylabel( 'No of people (in to/fro trips combined)' )
    plt.xticks( range(1,14), data['oct1']['Time'][::2] )
    plt.title( 'Trip-wise usage' )

    plt.suptitle( 'Total days = %d' % len(data) )
    plt.savefig( 'buggy_in_october.png' )
    print( 'Wrote figure to ./buggy_in_october.png' )

if __name__ == '__main__':
    main()
