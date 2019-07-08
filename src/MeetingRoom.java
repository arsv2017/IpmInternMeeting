import java.util.ArrayList;
import java.util.Random;

public class MeetingRoom {


    public ArrayList<Intern> meeting(ArrayList<Intern> ipmInterns, Kirill kirill) {




        Random rnd = new Random();
        boolean question;
        boolean answer;
        ArrayList<Intern> absentInternList = new ArrayList<>();

        for (Intern intern : ipmInterns) {
            try {
                if (!intern.isPresent())
                    throw new NullInternException("Intern with ID " + intern.getID() + " is absent!!!");


                if (intern.talk()) intern.addPoints(Constants.extraPointsForPunctuality);

                do {
                    question = kirill.generateQuestion();
                    answer = intern.answerQuestion(question);
                    if (kirill.validateAnswer(question, answer)) intern.addPoints(Constants.pointsForCorrectAnswer);
                } while (rnd.nextBoolean() & rnd.nextBoolean() & rnd.nextBoolean());


            } catch (NullInternException e) {
                System.out.println(e);
              absentInternList.add(intern);


            }


        }

        ipmInterns.removeAll(absentInternList);

        System.out.println(kirill.describeValueableTasksAndBrightFuture());

        return ipmInterns;
    }



















}
