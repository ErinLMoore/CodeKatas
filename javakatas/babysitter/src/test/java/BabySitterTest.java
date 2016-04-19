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
    public void StartsNoEarlierThan5() {
        assertEquals(true, bs.time_evaluator(6));
    }
}
