

define k = Character("Keiji", color="#035a19")
define r = Character("Rin", color="#ff4d4d")
define prof = Character("Teacher")




# Formula  -> Theory / Redacted -> Proof 

label start:

    scene black with fade
    "FATE / CONDUCTION"

label Homurahara1_test:
    
    play music "music/funkyloopable.ogg" fadein 1.0

    k "Hello."

    "I bow as I was told by my Handler. A common gesture in Eastern regions."

    k "My name is Yukimura Keiji. It is nice to meet you all."

    "I rise."

    k "Please take care of me as I acclimate to this new enviorment."
    prof "Yukimura-san. There is no need to be so formal. Tohsaka, will you aid the new student..."

    "Unneccesary information. Focus on the mission."

    k "I look out at the sea of students and instantly, my eyes land on a student in the back. Blue hair. Blue eyes. Just as the description called for."

    "40 percent Chance of Correct Identification of Mission."

    prof "Did you hear everything? Please take a seat whereever you'd like."

    k "Understood. Thank you for the assistance, ma'am."

    k "I bow once more."

    menu: 
        "Sit in the front.":
            "I take a seat near the front next to a girl with black hair. blue eyes. Not ideal for the mission, but it keeps my cover low."
            $ ATLAS_ALIGNMENT += 10
        "Sit in the back.":
            $ ATLAS_ALIGNMENT += 5
            "I take a seat at the back near the person who looks similar to the report."
            "I will continue to monitor him from here."
    
    "Switching to Redacted..."
    jump Redacted1_test


label Redacted1_test:

    play music "music/pressure.ogg" fadein 1.5

    k "Agk...!"

    k "The Berserker Class Servants Noble Phantasm cuts through me with ease."

    r "Keiji!"

    "I do not get the chance to respond. I do not know how I would respond."
   
    "But there..."

    "There is something I would to her."

    "But the world turns to black before I could..."

    "Bad End : Death"

menu: 
    "Start Over?":
        jump Proof1_test
    "End the timeline here.":
        k "..."

label Proof1_test:

    k "Proof is not in development yet..."
    k "Goodbye."

    return
