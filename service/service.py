import pandas as pd
import matplotlib.pyplot as plt
from errors.traceback_exceptions import traceException
def plotGraphUsingDF(df,x_axis,y_axis,kind):
    try:
        df.plot(kind = kind,
            x = x_axis,
            y = y_axis,
            color = 'green')
    
        # set the title
        plt.title('BarPlot')
        
        # show the plot
        plt.show()
    except Exception as e:
        traceException(e)