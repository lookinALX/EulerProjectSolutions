public class Euler_3 {

    public static void main(String[] args){
        int current_factor = 2;
        int last_factor = 1;
        long number = 600851475143L;
        while(number > 1){
            if(number % current_factor == 0){
                last_factor = current_factor;
                number /= current_factor;
                while(number % current_factor == 0){
                    number /= current_factor;
                }
            }
            current_factor += 1;
        }
        System.out.println(current_factor);
    }
}
