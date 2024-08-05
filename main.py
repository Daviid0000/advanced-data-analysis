import pandas as pd

data = pd.read_csv('MOCK_DATA.csv', delimiter=",")

data["media"] = data["performance_score"].mean()
performance_score = data["performance_score"]
suma = sum(performance_score)
mediana = sum(performance_score)/len(performance_score)


print(data.head(20))
print("mediana:", mediana)
