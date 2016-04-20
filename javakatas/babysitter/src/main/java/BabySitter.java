public class BabySitter {
  public static void main(String[] args){
    System.out.println("pretend this fizzbuzzes");
  }
    public Boolean start_time_evaluator (int input){
      if (input >=18)
        {return true;}
      else
        {return false;}
    }
    public Boolean end_time_evaluator (int input){
      if (input<12)
        {input += 12;}
      if (input <=28)
        {return true;}
      else
        {return false;}
    }
}
