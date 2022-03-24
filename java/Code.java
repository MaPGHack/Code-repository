import static java.lang.System.in;

import java.util.Scanner;

public class Code 
{
    private static final String FUN_2 = FUN_2(20);
    private static final String FUN2 = FUN_2;
    private static int var_1;
    public static void main (String[] arg) 
    {
        Scanner input = new Scanner(in);
        var_1 = Scanner.nextInt();
        if(var_1 < 20){
            System.out.println("op 1 es menor que 20");
        }else{
            System.out.println("op 1 es mayor que 20");
        }
        System.out.println("Hello World");
        String x = FUN2;
        System.out.println(x);
        //Fun_2
    }
    
    static String FUN_2 (int var_2) {
        if(var_2 == 5){
            System.out.println("var_2 es igual a 5");
        }else if(var_2 == 6){
            System.out.println("var_2 es igual a 6");
        }else{
            System.out.println("var_2 no es igual ni a 5 ni a 6");
        }
        return null;
    }
}