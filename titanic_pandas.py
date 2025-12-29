import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("train.csv", sep="\t")
print("\nDataset Info")
print(df.describe())
print("\nMissing Values")
print(df.isnull().sum())

# 1. Survival Rate by Passenger Class
print("\n1. Survival Rate by Passenger Class")
class_survival = df.groupby("Pclass")["Survived"].mean()
print(class_survival)

# 2. Gender Bias in Survival
print("\n2. Gender Bias in Survival")
gender_survival = df.groupby("Sex")["Survived"].agg(["mean", "count"])
overall = df["Survived"].mean()
gender_survival["Above_Average"] = gender_survival["mean"] > overall
print(gender_survival)
print("Overall Survival Rate:", overall)

# 3. Missing Cabin Analysis (COUNT + MEAN)
print("\n3. Missing Cabin Survival")
df["HasCabin"] = df["Cabin"].notna()

cabin_count = df.groupby("HasCabin")["Survived"].count()
cabin_survived = df.groupby("HasCabin")["Survived"].sum()
cabin_rate = df.groupby("HasCabin")["Survived"].mean()
print("Passenger Count:\n", cabin_count)
print("Survivors:\n", cabin_survived)
print("Survival Rate:\n", cabin_rate)

# 4. Family Size Feature using apply()
df["FamilySize"] = df.apply(lambda x: x["SibSp"] + x["Parch"] + 1, axis=1)

print("\n4. Family Size Correlation with Survival")
print(df["FamilySize"].corr(df["Survived"]))
df["FamilySize"].hist(bins=10)
plt.title("Family Size Distribution")
plt.show()

# 5. Age Distribution using seaborn + bins
df["Age"].fillna(df["Age"].median(), inplace=True)

plt.figure(figsize=(8,5))
sns.histplot(df[df["Survived"]==1]["Age"], bins=20, label="Survived", kde=True)
sns.histplot(df[df["Survived"]==0]["Age"], bins=20, label="Not Survived", kde=True)
plt.legend()
plt.title("Age Distribution of Survivors vs Non-Survivors")
plt.show()

# 6. Embarkation Port Analysis
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

print("\n6. Survival Rate by Embarkation Port")
embark_survival = df.groupby("Embarked")["Survived"].mean()
print(embark_survival)

# 7. Ticket Class vs Survival (Pivot Table)
df["TicketClass"] = df["Ticket"].str[0]

ticket_pivot = pd.pivot_table(df, values="Survived", index="TicketClass", aggfunc="mean")
print("\n7. Ticket Class Survival Rates")
print(ticket_pivot)

# 8. Missing Fare Handling (Median by Class)
print("\n8. Missing Fare Count:", df["Fare"].isnull().sum())

df["Fare"] = df.groupby("Pclass")["Fare"].transform(lambda x: x.fillna(x.median()))
print("Median Fare by Class")
print(df.groupby("Pclass")["Fare"].median())

# 9. Correlation Matrix + Heatmap
corr = df[["Age","Fare","Survived"]].corr()
print("\n9. Correlation Matrix")
print(corr)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 10. Advanced Family Size Survival Groups
df["FamilyCount"] = df["SibSp"] + df["Parch"]
def family_group(x):
    if x == 0:
        return "Solo"
    elif x == 1:
        return "Family of 1"
    else:
        return "Family 2+"
df["FamilyGroup"] = df["FamilyCount"].apply(family_group)

print("\n10. Survival Rate by Family Group")
print(df.groupby("FamilyGroup")["Survived"].mean())