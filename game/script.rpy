

define k = Character("Keiji", color="#035a19")
define r = Character("Rin", color="#ff4d4d")


# Formula  -> Theory / Redacted -> Proof 

label start:


    # These display lines of dialogue.
    play music "funkyloopable.ogg" fadein 0.5

    scene black with fade
    k "Is this screen black?"

    menu:
        "Yes":
            k "I see. Then this scene will continue as it should. Continue as you were."
        "No":
            k "It looks black to me. Perhaps you are mistaken. Blind perhaps. What do you think, Tohsaka?"
            r "...you really are an idiot."    

    # This ends the game.

    return
