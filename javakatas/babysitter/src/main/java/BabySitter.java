public class BabySitter {
  public static void main(String[] args){
    System.out.println("pretend this fizzbuzzes");
  }
  public Integer salary_evaluator (int start_time, int bed_time){
    Integer return_int = 0;
    for (int i = start_time; i<bed_time; i++){
      return_int += 12;
    }
    return return_int;
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
