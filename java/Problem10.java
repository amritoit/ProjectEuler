import java.math.BigInteger;
import java.util.Scanner;

public class Problem10 {

		public static void main(String args[]) {
	
			Scanner sc = new Scanner(System.in);
			int T = sc.nextInt();
			int N, K;
			String input;
			int[] val = new int[1000001];
			sieve(val);
			while (T-- > 0) {
				N = sc.nextInt();
				System.out.println(val[N]);
			}
	
		}
	
		private static void sieve(int[] val) {
	
			val[2] = 2;
			val[1] = 0;
			val[0] = 0;
	
			for (int i = 2; i <= val.length / 2; i++) {
				if (val[i] == -1) {
					val[i] = val[i - 1];
					continue;
				}
				val[i] = i + val[i - 1];

				int count=2;
				for (int c = count * i; c < 1000001; c = i * ++count) {
					if(c>=0)
						val[c] = -1;
					else break;
				}
	
			}
		}
}
