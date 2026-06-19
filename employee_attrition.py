import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = {
    'Age':[22,25,30,35,40,28,45,32],
    'Salary':[25000,30000,40000,60000,70000,35000,80000,50000],
    'Years':[1,2,3,5,8,2,10,4],
    'Attrition':[1,1,0,0,0,1,0,0]
}

df = pd.DataFrame(data)

print(df)

X = df[['Age','Salary','Years']]
y = df['Attrition']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

new_employee = pd.DataFrame({
    'Age':[27],
    'Salary':[32000],
    'Years':[2]
})

result = model.predict(new_employee)

if result[0] == 1:
    print("Employee May Leave")
else:
    print("Employee Will Stay")
    
    import matplotlib.pyplot as plt

attrition_count = df['Attrition'].value_counts()

plt.bar(
    ['Stayed', 'Left'],
    [attrition_count[0], attrition_count[1]]
)

plt.title("Employee Attrition Analysis")
plt.xlabel("Status")
plt.ylabel("Number of Employees")

plt.show()