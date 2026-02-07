import matplotlib.pyplot as plt
import pandas as pd

x = [1, 2, 3, 4, 5 ]
y = [5, 5, 2, 60, 10]
plt.plot(x,y, color ='red', marker = 'o', linewidth = 3, markersize = 10, label = 'line plot')
plt.grid()
plt.show()

data = {
    "salary": [1000, 2000, 3000, 5000, 1500],
   
}
df = pd.DataFrame(data)
print(df)
df.head()
df.shape
plt.plot(df['salary'], marker='o')
plt.show()
plt.hist(df['salary'], bins=5)
plt.show()


# import seaborn as sns
# import matplotlib.pyplot as plt
data = [10,20,30,40,50]
sns.histplot(data)
plt.show()



import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data = np.random.normal(50, 60, 100)
sns.histplot(data)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

data = [10, 12, 14, 16, 18]
print(np.mean(data))
print(np.std(data))
print(np.var(data))
print(np.median(data))
print(np.percentile(data, 25))
print(np.percentile(data, 75))
print(np.min(data))
print(np.max(data))
print(np.ptp(data))  # Peak to Peak (max - min)
print(plt.hist(data, bins=3))
plt.show()
