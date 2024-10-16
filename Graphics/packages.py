# import pandas as pd
# a=[1,5,7]
# myvar=pd.Series(a)
# print(myvar)

# import pandas as pd 
# a=[1,5,8]
# myvar=pd.Series(a,index=["x","y","z"])
# print(myvar)

# import pandas as pd 
# mydataset={
#     'cars':["BMW","volvo","ford"],
#     'passings':[5,4,8]
# }
# print(mydataset)
# myvar=pd.DataFrame(mydataset)
# print(myvar)

# #numpy


# import numpy
# arr=numpy.array([1,2,3,4,5,6,7,8,9,10])
# print(arr[1])
# print(arr[2]+arr[3])
# print(arr[1:4])
# print(arr[5:])
# print(arr[:5])
# print(arr[-3:-1])


# import numpy as np
# arr=np.array([1,2,3,4,5])
# print(arr)
# a=[]
# print(type(a))
# print(type(arr))

# import numpy as np
# arr=np.array([[1,2,3],[4,5,6]])
# print(arr)
# print('2nd element on 1st row:',arr[0,1])

"""import numpy as np
arr=np.array([[1,2,3,8],[4,5,6,7]])
print(arr[0,2])
print("1.",arr[1,1:4])
print("2.",arr[0:2,2])
print("3.",arr[0:2,1:4])




import numpy as np
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("4.",arr)
print("5.",arr[0,1,2])

print(arr[1,1,1,])
print(arr[1,0,0:2])
print(arr[0:5,0:2,1:3])"""



"""import matplotlib.pyplot as plt
import numpy as np

xpoints=np.array([0,2,8])
ypoints=np.array([0,58,44])
plt.plot(xpoints,ypoints)
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np
x=np.array([4,5,6,1])
y=np.array([85,76,59,44])
plt.title("title")
plt.ylabel("time")
plt.xlabel("speed")
plt.plot(x,y)
plt.show()
"""

"""import matplotlib.pyplot as plt
import numpy as np
x=np.array([2,3,4,5,9])
plt.plot(x)
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

y=np.array([4,6,8,4,33])
plt.plot(y,marker="o")
plt.plot(y,marker="*")
plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np

y=np.array([4,6,8,4,33])
plt.plot(y,marker='o',ms='10',mec='r',mfc='k')
plt.plot(y,color='r',linewidth="4")
plt.show()"""
"""
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(x1,x2,y1,y2)
plt.show()"""

"""import matplotlib.pyplot as plt
import numpy as np

x=np.array([4,5,6])
y=np.array([3,6,9])
font1={'family':'serif','color':'red','size':15}
font2={'family':'serif','color':'blue','size':10}
plt.title('data',fontdict=font1)
plt.xlabel("time",fontdict=font2)
plt.ylabel("speed",fontdict=font2)
plt.plot(x,y)
plt.show()
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
np.random.seed(42)
x = np.random.rand(50) * 10
y = 2 * x + 1 + np.random.randn(50) * 2
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
plt.scatter(x, y, label='Data')
plt.plot(x, y_pred, color='red', label=f'Regression Line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()