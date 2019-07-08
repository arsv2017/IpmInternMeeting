


import java.util.ArrayList;
import java.util.Random;


public class MainApp {



    public static void main(String[] args) {

        ArrayList<Intern> interns = getAllInterns();
        Kirill kirill = new Kirill();
        MeetingRoom mr = new MeetingRoom();
        ArrayList<Intern> internsTransformed = mr.meeting(interns, kirill);


        System.out.println("\n\nMEETING CONCLUSION:");
        for (Intern intern : internsTransformed) {


            System.out.println(intern.toString());
        }
    }






    public static ArrayList<Intern> getAllInterns() {
        String internID;
        Random rnd = new Random();
        ArrayList<Intern> ipmInterns = new ArrayList<>();


        for (int i = 0; i < Constants.numberOfInterns; i++) {

            ipmInterns.add(new Intern(rnd.nextBoolean(), rnd.nextBoolean(), rnd.nextBoolean(), rnd.nextBoolean(), i + 1));

        }

        return ipmInterns;


    }
}