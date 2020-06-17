import java.util.Scanner;

public class Calculopix{

	public static void main(String[] args){

	Scanner entrada = new Scanner(System.in);
	float pix=0;
	
	int op=0;
	while(op==0){
		System.out.print("Ingresa los pixeles: ");
		pix = entrada.nextFloat();
		double total = (double)(pix*44.4)/100;
		System.out.println("Los pixeles a escala 480x320 son: "+total);
		System.out.println("-----------------------------------------------");
	}

	}
}
