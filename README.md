# Monopoly - Online Edition 🎲

A fully featured Monopoly game implementation in Python with online multiplayer support, beautiful Pygame graphics, and realistic game mechanics.

## Features

- ✅ **Complete Monopoly Rules**: Full game implementation including properties, rent, mortgaging, and house/hotel trading
- 🌐 **Online Multiplayer**: Play with friends on different machines using socket-based networking
- 🎨 **Beautiful Graphics**: Pygame-based GUI with smooth animations and visual effects
- 🏗️ **Object-Oriented Design**: Clean, maintainable architecture using OOP principles
- 💾 **Game State Management**: Proper turn management, player tracking, and game flow
- 🎴 **Chance & Community Chest Cards**: Full card deck implementation
- 🚂 **All Property Types**: Streets, railroads, utilities with proper rent calculations
- 📊 **Player Statistics**: Track money, properties, and game status

## Project Structure

```
game/
├── core/                    # Core game logic
│   ├── __init__.py
│   ├── game.py             # Main game controller
│   ├── player.py           # Player class
│   ├── board.py            # Board and spaces
│   ├── property.py         # Property management
│   ├── dice.py             # Dice roller
│   ├── card.py             # Chance/Community Chest cards
│   └── utils.py            # Utility functions
├── server/                  # Server for multiplayer
│   ├── __init__.py
│   └── monopoly_server.py  # Game server
├── client/                  # Client GUI
│   ├── __init__.py
│   ├── game_client.py      # Network client
│   └── game_ui.py          # Pygame UI
├── config.py               # Configuration
├── requirements.txt        # Python dependencies
├── README.md               # This file
└── assets/                 # Game assets (images, sounds)
```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone or download the game:
```bash
cd game
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python -c "import pygame; print('Pygame installed successfully')"
```

## Quick Start

### Option 1: Single Machine (Demo Mode)

To test the game on a single machine:

```bash
# Terminal 1 - Start server with 2 players
python server/monopoly_server.py 2

# Terminal 2 - Start first client
python client/game_ui.py localhost 5000 "Player 1"

# Terminal 3 - Start second client
python client/game_ui.py localhost 5000 "Player 2"
```

### Option 2: Network Play (Multiple Machines)

**Machine 1 (Server):**
```bash
python server/monopoly_server.py 2
```

**Machine 2 (Client 1):**
```bash
python client/game_ui.py <SERVER_IP> 5000 "Player 1"
```

**Machine 3 (Client 2):**
```bash
python client/game_ui.py <SERVER_IP> 5000 "Player 2"
```

Replace `<SERVER_IP>` with the actual IP address of the server machine.

## Game Controls

### Keyboard Shortcuts
- **SPACE**: Roll dice
- **E**: End your turn
- **ESC**: Exit game
- **MOUSE**: Click on board to interact with properties

### Buttons in UI
- **Roll Dice**: Roll the dice to move
- **End Turn**: End your current turn
- **Buy Property**: Purchase the property you landed on (if available)

## Game Rules

### Objective
Become the wealthiest player by buying, renting, and trading properties.

### Basic Gameplay

1. **Rolling Dice**: Each turn, roll two dice to move around the board
2. **Landing on Spaces**:
   - **Unowned Property**: You can purchase it
   - **Owned by Another Player**: Pay rent
   - **Owned by You**: No action
   - **Special Spaces**: GO, Free Parking, Go to Jail, Income Tax, Luxury Tax

3. **Properties**:
   - Purchase unowned properties
   - Build houses and hotels on complete color sets
   - Collect rent from other players

4. **Jail**:
   - Landed on "Go to Jail" or drew jail card
   - Roll doubles to escape or pay bail

5. **Bankruptcy**: 
   - If you can't pay debt, you're out of the game
   - Last player remaining wins!

### Property Values
- **Streets**: Vary from $60 (Mediterranean) to $400 (Boardwalk)
- **Railroads**: $200 each
- **Utilities**: $150 each
- **Houses**: 50% of property cost
- **Hotels**: 50% of property cost

## Architecture

### Core Components

#### Game.py
Main game controller handling:
- Player turns and phases
- Dice rolling and movement
- Property purchases and rent
- Game state management

#### Player.py
Player management:
- Money tracking
- Property ownership
- Jail status
- Bankruptcy management

#### Board.py
Board management:
- All 40 board spaces
- Card decks (Chance and Community Chest)
- Property information

#### Network Components

**Server (monopoly_server.py)**:
- Manages game instances
- Handles multiple client connections
- Broadcasts game state updates
- Validates moves and enforces rules

**Client (game_client.py)**:
- Connects to game server
- Sends player actions
- Receives game state updates
- Manages message queue

**GUI (game_ui.py)**:
- Pygame-based interface
- Renders board and player positions
- Shows player information
- Handles user input
- Displays animations

## OOP Design Patterns

### Classes Overview

**Player**
```python
class Player:
    - Money management
    - Property ownership
    - Position tracking
    - Jail management
```

**Property**
```python
class Property:
    - Purchase and mortgage
    - Rent calculation
    - House/Hotel management
    - Color grouping
```

**Board**
```python
class Board:
    - Space management
    - Card decks
    - Property lookup
```

**MonopolyGame**
```python
class MonopolyGame:
    - Game flow control
    - Turn management
    - State synchronization
    - Rule enforcement
```

## Multiplayer Features

### Server-Client Architecture
- **Socket-based communication**: TCP sockets for reliable message delivery
- **JSON protocol**: Platform-independent message format
- **Real-time updates**: Broadcast game state to all clients
- **Message validation**: Verify legitimate player actions

### Game Synchronization
- Server maintains authoritative game state
- Clients display state and send actions
- No client-side game logic (prevents cheating)
- State updates via broadcast messages

## Building Your Own Features

### Adding New Properties
Edit `board.py` and modify the `_initialize_board()` method:
```python
(position, "Name", PropertyType.STREET, cost)
```

### Adding Sound Effects
1. Place audio files in `assets/sounds/`
2. Use pygame.mixer in `game_ui.py`:
```python
pygame.mixer.init()
sound = pygame.mixer.Sound("assets/sounds/diceroll.wav")
sound.play()
```

### Customizing Colors
Modify `Colors` class in `game_ui.py` or config.py:
```python
class Colors:
    CUSTOM_COLOR = (R, G, B)
```

## Troubleshooting

### "Connection refused" error
- Ensure server is running on the correct IP and port
- Check firewall settings
- Verify network connectivity between machines

### Pygame not found
```bash
pip install --upgrade pygame
```

### Game runs slowly
- Close other applications
- Check screen resolution settings
- Ensure 60 FPS is maintained (visible in debug logs)

### Players stuck or desynced
- Restart affected clients
- Check network latency with: `ping <server_ip>`

## Performance Considerations

- **Board rendering**: Efficient square-based rendering
- **Animation**: Smooth 60 FPS updates
- **Network**: Minimal message passing with delta updates
- **Memory**: Lightweight game state representation

## Future Enhancements

- [ ] Player profiles and statistics tracking
- [ ] Replay and game recording
- [ ] Mobile app version
- [ ] AI opponents
- [ ] Custom board themes
- [ ] Sound effects and music
- [ ] Trading UI improvements
- [ ] Tournament mode
- [ ] Chat functionality
- [ ] Save/Load game states

## License

This project is provided as-is for educational purposes.

## Contributing

Feel free to fork, modify, and improve this implementation!

## Support

For issues or questions, please refer to the code comments and docstrings throughout the project.

## Author

Created with ❤️ for Monopoly enthusiasts

---

**Enjoy the game!** 🎉
