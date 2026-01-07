init python:
    ## This is pure python code, which is inside the "init python" block
    
    random_var = ""
    
    #####################
    ### CODE FOR FINGER TANGO STARTS HERE
    # ▲►▼◄
    # ←↑↓→
    # ⮘⮙⮛⮚
    # These are all variables that are used as part of the functions    
    playing_puzzle = False
    dirs = ["←","↑","↓","→"]
    sequence = []
    playersequence = []

    # MODIFIERS
    greentrail = True
    greentrailcolor = "#555"
    nofailmode = False
    colorcoded = 2
    ac_left = "#4CD"
    ac_right = "#F77"
    ac_up = "#EC3"
    ac_down = "#4C5"

    difflevel = 0
    highestlevel = 0
    strikes = 3
    strikesmax = 3
    strikescost = 1500

    puzzletimelimit = 5
    puzzletimelimitmax = 5
    puzzletimeleft = 0
    puzzletimecost = 100

    puzzlescore = 0
    puzzlescorefinal = 0

    # Upgrade cost increase
    costincrease = 1.1
    coinslifetime = 0

    ### UPGRADE VARIABLES
    diffmultiplier = 1
    diffmax = 1
    diffcost = 50

    def upgradeDiff():
        global diffmax
        global diffcost
        global coins

        if coins >= diffcost:
            coins -= diffcost

            diffmax += 1
            renpy.play(audio.upgrade, channel="audio")

            # 50% Increase
            diffcost = int(diffcost * costincrease)

    def upgradeTime():
        global puzzletimelimitmax
        global puzzletimelimit
        global puzzletimecost
        global coins

        if coins >= puzzletimecost:
            coins -= puzzletimecost

            puzzletimelimitmax += 0.1
            renpy.play(audio.upgrade, channel="audio")

            # 50% Increase
            puzzletimecost = int(puzzletimecost * costincrease)

            UpdateTimeLimit()

    def upgradeLives():
        global strikes
        global strikesmax
        global strikescost
        global coins

        if coins >= strikescost:
            coins -= strikescost

            strikesmax += 1
            renpy.play(audio.upgrade, channel="audio")

            # 50% Increase
            strikescost = int(strikescost * costincrease)

    def generatePuzzle():
        global sequence
        global playersequence
        global difflevel
        global strikes
        global puzzletimelimit

        # if difflevel <= 0:
        #     pass
        # else:
        if playersequence == sequence: ## Win condition
            pass
        else: ## Lose level
            if difflevel > 0:
                difflevel -= 1
                strikes -= 1
                renpy.play(audio.fail, channel="audio", relative_volume=1.8)
            # if difflevel > 0:
    
        if difflevel > 0:

            sequence = []
            playersequence = []

            if difflevel <= 15:
                for num in range(difflevel+4):
                    direction = random.choice(dirs)
                    sequence.append(direction)
            elif difflevel > 15:
                for num in range(20):
                    direction = random.choice(dirs)
                    sequence.append(direction)

            UpdateTimeLimit()

        else:

            sequence = []
            playersequence = []
            puzzletimelimit = 5

            for num in range(3):
                direction = random.choice(dirs)
                sequence.append(direction)
            

    def playerSequenceInput(inputdir):
        global playersequence

        # if inputdir == "→":
        #     inputdir = "►"

        playersequence = playersequence[:]

        char_pos = len(playersequence)

        if char_pos < len(sequence):

            if sequence[char_pos] == inputdir:
                renpy.play(audio.note, channel="audio", relative_volume=0.5)
                playersequence.append(inputdir)
            else:
                renpy.play(audio.miss, channel="audio", relative_volume=1.5)
                if nofailmode == False:
                    playersequence = []

        checkPuzzleWin()

    def checkPuzzleWin():
        global playersequence
        global difflevel
        global puzzletimeleft
        global highestlevel
        global coins
        global puzzlescore

        if playersequence == sequence:
            if difflevel > highestlevel:
                highestlevel = difflevel

            # coins += difflevel
            puzzlescore += difflevel

            difflevel += 1
            puzzletimeleft = 0

            renpy.play(audio.complete, channel="audio")

    def puzzleTimer():
        global puzzletimelimit
        global puzzletimeleft

        if puzzletimeleft > 0:
            puzzletimeleft -= 0.1

        if puzzletimeleft <= 0:
            generatePuzzle()
            puzzletimeleft = puzzletimelimit

    def playPuzzle():
        global playing_puzzle
        global strikes
        global difflevel
        global puzzlescore

        if playing_puzzle == False:
            renpy.play(audio.button,channel="audio")
            strikes = strikesmax
            difflevel = 0
            puzzlescore = 0
            playing_puzzle = True
        elif playing_puzzle == True:
            # renpy.play(audio.fail, channel="audio")
            difflevel = 0
            UpdateTimeLimit()
            AwardCoins()
            playing_puzzle = False

    def UpdateTimeLimit():
        global puzzletimelimit
        difftimemod = 0

        # should be 16
        if difflevel > 16:
            difftimemod = (difflevel - 16) * 0.1

        puzzletimelimit = puzzletimelimitmax+0.5-(0.5*diffmultiplier)- difftimemod
       
    def CalcPuzzleScore():
        global puzzlescorefinal

        puzzlescorefinal = int(puzzlescore * (1*(diffmultiplier)))

        return puzzlescorefinal

    def AwardCoins():
        global coins
        global coinslifetime
        global puzzlescore

        coins += CalcPuzzleScore()
        coinslifetime += CalcPuzzleScore()

        if CalcPuzzleScore() > 0:
            renpy.play(audio.coin2,channel="audio", relative_volume=1.5)

    def ToggleGreenTrail():
        global greentrail

        renpy.play(audio.button,channel="audio")

        if greentrail == True:
            greentrail = False
        elif greentrail == False:
            greentrail = True

    def ToggleNoFail():
        global nofailmode

        renpy.play(audio.button,channel="audio")

        if nofailmode == True:
            nofailmode = False
        elif nofailmode == False:
            nofailmode = True

    def ToggleColorCoded():
        global colorcoded

        renpy.play(audio.button,channel="audio")
        colorcoded += 1

        if colorcoded == 3:
            colorcoded = 0

    def AdjustDiff(value):
        global diffmultiplier

        if isinstance(value, int):
            if value > 0:
                renpy.play(audio.up,channel="audio")
            if value < 0:
                renpy.play(audio.down,channel="audio")

        if value == "min":
            renpy.play(audio.down,channel="audio")
            value = 0
            diffmultiplier = 1
        if value == "max":
            renpy.play(audio.up,channel="audio")
            value = 0
            diffmultiplier = diffmax

        diffmultiplier += value/10

        if diffmultiplier < 1:
            diffmultiplier = 1

        if diffmultiplier > diffmax:
            diffmultiplier = diffmax

        UpdateTimeLimit()

