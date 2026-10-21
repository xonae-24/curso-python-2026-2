import java.util.Scanner;

public class Ejercicio1 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("ingrese los kilometros: ");
        double km = entrada.nextDouble();
        
        double metros = km * 1000;
        double centimetros = km * 100000;

        System.out.println("metros: " + metros);
        System.out.println("centimetros: " + centimetros);
        entrada.close();
    }
}
