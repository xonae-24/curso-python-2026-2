import java.util.Scanner;

public class Ejercicio2 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("ingrese el primer numero: ");
        int a = entrada.nextInt();
        
        System.out.print("ingrese el segundo numero: ");
        int b = entrada.nextInt();

        int suma = a + b;

        System.out.println("la suma es: " + suma);
        entrada.close();
    }
}
