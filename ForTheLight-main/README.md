# For The Light - Text Adventure Game

A Python-based text adventure game set in "The Final Alignment" universe with five planets.

## Recent Updates (July 30, 2025)

### Fixed Logic Issues in `tester.py`

**Critical Fixes:**
- Fixed assignment bug: Changed `==` to `=` for player location updates
- Improved menu system with proper looping functionality
- Enhanced game flow with continuous room interactions
- Fixed undefined variable issues (`street_choice1`, `street_choice2`)
- Added proper error handling and input validation

**Enhancements:**
- Added main game loop for seamless gameplay
- Improved currency system with feedback messages
- Better room transition handling
- Added debug output for location tracking
- Enhanced user experience with clearer prompts

**Technical Improvements:**
- Proper return values from `start_room()` function
- Fixed indentation and syntax errors
- Removed duplicate/broken conditional statements
- Added null checks for movement validation

## Game Features

- Interactive text-based adventure
- Colorized output using `colorama`
- Multiple planets and locations to explore
- Currency collection system
- Player progress tracking
- Movement system (W/A/S/D controls)

## How to Run

```bash
python tester.py
```

## Dependencies

- `colorama` - For colored terminal output
