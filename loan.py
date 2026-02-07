
from sklearn.linear_model import LogisticRegression


X = [
    [40, 600],
    [60, 700],
    [80, 750],
    [30, 500],
    [55, 650]
]

y = [0, 1, 1, 0, 1]


model = LogisticRegression()
model.fit(X, y)


income = float(input("Enter monthly income (in thousands): "))
credit_score = int(input("Enter credit score: "))


prediction = model.predict([[income, credit_score]])

if prediction[0] == 1:
    print("\nLoan Status: APPROVED ")
else:
    print("\nLoan Status: REJECTED ")
