public class BabySitter {

  private int start_to_bed_wage = 12;
  private int bed_to_mid_wage = 8;
  private int mid_to_end_wage = 16;

  public int check_time_and_evaluate_salary (int start_time, int bed_time, int end_time){
    int total_salary = 0;
    if (end_time<12)
      {end_time += 24;}

    Boolean start_time_valid = start_time_evaluator(start_time);
    Boolean end_time_valid = end_time_evaluator(end_time);

    if (start_time_valid && end_time_valid ){
      total_salary = calculate_salary(start_time, bed_time, end_time);
        }
    return total_salary;
    }

  public int calculate_salary(int start_time, int bed_time, int end_time){
    int return_val = 0;
    for (int i = start_time; i<end_time; i++){
      if (i < bed_time){
        return_val += start_to_bed_wage;
      }
      else if (i >= bed_time && i<24){
        return_val += bed_to_mid_wage;
      }
      else{
        return_val += mid_to_end_wage;
        }
      }
      return return_val;
    }

  public Boolean start_time_evaluator (int start_time){
    if (start_time >=17)
      {return true;}
    else
      {return false;}
    }
    
  public Boolean end_time_evaluator (int end_time){
    if (end_time <=28)
      {return true;}
    else
      {return false;}
  }
}
