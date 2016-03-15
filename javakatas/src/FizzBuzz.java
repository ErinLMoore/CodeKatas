/**
 * Created by erinmoore on 3/15/16.
 */
public class FizzBuzz {
    public String fizzbuzzer (int input){
        String return_value = "";
        if (input%3 == 0){
            return_value += "Fizz";
        }

        if (input%5 == 0){
            return_value += "Buzz";
        }
        if (return_value == ""){
        return_value = Integer.toString(input);
        }
        return return_value;
    }
}
