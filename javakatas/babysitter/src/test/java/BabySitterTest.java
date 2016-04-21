import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;
import org.junit.*;

/**
 * Created by erinmoore on 3/15/16.
 */
 public class BabySitterTest{
     BabySitter bs;

     @Before
     public void setUp(){
          bs = new BabySitter();
     }
     @Test
      public void returns_true_if_start_time_17_or_after() {
      Boolean expected = true;
      Boolean result = bs.start_time_evaluator(18);
      assertEquals(expected, result);
     }
     @Test
      public void returns_false_if_start_time_before_17() {
      Boolean expected = false;
      Boolean result = bs.start_time_evaluator(15);
      assertEquals(expected, result);
     }
     @Test
      public void returns_true_if_end_time_before_28() {
      Boolean expected = true;
      Boolean result = bs.end_time_evaluator(26);
      assertEquals(expected, result);
     }
     @Test
      public void gets_paid_12_an_hour_from_start_to_bed() {
      Integer expected = 60;
      Integer result = bs.salary_evaluator(5,10);
      assertEquals(expected, result);
     }
}
