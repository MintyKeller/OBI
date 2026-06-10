#include <iostream>
using namespace std;

int buscaBinaria(int arr[], int n, int x) {
    int esquerda = 0;
    int direita = n - 1;
    
    while (esquerda <= direita) {
        int meio = (esquerda + direita) / 2;
        
        if (arr[meio] == x) {
            return meio;
        } else if (arr[meio] < x) {
            esquerda = meio + 1;
        } else {
            direita = meio - 1;
        }
    }
    
    return -1;
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    int x;
    cin >> x;
    
    cout << buscaBinaria(arr, n, x) << endl;
    return 0;
}
