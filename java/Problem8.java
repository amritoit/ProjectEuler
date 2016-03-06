import java.util.Scanner;
import java.math.BigInteger;

public class Problem8 {
	public static void main(String args[]) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		int N, K;
		String input;
		BigInteger[] val = new BigInteger[1001];

		while (T-- > 0) {
			N = sc.nextInt();
			K = sc.nextInt();
			input = sc.next();

			for (int k = 0; k < N; k++) {
				val[k] = new BigInteger(String.valueOf(input.charAt(k)));
			}

			System.out.println(getMaxProductInSeries(N, K, val));
		}

	}

	private static BigInteger getMaxProductInSeries(int N, int K,
			BigInteger[] val) {

		BigInteger maxPro = BigInteger.ONE;
		int noOfZero = 0;

		for (int i = 0; i < K; i++) {
			if (val[i].compareTo(BigInteger.ZERO) != 0)
				maxPro = maxPro.multiply(val[i]);
			else
				noOfZero += 1;
		}
		boolean find=false;
		BigInteger tempMax = maxPro;
		for (int i = 0, j = K; j < N; i++, j++) {

			if (val[i].compareTo(BigInteger.ZERO) == 0) {
				noOfZero -= 1;
			} else {
				tempMax = tempMax.divide(val[i]);
			}

			if (val[j].compareTo(BigInteger.ZERO) == 0) {
				noOfZero += 1;
			} else {
				tempMax = tempMax.multiply(val[j]);
			}

			if (noOfZero == 0 && tempMax.compareTo(maxPro) == 1) {
				maxPro = tempMax;
				find=true;
			}
		}
		
		if (noOfZero > 0 && !find)
			return BigInteger.ZERO;
		
		return maxPro;
	}
}
