import java.util.Scanner;

public class BuscaBinaria {
    static int buscaBinaria(int[] arr, int x) {
        int esquerda = 0;
        int direita = arr.length - 1;
        
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
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int x = sc.nextInt();
        
        System.out.println(buscaBinaria(arr, x));
    }
}
