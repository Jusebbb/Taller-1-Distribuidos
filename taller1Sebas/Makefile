# ===== Taller 1 - MM OpenMP 
CC      := gcc-15
CFLAGS  := -O3 -march=native -fopenmp -Wall -Wextra
TARGET  := mmClasicaOpenMP
SRC     := mmClasicaOpenMP.c
OUTDIR  := archivos_dat

.PHONY: all run clean distclean datos

all: $(TARGET)

$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $@ $<

run: $(TARGET) datos
	@perl auto.txt

datos:
	@mkdir -p $(OUTDIR)

clean:
	@rm -f $(TARGET)

distclean: clean
	@rm -f $(OUTDIR)/*.dat estadisticas.csv