## This ends the "init python" block, and along with it, python code.
## Code from here on out is 'renpy' code


## GAME AUDIOS
define audio.note = "Fantasy_UI (1).wav"
define audio.miss = "Fantasy_UI (11).wav"
define audio.complete = "Fantasy_UI (6).wav"
define audio.fail = "Fantasy_UI (16).wav"
define audio.upgrade = "SkywardHero_UI (13).wav"

define audio.coin = "Coin Sound.mp3"
define audio.coin2 = "Coin Sound 2.mp3"
define audio.button = "Fantasy_UI (8).wav"
define audio.up = "SkywardHero_UI (7).wav"
define audio.down = "SkywardHero_UI (12).wav"

define puzzlemloop1 = "DavidKBD - Cosmic Pack 05 - Stellar Confrontation-Variation1.ogg"
define puzzlemloop2 = "DavidKBD - Cosmic Pack 05 - Stellar Confrontation-Variation2.ogg"
define puzzlemloop3 = "DavidKBD - Cosmic Pack 05 - Stellar Confrontation-Variation3.ogg"
define puzzlemloop4 = "DavidKBD - Cosmic Pack 06 - Lunar Rampage-variation1.ogg"
define puzzlemloop5 = "DavidKBD - Cosmic Pack 06 - Lunar Rampage-variation2.ogg"
define puzzlemloop6 = "DavidKBD - Cosmic Pack 06 - Lunar Rampage-variation3.ogg"
define puzzlemloop7 = "DavidKBD - Cosmic Pack 03 - Nebula Run-variation1.ogg"
define puzzlemloop8 = "DavidKBD - Cosmic Pack 03 - Nebula Run-variation3.ogg"

define puzzlemusic = [puzzlemloop1,puzzlemloop2,puzzlemloop3,puzzlemloop4,puzzlemloop5,puzzlemloop6,puzzlemloop7,puzzlemloop8]



## A "Screen" describes a visual area in Ren'py that the user can interact with
## All code within is part of the 'renpy' code, check the documentation for more clarity

