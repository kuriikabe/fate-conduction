# Copilot Instructions for Fate/Conduction

## Project Overview

Fate/Conduction is a visual novel project built with Ren'Py, set in an alternate Fate/stay night continuity. The story follows Keiji Yukimura, a magus from Atlas, through the Fifth Holy Grail War across four interconnected routes: FORMULA, THEORY, REDACTED, and PROOF.

## Technology Stack

- **Framework**: Ren'Py (visual novel engine)
- **Languages**: 
  - Ren'Py script language (`.rpy` files)
  - Python (embedded in Ren'Py for advanced logic)
- **Assets**: Images, audio, and translations stored in appropriate directories

## Project Structure

```
fate-conduction/
├── game/                    # Main game directory
│   ├── script.rpy          # Main story script and character definitions
│   ├── options.rpy         # Game configuration and build options
│   ├── gui.rpy             # GUI layout and styling definitions
│   ├── screens.rpy         # UI screens (menus, dialogs, etc.)
│   ├── gui/                # GUI assets (images, fonts)
│   ├── tl/                 # Translations
│   └── cache/              # Compiled bytecode (do not edit)
└── README.md               # Project documentation
```

## Coding Standards

### Ren'Py Script Files (.rpy)

1. **Comments**: Use `#` for single-line comments, `##` for documentation headers
2. **Indentation**: Use 4 spaces for indentation (Ren'Py standard)
3. **Character Definitions**: Define characters with `define` keyword
   ```renpy
   define character_name = Character("Display Name", color="#hexcolor")
   ```
4. **Labels**: Use descriptive lowercase names with underscores
   ```renpy
   label route_formula_chapter_1:
   ```
5. **Variables**: Use meaningful names following Python conventions
   - Stats: `CIRCUIT_STRAIN`, `ALIGN_ATLAS`, `AFF_RIN`
   - Flags: `route_formula_complete`, `keiji_trust_level`

### Python Code in Ren'Py

1. Follow PEP 8 style guidelines where applicable
2. Use `init python:` blocks for initialization code
3. Use `python:` blocks for runtime logic within labels

### GUI and Styling

1. GUI configuration lives in `gui.rpy`
2. Use `define gui.*` for GUI properties
3. Maintain consistent spacing and alignment values
4. Custom screens go in `screens.rpy`

## Domain-Specific Knowledge

### Visual Novel Terminology

- **Label**: A named story segment that can be jumped to
- **Scene**: Command to set background image
- **Show/Hide**: Commands to display/remove character sprites
- **Menu**: Present choices to the player
- **Jump**: Navigate to different story labels
- **Call**: Execute a label and return afterward

### Project-Specific Mechanics

1. **Route System**: Four progressive routes (FORMULA → THEORY → REDACTED → PROOF)
2. **Stats**:
   - `CIRCUIT_STRAIN`: Represents Keiji's mental/magical stress
   - `ALIGN_ATLAS`: Alignment toward Atlas methodology
   - `AFF_*`: Affinity with specific characters (e.g., `AFF_RIN`)
3. **Codex System**: Unlockable lore entries and archives
4. **Atlas Theme**: UI styled after operational readouts from the Atlas Institute

### Fate Universe Context

- Atlas Institute: One of three branches of the Mage's Association, focuses on prediction and computational magecraft
- Holy Grail War: Battle royale between mages and their summoned Servants
- Homurahara Academy: School setting from Fate/stay night
- Magecraft vs. Magic: Magecraft is reproducible supernatural phenomena; True Magic is impossible miracles

## Development Guidelines

### When Adding New Content

1. **New Routes/Chapters**: Create new labels in `script.rpy` or separate `.rpy` files in `game/`
2. **New Characters**: Define in `script.rpy` with appropriate display names and colors
3. **New Choices**: Use Ren'Py's `menu:` construct with clear option text
4. **Stat Changes**: Document changes clearly in comments
5. **Assets**: Place in appropriate subdirectories (`game/images/`, `game/audio/`)

### Configuration Changes

1. **Game Settings**: Modify `options.rpy`
2. **Visual Styling**: Modify `gui.rpy`
3. **UI Screens**: Modify `screens.rpy`
4. **Build Configuration**: Adjust `build.*` properties in `options.rpy`

### Best Practices

1. **Readability**: Keep story text clear and properly formatted
2. **Comments**: Document complex branching logic and stat calculations
3. **Testing**: Test all story branches and stat interactions
4. **Consistency**: Maintain consistent naming for characters, variables, and labels
5. **Translation Ready**: Use `_()` wrapper for translatable strings
6. **Save Compatibility**: Be careful when changing variable names or types

### File Organization

1. Keep main story in `script.rpy` or split into logical files (e.g., `route_formula.rpy`)
2. Use subdirectories for organization (e.g., `game/routes/`, `game/systems/`)
3. Don't edit compiled `.rpyc` files - they're auto-generated
4. Keep cache and save directories out of version control

## Common Tasks

### Adding a New Character
```renpy
define keiji = Character("Keiji Yukimura", color="#4a90e2")
```

### Creating a Choice Point
```renpy
menu:
    "Trust the calculation.":
        $ CIRCUIT_STRAIN += 1
        $ ALIGN_ATLAS += 5
        jump trust_calculation
    
    "Follow instinct.":
        $ AFF_RIN += 5
        jump follow_instinct
```

### Adding a Stat Check
```renpy
if CIRCUIT_STRAIN > 50:
    "The mental strain becomes unbearable."
    jump mental_breakdown
else:
    "You maintain your composure."
```

### Creating a New Screen
```renpy
screen stat_overlay():
    frame:
        xalign 0.98
        yalign 0.02
        vbox:
            text "Circuit Strain: [CIRCUIT_STRAIN]"
            text "Atlas Alignment: [ALIGN_ATLAS]"
```

## Testing and Validation

1. Launch the game using Ren'Py launcher to test changes
2. Test all story branches and choices
3. Verify stat calculations are correct
4. Check for syntax errors in `.rpy` files
5. Test UI changes at different resolutions
6. Verify translations if working on localization

## Avoiding Common Mistakes

1. Don't modify `.rpyc` compiled files directly
2. Don't forget to define variables before using them
3. Use `$` prefix for Python statements in Ren'Py script context
4. Remember that Ren'Py uses indentation-based syntax like Python
5. Don't hardcode paths - use Ren'Py's asset management
6. Test save/load compatibility after changing variables

## References

- [Ren'Py Documentation](https://www.renpy.org/doc/html/)
- [Ren'Py Language Reference](https://www.renpy.org/doc/html/language_basics.html)
- [Ren'Py GUI Customization](https://www.renpy.org/doc/html/gui.html)
- Project README: `/README.md`
