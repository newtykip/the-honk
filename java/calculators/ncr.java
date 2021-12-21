package calculators;
import java.util.Scanner;

class CombinationCalculator {
	private static int factorial(int n) {
		int res = 1;

		for (int i = 2; i <= n; i++) {
			res *= i;
		}

		return res;
	}

	private static int nCr(int n, int r) {
		return factorial(n) / (factorial(r) * factorial(n - r));
	}

	public static void main(String[] args) {
		// Open a scanner and take the relevant inputs
		Scanner scan = new Scanner(System.in);

		System.out.print("Please input the value for n: ");
		int n = scan.nextInt();

		System.out.print("Please input the value for r: ");
		int r = scan.nextInt();

		// Close the scanner, and calculate the result
		scan.close();

		int result = nCr(n, r);
		System.out.println(result);
	}
}
