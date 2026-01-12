#include<stdio.h>
#include<stdlib.h>

typedef struct {
    int *data;
    int capacity;
} Array;


void initArray(Array *arr, int capacity) {
    arr->data = (int *)malloc(sizeof(int) * capacity);
    arr->capacity = capacity;

    for (int i = 0; i<capacity; i++){
        *(arr->data +i) = 0;
    }
}


void put(Array *arr, int index, int value) {
    if (index < 0 || index >= arr->capacity) {
        printf("Index out of bounds\n");
        return;
    }
    *(arr->data + index) = value;
}


int get(Array *arr, int index) {
    if (index < 0 || index >= arr->capacity) {
        printf("Index out of bounds\n");
        return -1;
    }
    return *(arr->data + index);
}


void freeArray(Array *arr) {
    free(arr->data);
}


int main(){
    Array arr;
    initArray(&arr, 5);

    put(&arr, 0, 10);
    put(&arr, 1, 100);
    put(&arr, 2, 1000);

    for (int i = 0; i < arr.capacity; i++){
        printf("Index %d: %d\n", i, *(arr.data + i));
    }

    printf("Value at key 0: %d\n", get(&arr, 0));

    printf("Value at key 10: %d\n", get(&arr, 10));


    freeArray(&arr);
}