
image bg fundo = "#605448"


label start:

    scene bg fundo

    show screen timer

    # This calls the "choose game" screen and also stops renpy script from running, since we are "calling" a screen, instead of just "showing"
    call screen chooseGame

    return