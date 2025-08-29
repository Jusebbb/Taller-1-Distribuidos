# 📘 Taller 1 — Multiplicación de Matrices con OpenMP

## 📌 Introducción
Este proyecto desarrolla e implementa un algoritmo de **multiplicación de matrices clásica (MM)** en el lenguaje **C**,
paralelizado con **OpenMP** para aprovechar el poder de cómputo de múltiples núcleos.  
El trabajo incluye:
- Código en **C** bien documentado.
- **Makefile** para compilación automatizada.
- **Script de automatización en Perl** para pruebas masivas.
- **Script de análisis en Python** para procesar resultados.
- **Plan de pruebas** con 12 dimensiones y 5 configuraciones de hilos.
- **Resultados completos** en tabla y gráficas.
- **Conclusiones y mejoras futuras**.

---

## ⚙️ Funcionalidades principales del código
El archivo `mmClasicaOpenMP.c` implementa las siguientes funciones:

- **`iniMatrix`** → Inicializa matrices con valores aleatorios.  
- **`impMatrix`** → Imprime matrices pequeñas (N < 9).  
- **`multiMatrix`** → Multiplicación clásica de matrices con paralelismo OpenMP.  
- **`InicioMuestra` / `FinMuestra`** → Cronometraje en microsegundos.  
- **`main`** → Controla el flujo del programa (entrada de parámetros, ejecución y salida).  

---

# 🧱 Makefile documentado
El **Makefile** automatiza la compilación, estandariza el proceso y evita recompilaciones innecesarias.

### Variables principales
```make
CC       := gcc
CSTD     := -std=c99
CFLAGS   := -Wall -Wextra -O3 -fopenmp $(CSTD) -MMD -MP
LDFLAGS  := -lm

TARGET   := mmClasicaOpenMP
SRCS     := mmClasicaOpenMP.c
OBJS     := $(SRCS:.c=.o)
DEPS     := $(OBJS:.o=.d)
```

### Reglas principales
```make
all: $(TARGET)

$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $@ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS) $(DEPS) $(TARGET)
```

**Beneficios:** reproducibilidad, rapidez, claridad y estandarización.

## **🚀 Compilación **
Con `Makefile`:
```bash
make
```
## **🚀 ejecución **
Formato:
```bash
./clasicaOpenMP SIZE HILOS
```
Ejemplo:
```bash
./clasicaOpenMP 500 4
```
multiplica 2 matrices 500 *500 usando 4 hilos

## 🧪**Ejemplo de salida**

<img width="490" height="32" alt="Captura de pantalla 2025-08-28 a la(s) 9 45 08 p m" src="https://github.com/user-attachments/assets/d4676a17-2873-47d8-99d3-151ff47ddaa9" />

---

# 🧪 Plan de pruebas

## Diseño experimental
- **Tamaños (12 valores, N < 14 000):** {200, 400, 600, ..., 3600}.  
- **Hilos (5 configuraciones):** {1, 4, 8, 16, 20}.  
- **Repeticiones:** 30 por combinación `(N, T)`.  

## Métricas calculadas
- Media, desviación estándar.  
- Mediana, p90, IC95%.  
- Speedup: `tiempo(1)/tiempo(T)`.  
- Eficiencia: `speedup/T`.  
- GFLOPS ≈ `(2·N³)/(tiempo_segundos·1e9)`.  

## Script de automatización (auto.pl)
```perl
my @Size_Matriz = (200,400,600,...,3600);
my @Num_Hilos   = (1,4,8,16,20);
my $Reps        = 30;

foreach my $N (@Size_Matriz){
  foreach my $T (@Num_Hilos){
    my $file = "archivos_dat/mmClasicaOpenMP-$N-Hilos-$T.dat";
    for (my $i=0;$i<$Reps;$i++){
      system("./mmClasicaOpenMP $N $T >> $file");
    }
  }
}
```

---

# 📊 Resultados completos

A continuación se presenta la tabla de resultados obtenidos en `estadisticas.csv`:

