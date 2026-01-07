init python:
    variable = 0
    choosen_game = "None"

## This is the "Choose an Activity" screen where you can choose a game to run.
screen chooseGame:
    zorder 5
    frame:
        xalign 0.0
        yfill True
        xsize 500
        xpadding 50
        ypadding 30

        vbox: ## CHOOSE GAME
            text "Choose an Activity":
                size 50 color "#FF55CC"
            
            null height 30

            textbutton "Coin Gambler":
                action [SetVariable("choosen_game","Test"), Call("screenNavigation_Label")]

            null height 30

            textbutton "Dice":
                action [SetVariable("choosen_game","Dice"), Call("screenNavigation_Label")]

            null height 30

            textbutton "Pokehim":
                action [SetVariable("choosen_game","PokerGame"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Gallery":
                action [SetVariable("choosen_game","Gallery"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Lotto":
                action [SetVariable("choosen_game","Lotto"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Roulette":
                action [SetVariable("choosen_game","Roulette"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Play Finger Tango":
                action [SetVariable("choosen_game","PuzzleGame"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Play Space Explorer":
                action [SetVariable("choosen_game","SpaceExplorer"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Exploration System":
                action [SetVariable("choosen_game","Exploration"), Call("screenNavigation_Label")]

            # null height 30
            
            # textbutton "Tower Defense":
            #     action [SetVariable("choosen_game","TowerDefense"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "Play GAME TEST":
                action [SetVariable("choosen_game","Puzzlegame2"), Call("screenNavigation_Label")]

            null height 30
            
            textbutton "The Lounge":
                action [SetVariable("choosen_game","CharSprite"), Call("screenNavigation_Label")]

    ## CONTROL CHARS
    if renpy.get_screen("chooseGame"):
        $ renpy.hide("exp_composite")


## This is just renpy code to open the choosen game.
label screenNavigation_Label:

    if choosen_game == "None":
        call screen chooseGame

    elif choosen_game == "Dice":
        call screen dice_Game

    elif choosen_game == "Test":
        call screen coingambler

    elif choosen_game == "Gallery":
        call screen galleryscreen

    elif choosen_game == "Lotto":
        call screen lottogame

    elif choosen_game == "Roulette":
        call screen rouletteScreen

    elif choosen_game == "PuzzleGame":
        call screen puzlegameScreen

    elif choosen_game == "PokerGame":
        call screen pokergameScreen

    elif choosen_game == "CharSprite":
        call screen charspriteScreen

    elif choosen_game == "TowerDefense":
        call screen towerdefScreen

    elif choosen_game == "SpaceExplorer":
        call screen spaceexplorerscreen

    elif choosen_game == "Exploration":
        call screen exploration_screen

    elif choosen_game == "Puzzlegame2":
        call screen puzzlegame2screen