import random
import time
import pyttsx3 
engine = pyttsx3.init()
points = 0
IPM = ["Edijs", "Arvids", "Barba", "Vitalija", "Arturs","Rolands", "Rudolfs", "Vadims", "Raitis", "Andrejs"]
Question1 = "How are you"
Answer1 = ["Good :)", "Bad :(", "Normal :|"]
Question2 = "What did you do yesterday"
Answer2 = ["Nothing", "All I wanted to do", "I was not here", "Next question", "I was learning"]
Question3 = "What are you doing today"
Answer3 = ["Nothing", "Sleeping", "Learning", "Programming"]
Question4 = "Did you finnish your project"
Answer4 = ["I'm allmost there", "No", "Yes", "I will tomorow", "Can you help me with it?"]
Question5 = "How do you like working here"
Answer5 = ["I really like this place", "I hate this place", "I quit", "It's okay", "It is like hell in here", "Wonderfull", "I really enjoy working here", "I like the free food"]


def getAllInterns():
        print(IPM)
        engine.say(IPM)
        engine.runAndWait() 



guests = random.randint(0, len(IPM))
isHere = random.sample(set(IPM), guests)


def meeting():
        print("Everyone come here, the meeting is starting in 5 minutes!!!")
        engine.say("Everyone come here, the meeting is starting in 5 minutes")
        engine.runAndWait() 
        time.sleep(5)
         


        for person in isHere:
                print(person + " showed up!")
                engine.say(person + " showed up!")
                engine.runAndWait() 
                print()
        if len(isHere)==len(IPM):
                print("Everyone showed up! Kirill is very happy!")
                engine.say("Everyone showed up! Kirill is very happy!")
                engine.runAndWait() 
                print()
        elif len(isHere)==0:
                print("Nobody showed up! Kirill is very mad!")
                engine.say("Nobody showed up! Kirill is very mad!")
                engine.runAndWait() 
                print()
        now = time.time()
        future = now + 70

        for person in isHere:
                if time.time() > future:
                        print("Sorry we dont have any more time left")
                        engine.say("Sorry we dont have any more time left")
                        engine.runAndWait() 
                        print()
                        break
                        
                else:
                        print(Question1 + " " + person + "?")
                        engine.say(Question1 + " " + person + "?")
                        engine.runAndWait() 
                        answ1 = random.sample(Answer1,1)
                        print(answ1)
                        engine.say(answ1)
                        engine.runAndWait() 
                        print(Question2 + "?")
                        engine.say(Question2 + "?")
                        engine.runAndWait() 
                        answ2 = random.sample(Answer2,1)
                        print(answ2)
                        engine.say(answ2)
                        engine.runAndWait()
                        print(Question3 +"?")
                        engine.say(Question3 + "?")
                        engine.runAndWait() 
                        answ3 = random.sample(Answer3,1)
                        print(answ3)
                        engine.say(answ3)
                        engine.runAndWait()
                        print(Question4 +"?")
                        engine.say(Question4 + "?")
                        engine.runAndWait() 
                        answ4 = random.sample(Answer4,1)
                        print(answ4)
                        engine.say(answ4)
                        engine.runAndWait()
                        print(Question5 +"?")
                        engine.say(Question5 + "?")
                        engine.runAndWait() 
                        answ5 = random.sample(Answer5,1)
                        print(answ5)
                        engine.say(answ5)
                        engine.runAndWait()
                        print("Okay, thank you "+ person +" you earn 25 points.")
                        engine.say("Okay, thank you "+ person +" you earn 25 points.")
                        engine.runAndWait() 
                        print()
                        
                        

        
        for intern in isHere:
                points = 25
                print(intern +" "+ str(points) + " points")
                engine.say(intern +" "+ str(points) + " points")
                engine.runAndWait() 
        print()
        print("People who did not show up get -25 points!")
        engine.say("People who did not show up get -25 points!")
        engine.runAndWait() 
        print()

        for intern in isHere:
                if intern in IPM:
                        IPM.remove(intern)
                        
        for intern in IPM:
            print(intern + " -25 points")
            engine.say(intern + " -25 points")
            engine.runAndWait() 
        print()

def kirill():
        import this
        engine.say("""The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!""")
        engine.runAndWait()

# getAllInterns()
meeting()
# kirill()
