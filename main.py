# Importaciones
import pandas as pd
import matplotlib.pyplot as plt

# Obtención de archivo csv
data = pd.read_csv('MOCK_DATA.csv', delimiter=",")
salary = data["salary"]
sumSalary = sum(salary)
lenSalary = len(salary)

performance_score = data["performance_score"]
sumPerformanceScore = sum(performance_score)
lenPerformanceScore = len(performance_score)

media = sumPerformanceScore/lenPerformanceScore
media2 = sumSalary/lenSalary 


desvio_estandar = data["performance_score"].std()
departamentos = data["departament"]
empleados_por_departamento = data["departament"].value_counts()
correlacion = data["years_with_company"].corr(data["performance_score"])

desvio_estandar2 = data["salary"].std()
correlacion2 = data["salary"].corr(data["performance_score"])

sumSalary = data["salary"].sum()
lenSalary = len(salary)
ordenSalary = sorted(salary)

# print("Salarios:", salary)
# print("Salarios ordenados:", ordenSalary)
# print("Longitud de lista de salarios:", lenSalary)
# print("Suma de salarios:", sumSalary)

print("La media de Performance Score es:", media)
if lenPerformanceScore % 2 == 0:
    performanceScoreMitad = performance_score[lenPerformanceScore//2]
    performanceScoreMitad2 = performance_score[lenPerformanceScore//2 - 1]
    mediana2 = (performanceScoreMitad + performanceScoreMitad2)/2
else:
    mediana2 = performance_score[lenPerformanceScore//2]
print("La mediana de puntuación de rendimiento es:", mediana2)
# print("La mediana de Performance Score es:", mediana)
print("El desvio estandar de Performance Score es:", desvio_estandar)
print("La cantidad de empleados de cada departamento es:", empleados_por_departamento)
print("La correlación entre Years With Company y Performance Score es:", correlacion)

print("La media de Salary es:", media2)
if lenSalary % 2 == 0:
    salaryMitad = salary[lenSalary//2]
    salaryMitad2 = salary[lenSalary//2 - 1]
    mediana2 = (salaryMitad + salaryMitad2)/2
else:
    mediana2 = salary[lenSalary//2]
print("la mediana de los salarios es:", mediana2)
print("El desvio estandar de Salary es:", desvio_estandar2)
print("La correlación entre Salary y Performance Score es:", correlacion2)

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

