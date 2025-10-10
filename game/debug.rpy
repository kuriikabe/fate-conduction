label debug:
    scene black with fade 
    k "Debug Room Initialzed."

    menu:
        "Choose a test action:"
        "Check variables":
            jump debug_variables
        "Modify variables":
            jump debug_modify
        "Jump to route":
            jump debug_jump
        "Return to main menu":
            return

    label debug_variables:
    scene black
    with dissolve
    "AFF_RIN: [AFF_RIN]\nALIGN_ATLAS: [ALIGN_ATLAS]\nCIRCUIT_STRAIN: [CIRCUIT_STRAIN]\nREDACTED_UNLOCK: [REDACTED_UNLOCK]\nPROOF_UNLOCK: [PROOF_UNLOCK]"
    menu:
        "Back":
            jump debug

label debug_modify:
    scene black
    "Adjust key variables:"
    menu:
        "Increase Rin Affection (+10)":
            $ AFF_RIN += 10
            jump debug_modify
        "Decrease Rin Affection (-10)":
            $ AFF_RIN -= 10
            jump debug_modify
        "Increase Atlas Alignment (+10)":
            $ ALIGN_ATLAS += 10
            jump debug_modify
        "Increase Circuit Strain (+10)":
            $ CIRCUIT_STRAIN += 10
            jump debug_modify
        "Reset all values":
            $ AFF_RIN = 0
            $ ALIGN_ATLAS = 50
            $ CIRCUIT_STRAIN = 0
            jump debug_modify
        "Back":
            jump debug

label debug_jump:
    scene black
    "Jump to a section:"
    menu:
        "Formula (Homurahara intro)":
            jump formula_1
        "Theory (early War)":
            jump theory_1
        "Redacted (death loop)":
            jump redacted_entry
        "Proof (true end)":
            jump proof_start
        "Back":
            jump debug

define config.developer = True

define config.developer = True

init python:
    # Define the function
    def open_debug(*args, **kwargs):
        renpy.jump_in_new_context("debug")

    # Bind Alt+T to open Debug Room
    config.keymap['debug'] = ['alt_K_t']

    # Tell Ren'Py to call the function when the key is pressed
    config.underlay.append(renpy.Keymap(debug=open_debug))
