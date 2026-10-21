import java.util.Scanner;

public class Ejercicio3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int opcion = 0;

        while (opcion != 2) {
            System.out.println("\n1. calcular distancia");
            System.out.println("2. salir");
            System.out.print("seleccione una opcion: ");
            opcion = entrada.nextInt();

            if (opcion == 1) {
                System.out.print("ingrese x1: ");
                double x1 = entrada.nextDouble();

                System.out.print("ingrese y1: ");
                double y1 = entrada.nextDouble();

                System.out.print("ingrese x2: ");
                double x2 = entrada.nextDouble();

                System.out.print("ingrese y2: ");
                double y2 = entrada.nextDouble();

                double distancia = Math.sqrt(
                    Math.pow(x2 - x1, 2) +
                    Math.pow(y2 - y1, 2)
                );

                System.out.println("la distancia es: " + distancia);

            } else if (opcion == 2) {
                System.out.println("programa finalizado");

            } else {
                System.out.println("opcion incorrecta");
            }
        }

        entrada.close();
    }
}
