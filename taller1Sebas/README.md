# 📘 Taller 1 — Multiplicación de Matrices 

## 📌 Introducción
Este proyecto implementa la **multiplicación clásica de matrices en C**, paralelizada con **OpenMP** 
para aprovechar múltiples núcleos. Se acompaña de un **Makefile**, un **script de automatización en Perl**, 
y un **análisis estadístico en Python**, integrando todo en un solo flujo de pruebas.

El objetivo es analizar el rendimiento, la escalabilidad y la eficiencia del algoritmo bajo diferentes configuraciones de hilos y tamaños de matrices.

---

## ⚙️ Funcionalidades principales
- `iniMatrix` → Inicializa matrices con números aleatorios.
- `impMatrix` → Imprime matrices pequeñas (N < 9).
- `multiMatrix` → Multiplicación clásica con OpenMP.
- `InicioMuestra / FinMuestra` → Cronometraje en microsegundos.
- `main` → Control principal: recibe parámetros, ejecuta la multiplicación, mide tiempos.

---

# 🧱 Makefile documentado

El **Makefile** automatiza la compilación y estandariza el proceso para todo el equipo.

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

---

# 🧪 Plan de pruebas

## Diseño
- **Tamaños (12 valores, N < 14 000):** {200, 400, 600, ..., 3600}.  
- **Hilos (5 configuraciones):** {1, 4, 8, 16, 20}.  
- **Repeticiones:** 30 por combinación `(N, T)`.  

## Métricas
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

## 📊 Resultados completos

A continuación se incluye la tabla de resultados de `estadisticas.csv`:

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

## 📉 Gráficas de rendimiento

### Speedup vs Número de Hilos
![Speedup](graficas/speedup.png)

### Eficiencia vs Número de Hilos
![Eficiencia](graficas/eficiencia.png)

### Tiempo promedio vs Número de Hilos
![Tiempo](graficas/tiempo.png)

---

## ✅ Conclusiones
1. Para matrices grandes, el paralelismo mejora significativamente el tiempo de ejecución.  
2. En matrices pequeñas, el overhead de hilos puede empeorar el rendimiento.  
3. La eficiencia decrece a medida que se aumenta el número de hilos, debido a límites de hardware y sincronización.  
4. Repeticiones múltiples y análisis estadístico reducen ruido y validan los resultados.  
5. OpenMP es una herramienta práctica para paralelizar, pero se ve limitada frente a alternativas como librerías BLAS o GPU (CUDA/OpenCL).  

