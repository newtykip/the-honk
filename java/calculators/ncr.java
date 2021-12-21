package calculators;
import java.util.InputMismatchException;
import java.util.Scanner;

class CombinationCalculator {
	private static Scanner scanner = new Scanner(System.in);

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

	private static int intInput(String message) {
		int value = -1;

		while (value < 0) {
			try {
				System.out.print(message);
				value = scanner.nextInt();
			} catch (InputMismatchException e) {
				scanner.next();
			}
		}

		return value;
	}

	public static void main(String[] args) {
		// Take inputs
		int n = intInput("Please input the value for n: ");
		int r = intInput("Please input the value for r: ");
		scanner.close();

		// Calculate the result
		int result = nCr(n, r);
		System.out.println(result);
	}
}
