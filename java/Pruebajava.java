import java.util.Scanner;

public class Pruebajava {
    public static void main (String[] args){

        try (Scanner scanner = new Scanner (System.in)) {
            int var_1;
            System.out.println("Elige nota 1");
            var_1 = scanner.nextInt();
            System.out.println("Elige nota 2");
            int var_2;
            var_2 = scanner.nextInt();
            System.out.println("El resultado es:" + (var_1 + var_2)/2);
        }
    }
}