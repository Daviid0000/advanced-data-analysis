import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('MOCK_DATA.csv', delimiter=",")

data["media"] = data["performance_score"].mean()

performance_score = data["performance_score"]
suma = sum(performance_score)
mediana = sum(performance_score)/len(performance_score)
desvio_estandar = data["performance_score"].std()
departamentos = data["departament"]
empleados_por_departamento = data["departament"].value_counts()
correlacion = data["years_with_company"].corr(data["performance_score"])

# Histograma del performance_score para cada departamento
departamentos = data["departament"].unique()
for departamento in departamentos:
    subset = data[data["departament"] == departamento]
    plt.hist(subset["performance_score"], bins=10, alpha=0.5, label=departamento)

plt.xlabel('Performance Score')
plt.ylabel('Frequency')
plt.title('Histograma del Performance Score por Departamento')
plt.legend(loc='upper right')
plt.show()

# Gráfico de dispersión de years_with_company vs. performance_score
plt.scatter(data["years_with_company"], data["performance_score"], alpha=0.5)
plt.xlabel('Years with Company')
plt.ylabel('Performance Score')
plt.title('Years with Company vs. Performance Score')
plt.show()

# Gráfico de dispersión de salary vs. performance_score
plt.scatter(data["salary"], data["performance_score"], alpha=0.5)
plt.xlabel('Salary')
plt.ylabel('Performance Score')
plt.title('Salary vs. Performance Score')
plt.show()


print("mediana:", mediana)
print("desvio estandar:", desvio_estandar)
print("empleados:", empleados_por_departamento)
print("correlación1 :", correlacion)