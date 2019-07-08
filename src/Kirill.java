

import java.util.Random;


public class Kirill {
    Random rnd = new Random();


    public boolean generateQuestion() {
        return rnd.nextBoolean();
    }


    public boolean validateAnswer(boolean question, boolean answer) {

        if (question==answer) return true;

        return false;
    }


    public String describeValueableTasksAndBrightFuture() {


        return "\n\nValuable tasks is a key to much brighter future!!!\n\n";
    }
}


