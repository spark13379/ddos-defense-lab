import json
import matplotlib.pyplot as plt

with open("analytics/results.json") as f:
    data = json.load(f)

labels = ["Sucesso", "Bloqueado"]
values = [data["success"], data["fail"]]

plt.figure()
plt.bar(labels, values)

plt.title("Requisições vs Bloqueios")
plt.xlabel("Tipo")
plt.ylabel("Quantidade")

# salva imagem
plt.savefig("analytics/grafico.png")

print("Gráfico salvo em: analytics/grafico.png")