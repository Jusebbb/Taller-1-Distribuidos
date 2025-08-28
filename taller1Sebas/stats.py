#!/usr/bin/env python3
import re, glob, statistics, csv

rows = []
by_size = {}  # para guardar tiempos base (T=1)

for path in sorted(glob.glob("archivos_dat/mmClasicaOpenMP-*-Hilos-*.dat")):
    m = re.search(r"mmClasicaOpenMP-(\d+)-Hilos-(\d+)\.dat", path)
    N = int(m.group(1)); T = int(m.group(2))
    with open(path) as f:
        us = [float(x.strip()) for x in f if x.strip()]
    if not us: continue
    mean = statistics.fmean(us)
    med  = statistics.median(us)
    stdd = statistics.pstdev(us) if len(us)>1 else 0.0
    rows.append([N,T,len(us),mean,med,stdd])
    by_size.setdefault(N, {})[T] = med

# calcular speedup y eficiencia usando la mediana con T=1
final = []
for N,T,n,mean,med,stdd in rows:
    base = by_size[N].get(1, med)
    speedup = base/med if med>0 else 0
    eff = speedup/T
    final.append([N,T,n,mean,med,stdd,speedup,eff])

final.sort(key=lambda r:(r[0], r[1]))

with open("estadisticas.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["N","Hilos","n","media_us","mediana_us","std_us","speedup","eficiencia"])
    w.writerows(final)

print("✅ OK -> estadisticas.csv")



