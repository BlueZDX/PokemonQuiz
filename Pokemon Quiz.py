def game():
    print("WELCOME TO THE POKEMON QUIZ!!")

    playing = input("Enter Game?")

    if playing != "yes":
        print("Ok thats good *sniffle*")
    if playing == "yes":
        print("HELL YEAH LETS DO THIS!!!")
        score = 0

        answer = input("What was the first pokemon ever made in the pokemon game series? ")
        if answer == "Rhydon":
            print("Man you got through this question quicker than an onyx with dig heres your 1st gym badge!")
            score += 1
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 1

        answer = input("What number is Blaziken in the  national pokedex? ")
        if answer == "257":
            print("Man you flare blitzed your way to your 2nd gym badge!")
            score += 2
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 1

        answer = input("What was flying type going to be called before they changed it to flying type? ")
        if answer == "Bird":
            print("Woah you areal ACED your way to your 3rd gym badge! (see what i did there.)")
            score += 3
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 1

        answer = input("What is  Eevee's grass type evolution named? ")
        if answer == "Leafeon":
            print("Woah you're rolling along like a tumbleweed heres your 4th gym badge")
            score += 4
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 2

        answer = input("What is Daramatian's Galarian typing?")
        if answer == "Ice":
            print("Can't believe my ice types lost, heres your 5th gym badge!")
            score += 5
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 2

        answer = input("What is Zoroark's ability called")
        if answer == "Illousion":
            print("before there was light there was nothing but darkness...heres your 6th gym badge")
            score += 6
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 3

        answer = input("What was the first pokemon ever created by Arceus")
        if answer == "Mew":
            print("I am psy...SHOCKED you got that answer right, heres your 7th gym badge")
            score += 7
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 3

        answer = input("What was the first pokemon that ever mega evolved")
        if answer == "Rayquaza":
            print("Man you dragon RUSHED through this one! Heres your 8th gym badge")
            score += 8
        else:
            print("You blacked out and ran to the nearest pokemon center dropping 1 point.")
            score -= 3

    print("Looks like you got most or all of the questions right, you have a total of" + str(score))
    print("and a total score percent of" + str(score / 8 * 100) + "%")

    if score <= 36:
        print("")


    if score >= 36:
        print("WELCOME TO THE ELIETE 4")

        challenge = input("YOU HAVE OBTAINED ALL 8 GYM BADGES DO YOU WISH TO CHALLENGE THE ELITE 4")

        if challenge != "yes":
            print("You can always play again if you want")

        if challenge == "yes":
            print("If you get a single question wrong all of your points dissapear and the game ends, each elite 4 member is worth 500 points except the champion")
        scoreEF = score

        answer = input("What pokemon in pokemon moon was the lost man looking for in the haina desert when he asks you to show him a moon pokemon? ")
        if answer == "Lunatone":
            print("you actually won, ridiculous!")
            score += 500
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")


        answer = input("What is the  name of the location where you can find mew in the special pokemon R/S/E event? ")
        if answer == "Faraway Island":
            print("WHAT I NEVER LOSE NO NO NO NO!!!")
            score += 500
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")


        answer = input("What is the name of a glitch where if you obtain it, it ruins your save file in pokemon platnum? ")
        if answer == "Bad Egg":
            print("....")
            score += 500
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")


        answer = input("What pokemon was Brendan attacked by that made him wear his iconic cap? ")
        if answer == "Salamence":
            print("Tch beginners luck!")
            score += 500
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")


        answer = input("Who was the first CEO of the pokemon company? ")
        if answer == "Tsunekazu Ishihara":
            print("WE'RE NOT DONE YET! NO ONE BEATS ME!")
            score += 1000
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")


        answer = input("What was Tsunekazu Ishihara's favorite pokemon")
        if answer == "Exeggutor":
            print("YOU'RE NOT BEATING ME I DON'T LOSE!")
            score += 1500
        else:
            print("You blacked out and ran to the nearest pokemon center dropping all your points.")
            score -= 99999

    if score <= 0:
        print("")
    else:
        print("")

        answer = input("LAST BUT NOT LEAST.... WHAT IS MY FAVORITE POKEMON!!!")
        if answer == "Blaziken":
            print("NOOOOOOOOOOOOOOOOOOO I LOST HOW IMPOSSIBLE I NEVER LOSE!!!")
            score += 2000
        else:
            print("I TOLD YOU I NEVER LOSE!!!!")

    if score <= 0:
        print("")
    else:
        print("Man you actually got them all right!")

    if score > 36:
        print("Looks like you got every question right...WOW heres your score:" + str(score))
        print("and heres your score percent:" + str(score / 8 * 100) + "%")
    print("Thanks for playing")
    
play = "yes"

while play == "yes":
    game()
    play = input("Wanna play again if so press yes: ")
