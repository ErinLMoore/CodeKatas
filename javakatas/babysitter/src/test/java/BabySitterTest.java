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
      public void returns_false_if_end_time_after_28() {
      Boolean expected = false;
      Boolean result = bs.end_time_evaluator(29);
      assertEquals(expected, result);
     }
     @Test
      public void gets_paid_12_an_hour_from_start_to_bed() {
      int expected = 76;
      int result = bs.calculate_salary(17,22, 24);
      assertEquals(expected, result);
     }
     @Test
      public void gets_paid_8_an_hour_from_bed_to_mid() {
      int expected = 16;
      int result = bs.calculate_salary(22,22, 24);
      assertEquals(expected, result);
     }
     @Test
      public void gets_paid_16_an_hour_from_mid_to_end() {
      int expected = 32;
      int result = bs.calculate_salary(24,24, 26);
      assertEquals(expected, result);
     }
     @Test
      public void test_invalid_start_times_return_0_salary() {
      int expected = 0;
      int result = bs.check_time_and_evaluate_salary(16,24, 2);
      assertEquals(expected, result);
     }
     @Test
      public void test_invalid_end_times_return_0_salary() {
      int expected = 0;
      int result = bs.check_time_and_evaluate_salary(18,24,5);
      assertEquals(expected, result);
     }
     @Test
      public void test_salary_end_to_end() {
      int expected = 100;
      int result = bs.check_time_and_evaluate_salary(18,23,2);
      assertEquals(expected, result);
     }
}
