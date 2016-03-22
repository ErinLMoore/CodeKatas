import org.junit.Before;
import org.junit.Test;

import static org.junit.Assert.*;

/**
 * Created by erinmoore on 3/15/16.
 */
public class FizzBuzzTest{
    FizzBuzz fb;

    @Before
    public void setUp(){
         fb = new FizzBuzz();
    }

    @Test
    public void returnsOneifGivenOnes() {
        assertEquals(String.valueOf("1"), fb.fizzbuzzer(1));
    }

    @Test
    public void returnsTwoifGivenTwo() {
        assertEquals(String.valueOf("2"), fb.fizzbuzzer(2));
    }

    @Test
    public void returnsFizzifGivenThree() {
        assertEquals(String.valueOf("Fizz"), fb.fizzbuzzer(3));
    }

    @Test
    public void returnsFizzifGivenSix() {
        assertEquals(String.valueOf("Fizz"), fb.fizzbuzzer(6));
    }

    @Test
    public void returnsBuzzifGivenTen() {
        assertEquals(String.valueOf("Buzz"), fb.fizzbuzzer(10));
    }

    @Test
    public void returnsFizzBuzzifGivenSixty() {
        assertEquals(String.valueOf("FizzBuzz"), fb.fizzbuzzer(60));
    }
}
