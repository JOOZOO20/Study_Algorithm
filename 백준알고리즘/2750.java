import java.util.Scanner;


public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		// ����� ���� ���� �Է�
		int num = sc.nextInt();
		int[] list1 = new int[num];

		// ������ŭ ���ڸ� �Է¹���.
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

			//item�� ���Ե� ��ġ j�� ã��
			for(j=i;(j>0)&&(a[j-1]>item);j--) {
				a[j]=a[j-1];
			}
			a[j]=item;
		}
	}
}
