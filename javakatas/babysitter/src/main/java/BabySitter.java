public class BabySitter {
  
  public int salary_evaluator (int start_time, int bed_time, int end_time){
    int return_int = 0;
    if (end_time<12)
      {end_time += 24;}

    Boolean start_time_valid = start_time_evaluator(start_time);
    Boolean end_time_valid = end_time_evaluator(end_time);

    if (start_time_valid == true && end_time_valid == true){
      for (int i = start_time; i<end_time; i++){
        if (i < bed_time){
          return_int += 12;
        }
        else if (i >= bed_time && i<24){
          return_int += 8;
        }
        else{
          return_int += 16;
          }
        }
      }
    return return_int;
  }
    public Boolean start_time_evaluator (int input){
      if (input >=17)
        {return true;}
      else
        {return false;}
    }
    public Boolean end_time_evaluator (int input){
      if (input <=28)
        {return true;}
      else
        {return false;}
    }
}
