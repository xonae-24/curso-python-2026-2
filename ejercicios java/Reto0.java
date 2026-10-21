import java.util.Scanner;

class Calculadora {
    public void suma(float a, float b) {
        System.out.printf("%.1f ", a + b);
    }

    public void producto(float a, float b) {
        System.out.printf("%.1f%n", a * b);
    }
}

public class Reto0 {
    static Scanner entrada = new Scanner(System.in);

    public void run() {
        Calculadora calculadora = new Calculadora();
        int opcion = 0;

        while (opcion != 2) {
            System.out.println("1. calcular suma y multiplicacion");
            System.out.println("2. salir");
            System.out.print("seleccione una opcion: ");

            opcion = entrada.nextInt();

            if (opcion == 1) {
                System.out.print("ingrese el primer numero: ");
                float a = entrada.nextFloat();
                System.out.print("ingrese el segundo numero: ");
                float b = entrada.nextFloat();

                calculadora.suma(a, b);
                calculadora.producto(a, b);

            } else if (opcion == 2) {
                System.out.println("programa finalizado");

            } else {
                System.out.println("opcion incorrecta");
            }
        }
    }

    public static void main(String[] args) {
        new Reto0().run();
    }
}