|    N |   Hilos |   n |         media_us |       mediana_us |           std_us |   speedup |   eficiencia |
|-----:|--------:|----:|-----------------:|-----------------:|-----------------:|----------:|-------------:|
| 1000 |       1 |   7 | 492859           | 493927           |   3100.29        |   1       |     1        |
| 1000 |       4 |   7 | 131413           | 132085           |   1836.34        |   3.73946 |     0.934866 |
| 1000 |       8 |   7 | 101810           | 101047           |   2275.31        |   4.88809 |     0.611011 |
| 1000 |      16 |   7 |  91793.6         |  92415           |   2468.27        |   5.34466 |     0.334041 |
| 1000 |      20 |   7 |  92299.3         |  92304           |   1283.43        |   5.35109 |     0.267554 |
| 2000 |       1 |   7 |      5.01369e+06 |      5.01113e+06 |  13168.3         |   1       |     1        |
| 2000 |       4 |   7 |      2.40966e+06 |      2.3771e+06  |  49381.8         |   2.10809 |     0.527021 |
| 2000 |       8 |   7 |      1.4167e+06  |      1.40536e+06 |  31381.6         |   3.56573 |     0.445716 |
| 2000 |      16 |   7 |      1.35607e+06 |      1.35948e+06 |  43143.3         |   3.68606 |     0.230378 |
| 2000 |      20 |   7 |      2.41285e+06 |      2.45281e+06 | 357244           |   2.04302 |     0.102151 |
| 3040 |       1 |   7 |      3.03058e+07 |      3.03162e+07 | 746492           |   1       |     1        |
| 3040 |       4 |   7 |      1.55334e+07 |      1.55223e+07 | 296605           |   1.95308 |     0.48827  |
| 3040 |       8 |   7 |      1.40896e+07 |      1.39914e+07 | 185479           |   2.16677 |     0.270846 |
| 3040 |      16 |   7 |      1.46169e+07 |      1.45576e+07 | 286093           |   2.08251 |     0.130157 |
| 3040 |      20 |   7 |      1.44554e+07 |      1.44832e+07 | 370480           |   2.09321 |     0.10466  |
| 4040 |       1 |   7 |      2.84423e+08 |      1.25747e+08 |      3.71997e+08 |   1       |     1        |
| 4040 |       4 |   7 |      4.17222e+07 |      4.21762e+07 |      1.285e+06   |   2.98147 |     0.745367 |
| 4040 |       8 |   7 |      3.22217e+07 |      3.23024e+07 |      1.59009e+06 |   3.89281 |     0.486601 |
| 4040 |      16 |   7 |      3.24877e+07 |      3.27114e+07 | 798536           |   3.84414 |     0.240259 |
| 4040 |      20 |   7 |      3.54806e+07 |      3.60204e+07 |      1.03111e+06 |   3.49099 |     0.17455  |
| 5040 |       1 |   3 |      3.15868e+08 |      2.37442e+08 |      1.14006e+08 |   1       |     1        |

---

# 📉 Gráficas de rendimiento

### Speedup vs Número de Hilos
<img width="1400" height="1000" alt="speedup (2)" src="https://github.com/user-attachments/assets/7c6f1c21-2da7-4bf4-85f3-d6dcb478daf6" />


### Eficiencia vs Número de Hilos
<img width="1400" height="1000" alt="eficiencia (1)" src="https://github.com/user-attachments/assets/a4357897-7d0f-4733-85f8-a5fafef410c0" />


### Tiempo promedio vs Número de Hilos
<img width="1400" height="1000" alt="tiempo" src="https://github.com/user-attachments/assets/63606bfa-869f-443d-ab2f-bc743130a1c6" />


---

# 📂 Scripts de análisis

## `analisis.py`
- Lee los archivos `.dat` generados en `archivos_dat/`.
- Calcula estadísticos: media, std, mediana, IC95%, speedup, eficiencia, GFLOPS.
- Genera `estadisticas.csv` y gráficas de rendimiento.

## `plot.py`
- Usa `matplotlib` para graficar `speedup`, `eficiencia` y `tiempo`.
- Guarda las gráficas en la carpeta `graficas/`.

---

# ✅ Conclusiones
1. **Escalabilidad**: En matrices grandes se observa una mejora significativa al aumentar hilos.  
2. **Sobrecarga**: En matrices pequeñas el overhead de paralelismo puede empeorar resultados.  
3. **Eficiencia**: Disminuye a medida que se incrementan los hilos debido a límites de hardware.  
4. **Repeticiones**: Ejecutar cada configuración varias veces permite un análisis estadístico confiable.  
5. **Valor académico**: Este taller demuestra el impacto del paralelismo con OpenMP en algoritmos clásicos.  
6. **Trabajo futuro**: Explorar algoritmos avanzados (Strassen, BLAS) o ejecución en GPU (CUDA/OpenCL).  

---
