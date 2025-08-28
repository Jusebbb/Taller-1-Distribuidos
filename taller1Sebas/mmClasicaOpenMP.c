#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/time.h>
#include <omp.h>

struct timeval inicio, fin;

static inline void InicioMuestra(){ gettimeofday(&inicio, (void *)0); }
static inline void FinMuestra(){
    gettimeofday(&fin, (void *)0);
    fin.tv_usec -= inicio.tv_usec;
    fin.tv_sec  -= inicio.tv_sec;
    double tiempo = (double)(fin.tv_sec*1000000 + fin.tv_usec);
    printf("%9.0f\n", tiempo); // microsegundos
}

static inline void impMatrix(size_t *m, int D){
    if (D < 9){
        for(int i=0;i<D;i++){
            for(int j=0;j<D;j++) printf("%zu ", m[i*D+j]);
            printf("\n");
        }
        printf("**-----------------------------**\n");
    }
}

static inline void iniMatrix(size_t *m1, size_t *m2, int D){
    for (int i=0;i<D*D;i++){ m1[i] = (size_t)(i*2); m2[i] = (size_t)(i+2); }
}

static inline void multiMatrix(size_t *mA, size_t *mB, size_t *mC, int D){
    #pragma omp parallel
    {
        size_t Suma, *pA, *pB;                  // privadas por bloque
        #pragma omp for schedule(static)        // distribuir por filas
        for (int i=0;i<D;i++){
            for (int j=0;j<D;j++){
                pA = mA + i*D;
                pB = mB + j;
                Suma = 0;
                for (int k=0;k<D;k++, pA++, pB+=D){
                    Suma += (*pA) * (*pB);
                }
                mC[i*D + j] = Suma;
            }
        }
    }
}

int main(int argc, char *argv[]){
    if (argc < 3){
        fprintf(stderr, "Uso: %s N HILOS\n", argv[0]);
        return 1;
    }
    int N  = atoi(argv[1]);
    int TH = atoi(argv[2]);
    if (N<=0 || TH<=0){ fprintf(stderr, "Parámetros inválidos\n"); return 2; }

    omp_set_num_threads(TH);

    size_t *A = (size_t*)calloc((size_t)N*N, sizeof(size_t));
    size_t *B = (size_t*)calloc((size_t)N*N, sizeof(size_t));
    size_t *C = (size_t*)calloc((size_t)N*N, sizeof(size_t));
    if(!A || !B || !C){ fprintf(stderr, "Memoria insuficiente para N=%d\n", N); return 3; }

    iniMatrix(A,B,N);
    impMatrix(A,N); impMatrix(B,N);

    InicioMuestra();
    multiMatrix(A,B,C,N);
    FinMuestra();

    impMatrix(C,N);

    free(A); free(B); free(C);
    return 0;
}


