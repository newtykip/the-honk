import java.util.Scanner;

public class Babylonian
{
    public static void main(String [] args)
    {
        Scanner input = new Scanner(System.in);
        long x = input.nextLong();
        double a = 2;

        while (Math.abs(a - (x / a)) > 1)
        {
            a = (a + (x / a)) / 2;
        }

        System.out.println(a);
    }
}
