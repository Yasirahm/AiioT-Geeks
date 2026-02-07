
from sklearn.linear_model import LinearRegression

X = [
    [800, 2, 10],
    [1000, 3, 8],
    [1200, 3, 6],
    [1500, 4, 4],
    [1800, 4, 2]
]


y = [20, 30, 40, 55, 70]

model = LinearRegression()
model.fit(X, y)


size = float(input("Enter house size (sqft): "))
rooms = int(input("Enter number of rooms: "))
age = int(input("Enter age of house (years): "))

predicted_price = model.predict([[size, rooms, age]])

print("\nPredicted House Price:", round(predicted_price[0], 2))
