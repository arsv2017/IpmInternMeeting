


import java.util.Random;


public class Intern {


    Random rnd = new Random();


    private boolean isMotivated;
    private boolean isNervous;
    private boolean isPrepared;
    private boolean isPunctual;
    private int earnedPoints;
    private String ID;
    private boolean isPresent;


    public Intern(boolean isMotivated, boolean isNervous, boolean isPrepared, boolean isPunctual, int number) {

        this.isMotivated = isMotivated;
        this.isNervous = isNervous;
        this.isPrepared = isPrepared;
        this.isPunctual = isPunctual;

        this.isPresent = isMotivated | isNervous | isPrepared | isPunctual;
        this.ID = number + "1";


        for (int i = 0; ID.length() < Constants.internIDLength; i++) ID = ID + "1";
    }


    public String getID() {
        return ID;
    }


    public boolean isPresent() {
        return isPresent;
    }


    public boolean talk() {


        if (isPunctual) {

            System.out.println("Intern with ID " + ID + " talks. Fits well within specified time limits!!!");
            return true;
        } else {

            System.out.println("Intern with ID " + ID + " talks, but does not fit too well within specified time limits!!!");
            return false;

        }

    }
        public boolean answerQuestion ( boolean question){

            return question & rnd.nextBoolean();
        }


        public void addPoints ( int earnedPoints){

            this.earnedPoints += earnedPoints;

        }


        @Override
        public String toString () {
            return "Intern{" +
                    "isMotivated=" + isMotivated +
                    ", isNervous=" + isNervous +
                    ", isPrepared=" + isPrepared +
                    ", isPunctual=" + isPunctual +
                    ", points=" + earnedPoints +
                    ", ID='" + ID + '\'' +
                    ", isPresent=" + isPresent +
                    '}';
        }
    }
