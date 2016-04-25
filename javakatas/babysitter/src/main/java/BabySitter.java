import java.util.stream.IntStream;

public class BabySitter {

  //instead of for loop, use intersecional arrays or buckets or something i forget

  private int startToBedWage = 12;
  private int bedToMidWage = 8;
  private int midToEndWage = 16;
  private int minimumStartTime= 17;
  private int maximumEndTime= 28;
  private int midnight = 24;

  public int checkTimeAndEvaluateSalary (int startTime, int bedTime, int endTime){
    int totalSalary = 0;
    endTime = normalizeEndTime(endTime);

    Boolean startTimeValid = startTimeEvaluator(startTime);
    Boolean endTimeValid = endTimeEvaluator(endTime);

    if (startTimeValid && endTimeValid ){
      totalSalary = calculateSalary(startTime, bedTime, endTime);
        }
    return totalSalary;
    }

  public int calculateSalary(int startTime, int bedTime, int endTime){
  return IntStream.of((bedTime - startTime)*startToBedWage,
                            (midnight - bedTime)*bedToMidWage,
                            (endTime - midnight)*midToEndWage).sum();
    }

  public Boolean startTimeEvaluator (int startTime){
    if (startTime >=minimum_startTime)
      {return true;}
    else
      {return false;}
    }

  public Boolean endTimeEvaluator (int endTime){
    if (endTime <=maximum_endTime)
      {return true;}
    else
      {return false;}
  }

  public int normalizeEndTime(int endTime){
    if (endTime<midnight/2)
      {endTime += midnight;}
    return endTime;
  }
}