screen puzlegameScreen:
    zorder 5
    frame:
        xalign 0.05
        yalign 0.5
        xsize 1000
        ysize 800
        xpadding 20
        ypadding 20

        hbox: ## BUTTONS AND INFO
            xalign 0.5
            spacing 20
            label "Finger Tango"
            textbutton "Return":
                    action [SetVariable("choosen_game","None"),Call("screenNavigation_Label")]

        ## GAME SCREEN // PLAYING
        if playing_puzzle == True:

            vbox:
                xalign 0.5
                yalign 0.5

                spacing 20

                text "Level [difflevel]" xalign 0.5 size 35
                text "Time Limit: [puzzletimelimit:.2f]" xalign 0.5 size 30

                ### TIMER
                fixed:
                    ysize 40
                    xsize 750
                    if difflevel > 0:
                        bar value AnimatedValue(puzzletimeleft,puzzletimelimit):
                            xsize 35*len(sequence) ysize 40 xalign 0.5
                        text "[puzzletimeleft:.1f]" xalign 0.5 yalign 0.5 size 30

                # ←↑↓→

                ### SEQUENCE
                vbox:
                    xalign 0.5
                    hbox:
                        xalign 0.5
                        ## GREEN TRAIL
                        for x in range(len(playersequence)):
                            text sequence[x]:
                                yalign 0.5
                                bold True
                                size 40

                                if colorcoded == 1 or colorcoded == 2:
                                    if sequence[x] == "→":
                                        color ac_right
                                    if sequence[x] == "←":
                                        color ac_left
                                if colorcoded == 2:
                                    if sequence[x] == "↑":
                                        color ac_up
                                    if sequence[x] == "↓":
                                        color ac_down

                                if greentrail == True:
                                    color greentrailcolor
                                else:
                                    color "#AAA"
                        
                        ## FOCUS MODE
                        if len(playersequence) < len(sequence):
                            text sequence[len(playersequence)]:
                                yalign 0.5
                                bold True
                                size 40

                                # if greentrail == False:
                                color "#AAA"
                                # if sequence[len(playersequence)] == "→":
                                #     color "#5CC"
                                if colorcoded == 1 or colorcoded == 2:
                                    if sequence[len(playersequence)] == "→":
                                        color ac_right
                                    if sequence[len(playersequence)] == "←":
                                        color ac_left
                                if colorcoded == 2:
                                    if sequence[len(playersequence)] == "↑":
                                        color ac_up
                                    if sequence[len(playersequence)] == "↓":
                                        color ac_down
                            
                        ## REST OF SEQUENCE
                        for x in range(len(sequence)-len(playersequence)-1):
                            if x < len(sequence):
                                text sequence[x+len(playersequence)+1]:
                                    yalign 0.5
                                    size 40
                                    bold True
                                    color "#AAA"

                                    # if sequence[x+len(playersequence)+1] == "→":
                                    #     color "#5CC"
                                    if colorcoded == 1 or colorcoded == 2:
                                        if sequence[x+len(playersequence)+1] == "→":
                                            color ac_right
                                        if sequence[x+len(playersequence)+1] == "←":
                                            color ac_left
                                    if colorcoded == 2:
                                        if sequence[x+len(playersequence)+1] == "↑":
                                            color ac_up
                                        if sequence[x+len(playersequence)+1] == "↓":
                                            color ac_down

                    # if greentrail == False:
                    text playersequence:
                        # xalign 0.5
                        bold True
                        size 40

                text "Lives [strikes]" xalign 0.5
                hbox:
                    xalign 0.5
                    spacing 20
                    for i in range (strikes):
                        text "❤"


                # text "Coins: [coins]" xalign 0.5
                # text "Highest cleared level: [highestlevel]" xalign 0.5

                frame:
                    xalign 0.5
                    textbutton "END":
                        action [SetVariable("strikes",0), Play("audio",audio.button)]

                ## CONTROL
                if strikes == 0:
                    timer 0.1 action Function(playPuzzle)


            ## Timer is a renpy screen statement that executes an action once time elapses. In this case, it runs functions definited in the python blocks as part of init.
            timer 0.1 action Function(generatePuzzle)
            timer 0.1 action Function(puzzleTimer) repeat True

            # The key command 'inputs' a key when the game is running, hence it's inside the 'if playing_puzzle' block.

            ## ARROW KEYS
            key "K_UP" action Function(playerSequenceInput,"↑")
            key "K_DOWN" action Function(playerSequenceInput,"↓")
            key "K_LEFT" action Function(playerSequenceInput,"←")
            key "K_RIGHT" action Function(playerSequenceInput,"→")
            ## WASD
            key "w" action Function(playerSequenceInput,"↑")
            key "s" action Function(playerSequenceInput,"↓")
            key "a" action Function(playerSequenceInput,"←")
            key "d" action Function(playerSequenceInput,"→")
            ## GAMEPAD DPAD
            key "pad_dpup_press" action Function(playerSequenceInput,"↑")
            key "pad_dpdown_press" action Function(playerSequenceInput,"↓")
            key "pad_dpleft_press" action Function(playerSequenceInput,"←")
            key "pad_dpright_press" action Function(playerSequenceInput,"→")
            ## GAMEPAD FACEBTNS
            key "pad_y_press" action Function(playerSequenceInput,"↑")
            key "pad_a_press" action Function(playerSequenceInput,"↓")
            key "pad_x_press" action Function(playerSequenceInput,"←")
            key "pad_b_press" action Function(playerSequenceInput,"→")

        ## GAME MAIN MENU
        if playing_puzzle == False:

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 20

                text "Play with Arrows, WASD, gamepad, or touch screen." xalign 0.5 size 35 xsize 600 justify True

                frame:
                    xalign 0.5
                    textbutton "Play":
                        action Function(playPuzzle)

                if puzzlescorefinal > 0:
                    text "Coins Gained: [puzzlescorefinal]" xalign 0.5 size 35

                
            vbox:
                xalign 0.5
                yalign 1.0
                text "{b}Coins{/b}: [coins]" xalign 0.5 size 35
                text "Highest cleared level: [highestlevel]" xalign 0.5 size 35

                text "Lifetime Coins: [coinslifetime]" xalign 0.5 size 30

    ### UPGRADE SCREEN
    if playing_puzzle == False:
        frame:
            xsize 850
            # ysize 1000
            yfill True
            xalign 1.0
            yalign 0.5


            vbox:
                spacing 20
                xalign 0.5
                ypos 20
                xmaximum 800

                label "Accessibility Options" text_size 35 text_bold True
                
                ## HIT TRAIL
                hbox:
                    spacing 50
                    text "{b}Hit Trail{/b}" yalign 0.5 size 35
                    frame:
                        xsize 180
                        if greentrail == False:
                            textbutton "Disabled":
                                text_size 35
                                action Function(ToggleGreenTrail)
                                xalign 0.5
                        if greentrail == True:
                            textbutton "Enabled":
                                text_size 35
                                action Function(ToggleGreenTrail)
                                xalign 0.5
                    if greentrail == True:
                        text "{color=[greentrailcolor]}←↑{/color}↓→"  yalign 0.5 bold True size 35
                    if greentrail == False:
                        text "←↑↓→" yalign 0.5 bold True size 35

                ## NO FAIL MODE
                hbox:
                    spacing 50
                    text "{b}No Fail Mode{/b}" yalign 0.5 size 35
                    frame:
                        xsize 180
                        xalign 0.5
                        yalign 0.5
                        if nofailmode == False:
                            textbutton "Disabled":
                                action Function(ToggleNoFail)
                                text_size 35
                                xalign 0.5
                        if nofailmode == True:
                            textbutton "Enabled":
                                action Function(ToggleNoFail)
                                text_size 35
                                xalign 0.5
                    if nofailmode == True:
                        text "Keep sequence on mistake" yalign 0.5 size 35
                    if nofailmode == False:
                        text "Clear sequence on mistake" yalign 0.5 size 35

                ## COLOR CODED MODE
                hbox:
                    spacing 50
                    text "{b}Color Coded Arrows{/b}" yalign 0.5 size 35
                    frame:
                        xsize 160
                        ysize 60
                        textbutton "Mode [colorcoded]":
                        # if colorcoded == 0:
                        #     text "Mode 0" xalign 0.5 yalign 0.5 size 35
                        
                        # button:
                            action Function(ToggleColorCoded)
                            text_size 35
                            xalign 0.5

                    if colorcoded == 0:
                        text "←↑↓→" yalign 0.5 bold True size 35
                    if colorcoded == 1:
                        text "{color=[ac_left]}←{/color}↑↓{color=[ac_right]}→{/color}" yalign 0.5 bold True size 35
                    if colorcoded == 2:
                        text "{color=[ac_left]}←{/color}{color=[ac_up]}↑{/color}{color=[ac_down]}↓{/color}{color=[ac_right]}→{/color}" yalign 0.5 bold True size 35

                ### UPGRADES
                # if coinslifetime >= 50:
                label "Upgrades Menu" text_size 35 text_bold True

                hbox:
                    spacing 50
                    ## TITLES
                    vbox:
                        spacing 40
                        ypos 20
                        xalign 0.0
                        
                        text "{b}Max Difficulty{/b}: [diffmax]" yalign 0.5 size 35
                        # if coinslifetime >= 100:
                        text "{b}Time Limit{/b}: [puzzletimelimitmax:.2f]" yalign 0.5 size 35
                        # if coinslifetime >= 1500:
                        text "{b}Max Lives{/b}: [strikesmax]" yalign 0.5 size 35

                    ## BUTTONS
                    vbox:
                        spacing 20
                        xalign 0.6
                        frame:
                            xalign 0.5
                            textbutton "+ 1":
                                text_size 35
                                if coins >= diffcost:
                                    action Function(upgradeDiff)
                        
                        # if coinslifetime >= 100:
                        frame:
                            xalign 0.5
                            textbutton "+ 0.1":
                                text_size 35
                                if coins >= puzzletimecost:
                                    action Function(upgradeTime)
                        # if coinslifetime >= 1500:
                        frame:
                            xalign 0.5
                            textbutton "+ 1":
                                text_size 35
                                if coins >= strikescost:
                                    action Function(upgradeLives)


                    ## COST / COIN
                    vbox:
                        spacing 40
                        ypos 20
                        xalign 1.0

                        text "[diffcost] coins" yalign 0.5 size 35
                        # if coinslifetime >= 100:
                        text "[puzzletimecost] coins" yalign 0.5 size 35
                        # if coinslifetime >= 1500:
                        text "[strikescost] coins" yalign 0.5 size 35

                ### DIFFICULTY SETTINGS
                if diffmax > 1:
                    hbox:
                        spacing 20
                        label "Difficulty:" text_size 35 text_bold True
                        # text "[diffmultiplier:.1f]"

                    # text "Click and drag to adjust" size 20 xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing 20
                        frame:
                            textbutton "MIN" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,"min")
                        frame:
                            textbutton "-1.0" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,-10)
                        
                        frame:
                            textbutton "-0.5" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,-5)



                        text "[diffmultiplier:.1f]" yalign 0.5 size 35

                        frame:
                            textbutton "+0.5" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,+5)

                        frame:
                            textbutton "+1.0" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,+10)
                        frame:
                            textbutton "MAX" xalign 0.5 yalign 0.5:
                                text_size 35
                                action Function(AdjustDiff,"max")

                    text "Coins Multiplier: [1*(diffmultiplier):.2f]x":
                        size 35
                    text "Time Limit: [(puzzletimelimit):.2f] seconds":
                        size 35
                        if puzzletimelimit <= 0:
                            color "#F77"

                    null height 10

    # ▲►▼◄
    # ←↑↓→
    # ⮘⮙⮛⮚

    ### CONTROLS
    if playing_puzzle == True:
        frame: ### UP
            xalign 0.8
            yalign 0.2
            xysize (250,250)
            # if colorcoded == 2:
            #     background ac_up

            text "↑" size 250 xalign 0.5 yalign 0.5:
                if colorcoded == 2:
                    color ac_up

            button action Function(playerSequenceInput,"↑")

        frame: ### DOWN
            xalign 0.8
            yalign 0.8
            xysize (250,250)
            # if colorcoded == 2:
            #     background ac_down

            text "↓" size 250 xalign 0.5 yalign 0.5:
                if colorcoded == 2:
                    color ac_down

            button action Function(playerSequenceInput,"↓")

        frame: ### LEFT
            xalign 0.65
            yalign 0.5
            xysize (250,250)
            # if colorcoded >= 1:
            #     background ac_left

            text "←" size 250 xalign 0.5 yalign 0.5:
                if colorcoded >= 1:
                    color ac_left

            button action Function(playerSequenceInput,"←")

        frame: ### RIGHT
            xalign 0.95
            yalign 0.5
            xysize (250,250)
            # if colorcoded >= 1:
            #     background ac_right

            text "→" size 250 xalign 0.5 yalign 0.5:
                if colorcoded >= 1:
                    color ac_right

            button action Function(playerSequenceInput,"→")


    #### MUSIC CONTROL
    if playing_puzzle == True:
        timer 0.05:
            action Play("music", (random.choice(puzzlemusic)), fadein=1,fadeout=1,relative_volume=0.5)
        # $ renpy.play(puzzlemusic1, channel="music", fadein=1, fadeout=1, relative_volume=0.8)
    else:
        # $ renpy.music.stop(channel="music",fadeout=2)
        timer 0.05:
            action Stop("music", fadeout=2)



#### END