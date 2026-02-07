import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("titanic.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

df["Age"].fillna(df["Age"].mean(), inplace=True)

df.drop_duplicates(inplace=True)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.show()

sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.show()


sns.countplot(x="Pclass", hue="Survived", data=df)
plt.title("Survival by Passenger Class")
plt.show()

sns.histplot(df["Age"], bins=30)
plt.title("Age Distribution")
plt.show()

sns.histplot(df["Fare"], bins=30)
plt.title("Fare Distribution")
plt.show()

print("\nINSIGHTS FROM TITANIC DATASET:")
print("1. More passengers did not survive than survived.")
print("2. Female passengers had higher survival rate.")
print("3. Passengers from higher class survived more.")
print("4. Younger passengers had better survival chances.")
print("5. Passengers who paid higher fare had higher survival rate.")
