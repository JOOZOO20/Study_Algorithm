import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// 출력할 문장 갯수 입력
		int num = sc.nextInt();
		int[] list1 = new int[num];

		// 갯수만큼 숫자를 입력받음.
		for(int i=0;i<num;i++) {
			list1[i]=sc.nextInt();
		}

		MySort.insertionSort(list1);
		for(int i=0;i<num;i++) {
			System.out.println(list1[i]);
		}
		sc.close();

	}
}

class MySort {
	public static void insertionSort(int[] a) {
		int i,j,item;

		for(i=1;i<a.length;i++) {
			item=a[i];

			//item이 삽입될 위치 j를 찾음
			for(j=i;(j>0)&&(a[j-1]>item);j--) {
				a[j]=a[j-1];
			}
			a[j]=item;
		}
	}
}
