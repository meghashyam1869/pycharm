import pandas as pd
#import numpy as np
import numpy as np
#simple array
data= np.array(['g', 'e', 'e', 'k', 's',])
#providing an index
ser = pd.Series(data, index=[10, 11, 12, 13, 14])
print(ser)
