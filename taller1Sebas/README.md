# Taller 1 — Multiplicación de Matrices con OpenMP

**Autor:** Juan Sebastián Vargas Cortes  
**Fecha:** 2025-08-28

## Requisitos
- macOS
- Homebrew + `gcc-15` (o similar con `-fopenmp`)
- Python 3 (para estadísticas y gráficas)

## Compilar y ejecutar
```bash
make            # compila mmClasicaOpenMP
make run        # corre lotes y genera .dat en ./archivos_dat
python3 stats.py
python3 plot.py

