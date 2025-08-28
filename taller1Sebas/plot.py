#!/usr/bin/env python3
import csv, os
from collections import defaultdict
import matplotlib.pyplot as plt

# Leer CSV
rows = []
with open("estadisticas.csv") as f:
    r = csv.DictReader(f)
    for row in r:
        row["N"] = int(row["N"])
        row["Hilos"] = int(row["Hilos"])
        row["media_us"] = float(row["media_us"])
        row["mediana_us"] = float(row["mediana_us"])
        row["std_us"] = float(row["std_us"])
        row["speedup"] = float(row["speedup"])
        row["eficiencia"] = float(row["eficiencia"])
        rows.append(row)

# Agrupar por N
byN = defaultdict(list)
for row in rows:
    byN[row["N"]].append(row)

os.makedirs("graficas", exist_ok=True)

for N, arr in sorted(byN.items()):
    arr = sorted(arr, key=lambda x: x["Hilos"])
    X = [r["Hilos"] for r in arr]
    Tm = [r["mediana_us"] for r in arr]
    Sp = [r["speedup"] for r in arr]
    Ef = [r["eficiencia"] for r in arr]

    # Tiempo vs Hilos
    plt.figure()
    plt.plot(X, Tm, marker="o")
    plt.title(f"Tiempo (mediana µs) vs Hilos — N={N}")
    plt.xlabel("Hilos")
    plt.ylabel("Tiempo (µs)")
    plt.grid(True)
    plt.savefig(f"graficas/tiempo_vs_hilos_N{N}.png", bbox_inches="tight")
    plt.close()

    # Speedup vs Hilos
    plt.figure()
    plt.plot(X, Sp, marker="o")
    plt.title(f"Speedup vs Hilos — N={N}")
    plt.xlabel("Hilos")
    plt.ylabel("Speedup")
    plt.grid(True)
    plt.savefig(f"graficas/speedup_vs_hilos_N{N}.png", bbox_inches="tight")
    plt.close()

    # Eficiencia vs Hilos
    plt.figure()
    plt.plot(X, Ef, marker="o")
    plt.title(f"Eficiencia vs Hilos — N={N}")
    plt.xlabel("Hilos")
    plt.ylabel("Eficiencia")
    plt.grid(True)
    plt.savefig(f"graficas/eficiencia_vs_hilos_N{N}.png", bbox_inches="tight")
    plt.close()

print("Listo -> carpeta graficas/")


