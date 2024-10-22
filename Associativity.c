#include <stdio.h>
#include <stdlib.h>
#include <time.h>       

#define N 1000
#define RAND_MAX 2147483647

int associativity(){
    float x =  rand();
    float y = rand();
    float z = rand();
    return (x+y)+z == x+(y+z);
}

int main(int argc, int** argv){
    srand(time(NULL));
    int i = 0;
    int good_answers = 0;
    while(i<N){
        if(associativity())
            good_answers++;
        i++;
    }
    printf("Fraction de bonnes réponses : %d sur %d\n", good_answers, N);
    return 0;
}