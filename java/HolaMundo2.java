public class HolaMundo2 {
    public static void main(String[] args) {
        java.util.Scanner sc = new java.util.Scanner(System.in);
        System.out.print("Ingrese su edad: ");
        if (sc.hasNextInt()) {
            int edad = sc.nextInt();
            if (edad < 0) {
                System.out.println("Edad no válida.");
            } else if (edad < 13) {
                System.out.println("Eres un niño.");
            } else if (edad <= 17) {
                System.out.println("Eres un adolescente.");
            } else if (edad <= 64) {
                System.out.println("Eres un adulto.");
            } else {
                System.out.println("Eres un adulto mayor.");
            }
        } else {
            System.out.println("Entrada no válida.");
        }
        sc.close();
    }
}