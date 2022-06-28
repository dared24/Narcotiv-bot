try:
    import pyttsx3
    import random
    import time
    import tkinter




    def Gui():

        import tkinter
        m = tkinter.Tk()
        button = tkinter.Button(m, text='Stop', width=25)
        button.pack()

        w = tkinter.Canvas(m, width=40, height=60)
        w.pack()
        m.mainloop()

    engine = pyttsx3.init()

    print("NOTICE : pls answer most of the questions in yes or no")
    print('\n')
    print('\n')

    engine.say("Welcome to Narcotic - a personalised medical chat bot")
    print("Welcome to Narcotic - a personalised medical chat bot")
    engine.runAndWait()

    engine.say("HOPE YOU ARE DOING FINE ")
    print("HOPE YOU ARE DOING FINE ")
    engine.runAndWait()


    def cure_of_diseases(ingine=engine):
        ingine.say("CURE OF WHICH DISEASE DO U WANT: ")
        engine.runAndWait()
        cure1 = input("CURE OF WHICH DISEASE DO U WANT: ").strip().upper()

        if cure1 == "NONE":
            print("THANK YOU FOR YOUR TIME!")
        cure = {
            'JAUNDICE': 'BLOOD TRANSFUSION OR PHOTOTHERAPY.',
            'Conjunctivitis': 'artificial tears, cleaning your eyelids with a wet cloth, and applying cold or warm '
                              'compresses several times daily, avoiding contact lenses '
            ,
            'cold and flu': 'most people recover from cold and flu on their own within 2 weeks but to recover faster '
                            'some '
                            'home remedies can be applied like drinking chicken soup, drinking hot honey water, '
                            'eating garlic, eating vitamin c fruits, staying hydrated, taking rest '
        }
        print(cure[cure1])


    def diseases_identify():
        engine.say("ENTER YOUR SYMPTOM: ")
        take_input_diseases = input("ENTER YOUR SYMPTOM: ")
        engine.runAndWait()
        disease_database = {'FEVER': 'JAUNDICE', 'watery, loose stools, frequent bowel movements, cramping or pain '
                                                 'in the abdomen, nausea, bloating, possibly fever or bloody stools,'
                                                 ' depending on the cause': 'diarrhoea '
                            }
        if any(word in disease_database for word in take_input_diseases.split()):
            print(disease_database[take_input_diseases])



    def health_checkup():
        engine.say("Welcome to health checkup  ")

        print("Welcome to health checkup ")
        engine.runAndWait()

        print("\n")
        engine.say("DO YOU HAVE ANY GENETIC DISEASES?: ")
        engine.runAndWait()
        first_Questions = input(
            "DO YOU HAVE ANY GENETIC DISEASES?: ").strip()

        engine.say("DO YOU SUFFER FROM HYPERTENSION?: ")
        engine.runAndWait()
        second_question = input('DO YOU SUFFER FROM HYPERTENSION?: ').strip()

        engine.say("DO YOU HAVE CANCER?")
        engine.runAndWait()
        third_Questions = input('DO YOU HAVE CANCER?: ').strip()

        engine.say("HOW MUCH ARE YOU PHYSICALLY ACTIVE?")
        engine.runAndWait()
        fourth_Questions = input('HOW MUCH ARE YOU PHYSICALLY ACTIVE?: ').strip()

        engine.say("DO YOU HAVE ANY ALLERGIES?")
        engine.runAndWait()
        fifth_Questions = input('DO YOU HAVE ANY ALLERGIES?: ').strip()

        engine.say("DO YOU SUFFER FROM HIGH CHOLESTEROL?")
        engine.runAndWait()
        sixth_Questions = input('DO YOU SUFFER FROM HIGH CHOLESTEROL: ?').strip()

        engine.say("DO YOU HAVE ANY PROBLEMS WITH YOUR TEETH OR MOUTH?")
        engine.runAndWait()
        seventh_Questions = input(
            'DO YOU HAVE ANY PROBLEMS WITH YOUR TEETH OR MOUTH?: ').strip()

        engine.say("DO YOU HAVE ANY PROBLEMS GOING FOR A POO E.G. CONSTIPATION, DIARRHOEA, OR INCONTINENCE?: ")
        engine.runAndWait()
        eight_Questions = input(
            'DO YOU HAVE ANY PROBLEMS GOING FOR A POO E.G. CONSTIPATION, DIARRHOEA, OR INCONTINENCE?: '
        ).strip()

        engine.say("DO YOU HAVE ANY PROBLEMS GOING FOR A WEE E.G. PAIN, BLOOD OR INCONTINENCE?")
        engine.runAndWait()
        ninth_Questions = input(
            'DO YOU HAVE ANY PROBLEMS GOING FOR A WEE E.G. PAIN, BLOOD OR INCONTINENCE?: '
        ).strip()

        engine.say("WHAT ARE YOUR GENDER AND AGE?")
        engine.runAndWait()
        tenth_Questions = input('WHAT ARE YOUR GENDER AND AGE?: ').strip()

        if (second_question == "yes") and (third_Questions == "yes") and (
                fifth_Questions == "yes") and (sixth_Questions == 'yes') and (
                seventh_Questions == "yes") and (eight_Questions
                                                 == 'yes') and (ninth_Questions
                                                                == 'yes'):
            print(
                'Your health is not very good we recommend that you take kare of your health'
            )

        elif (second_question == "no") and (third_Questions == "no") and (
                fifth_Questions == "no") and (sixth_Questions == 'no') and (
                seventh_Questions == "no") and (eight_Questions
                                                == 'no') and (ninth_Questions
                                                              == 'no'):
            print("Your health is in excellent condition")
        elif (second_question == "no") and (third_Questions == "yes") and (
                fifth_Questions == "yes") and (sixth_Questions == 'no') and (
                seventh_Questions == "no") and (eight_Questions
                                                == 'yes') and (ninth_Questions
                                                               == 'no'):
            print("")


    def symptoms_of_diseases():
        engine.say("So do u want to get the symptoms of a particular illness: ")
        symptoms1 = input(
            "So do u want to get the symptoms of a particular illness: ").lower()
        engine.runAndWait()
        if symptoms1 == "no":
            print("ok")
        elif symptoms1 == "yes":
            engine.say("pls enter the disease on which u want symptoms: ")
            c = input("pls enter the disease on which u want symptoms: ")
            engine.runAndWait()
            print('\n')
            data_base2 = {
                'Jaundice':
                    'Fever. Chills. Abdominal pain. Flu-like symptoms. Change in skin color. '
                    'Dark-colored urine and/or clay-colored stool.',
                'Diabetes':
                    'Urinate ('
                    'pee) a lot, '
                    'often at '
                    'night, '
                    'are very '
                    'thirsty, '
                    'lose weight '
                    'without '
                    'trying, '
                    'are very '
                    'hungry, '
                    'have blurry '
                    'vision, '
                    'have numb '
                    'or tingling '
                    'hands or '
                    'feet, '
                    'feeling '
                    'very tired, '
                    'have very '
                    'dry skin, '
                    'have sores '
                    'that heal '
                    'slowly, '
                    'have more '
                    'infections '
                    'than usual.',
                'Cold and flu':
                    'Fever or feeling feverish / chills, cough, sore-throat, runny or stuffy-nose, '
                    'muscle or body-aches, '
                    'headaches, and fatigue(tiredness) ',
                'Conjunctivitis or pink eye':
                    'Redness, itching, tearing, burning sensation, pus - like discharge '
                    'and / or '
                    'crusting of the eyelids ',
                'Diarrhea':
                    'Watery, loose stools, frequent bowel movements, cramping or pain in the abdomen, '
                    'nausea, bloating, possibly fever or bloody stools, depending on the cause '
            }
            print(data_base2[c])
        engine.say("Do you wanna continue researching on symptoms?: ")
        symptoms_continue = input(
            "Do you wanna continue researching on symptoms?: ").upper().strip()
        engine.runAndWait()
        if symptoms_continue == 'YES':
            print(symptoms1)
            print('\n')
        else:
            print("Ok thank you for using symptoms")


    engine.say("So what would you like to do today ")
    print("So what would you like to do today ")
    engine.runAndWait()


    def create_function():
        engine.say(" Would you like to "
                   "\n"
                   "1:  Assess yourself by taking our test? or"
                   "\n"
                   "2:  Do You want to know the symptoms of a particular illness? or"
                   "\n"
                   "3:  Do You want to know the cure of a particular illness? or"
                   "\n"
                   "4:  Do you want to identify your disease"
                   '\n'
                   "You can write the 1,2,3,4 only, you can write exit for exiting: ")
        engine.runAndWait()
        input2 = input(
            " Would you like to "
            "\n"
            "1:  Assess yourself by taking our test? or"
            "\n"
            "2:  Do You want to know the symptoms of a particular illness? or"
            "\n"
            "3:  Do You want to know the cure of a particular illness? or"
            "\n"
            "4:  Do you want to identify your disease"
            '\n'
            "You can write the 1,2,3,4 only, you can write exit for exiting: ").lower()

        if input2 == '1':
            health_checkup()
        elif input2 == '2':
            symptoms_of_diseases()
        elif input2 == "3":
            cure_of_diseases()
        elif input2 == '4':
            diseases_identify()
        elif input2 == 'exit'.lower():
            exit()
        else:
            engine.say("You have entered wrong values!!!")
            print("You have entered wrong values!!!")
            engine.runAndWait()

            exit()


    create_function()
    engine.say("Do you want to continue using our bot:")

    continue_using = input(
        "Do you want to continue using our bot: ").strip().lower()
    engine.runAndWait()

    if continue_using == 'yes':
        create_function()
    else:
        print("Thank you for using this bot ")

    print('\n')
    time.sleep(2)

    raise_queries = input("Do you have any other queries?(Write yes or no): ")
    if raise_queries == "yes":
        print("Pls provide us with your name and contact info")
        input22 = input("Name: ")
        input33 = input("Contact info: ")
        problem = input("Pls tell us your problem or any other feedbacks: ")
        print("Your problem has been recorded ")
        random2 = random.randrange(0, 100, 1) + random.randrange(0, 1000, 2)
        print(f"Your ticket number is: {random2}")
    else:
        print("Thank you for your support")

    print(
        "If you have different queries pls contact us at caniattainsomepeace@gmail.com"
    )
except KeyboardInterrupt:
    print("You have interrupted the program")
