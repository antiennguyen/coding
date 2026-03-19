"""
API Documentation for Monopoly Game

This file documents all classes, methods, and networking protocols.
"""

# ============================================================================
# CORE GAME CLASSES
# ============================================================================

"""
Module: core/game.py
====================

class MonopolyGame:
    '''Main game controller for Monopoly
    
    Attributes:
        players: List[Player] - All game players
        board: Board - Game board instance
        dice: Dice - Dice roller
        current_player_index: int - Index of current player
        game_state: GameState - Current game state
        turn_count: int - Number of turns played
    
    Methods:
        __init__(player_names: List[str], player_colors: List[str])
            Create new game with specified players
        
        start_game()
            Initialize and start the game
        
        roll_dice() -> Tuple[int, int]
            Roll two dice, return (die1, die2)
        
        move_current_player() -> Tuple[bool, int]
            Move current player based on dice roll
            Returns (passed_go, new_position)
        
        land_on_space() -> str
            Handle landing on a board space
            Returns action type: "available_for_purchase", "owned_by_other", etc.
        
        purchase_property(player_id: int, property_id: int) -> bool
            Attempt to purchase a property
        
        pay_rent(amount: int)
            Transfer rent from current player to property owner
        
        next_turn()
            Move to next player's turn
        
        check_game_over() -> Optional[Player]
            Check if game has ended, return winner if so
        
        get_game_state_dict() -> dict
            Serialize game state for transmission
    
    Example:
        game = MonopolyGame(["Alice", "Bob"])
        game.start_game()
        current_player = game.get_current_player()
'''

class GamePhase(Enum):
    '''Phases of a player's turn'''
    ROLL = "roll"      # Player must roll dice
    MOVE = "move"      # Player is moving
    LAND = "land"      # Player landed on space
    BUY = "buy"        # Player can buy property
    TRADE = "trade"    # Player can trade
    END = "end"        # End of turn

class GameState(Enum):
    '''Overall game state'''
    SETUP = "setup"        # Waiting for players
    PLAYING = "playing"    # Game in progress
    PAUSED = "paused"      # Game paused
    FINISHED = "finished"  # Game completed
"""

"""
Module: core/player.py
======================

class Player:
    '''Represents a Monopoly player
    
    Attributes:
        player_id: int - Unique player ID
        name: str - Player name
        color: str - Player color
        money: int - Current money
        position: int - Current board position (0-39)
        status: PlayerStatus - Current status
        in_jail: bool - Whether in jail
        owned_properties: List[int] - Property IDs owned
    
    Methods:
        add_money(amount: int)
            Add money to player
        
        remove_money(amount: int) -> bool
            Remove money, return True if successful
        
        move_to_position(new_position: int) -> bool
            Move to new position, return True if passed GO
        
        go_to_jail()
            Send player to jail
        
        release_from_jail()
            Release player from jail
        
        add_property(property_id: int)
            Add owned property
        
        declare_bankruptcy()
            Player is bankrupt and out of game
    
    Example:
        player = Player(0, "Alice", "red")
        player.add_money(100)
        player.move_to_position(25)
'''

class PlayerStatus(Enum):
    '''Player game status'''
    PLAYING = "playing"
    IN_JAIL = "in_jail"
    BANKRUPT = "bankrupt"
    SPECTATOR = "spectator"
"""

"""
Module: core/property.py
=========================

class Property:
    '''Represents a board property
    
    Attributes:
        name: str - Property name
        position: int - Position on board
        property_type: PropertyType - Type of property
        purchase_price: int - Cost to buy
        owner: Optional[int] - Player ID of owner
        house_count: int - Number of houses (0-4)
        has_hotel: bool - Whether has hotel
    
    Methods:
        is_available() -> bool
            Check if property can be purchased
        
        set_owner(player_id: int)
            Set property owner
        
        mortgage() -> int
            Mortgage property, return mortgage value
        
        unmortgage() -> int
            Unmortgage property, return cost
        
        add_house() -> bool
            Add house to property
        
        add_hotel() -> bool
            Add hotel to property
        
        get_rent(dice_roll: int = 0, ...) -> int
            Calculate rent for property
    
    Example:
        prop = board.get_space(6)
        if prop.is_available():
            game.purchase_property(0, 6)
'''

class PropertyType(Enum):
    '''Types of properties'''
    STREET = "street"
    RAILROAD = "railroad"
    UTILITY = "utility"
    SPECIAL = "special"
"""

"""
Module: core/board.py
======================

class Board:
    '''Monopoly game board
    
    Attributes:
        spaces: List[Property] - All 40 board spaces
        chance_deck: CardDeck - Chance cards
        community_chest_deck: CardDeck - Community Chest cards
    
    Methods:
        get_space(position: int) -> Property
            Get property at position
        
        get_property_by_name(name: str) -> Property
            Get property by name
        
        get_next_railroad(current_position: int) -> int
            Get next railroad position from current
        
        get_next_utility(current_position: int) -> int
            Get next utility position from current
    
    Example:
        space = board.get_space(0)
        print(space.name)  # "GO"
'''

class CardDeck:
    '''Deck of Chance or Community Chest cards
    
    Methods:
        draw_card() -> Card
            Draw a random card from deck
        
        return_card(card: Card)
            Return card to discard pile
    
    Example:
        card = board.chance_deck.draw_card()
        print(card.description)
'''
"""

"""
Module: core/dice.py
====================

class Dice:
    '''Dice roller for Monopoly
    
    Attributes:
        last_roll: Tuple[int, int] - Result of last roll
        doubles_count: int - Number of consecutive doubles
    
    Methods:
        roll() -> Tuple[int, int]
            Roll two dice, return results
        
        get_total() -> int
            Get sum of last roll
        
        is_doubles() -> bool
            Check if last roll was doubles
        
        reset_doubles()
            Reset doubles counter
    
    Example:
        dice = Dice()
        d1, d2 = dice.roll()
        total = dice.get_total()
'''
"""

# ============================================================================
# NETWORKING PROTOCOL
# ============================================================================

"""
MESSAGE PROTOCOL
================

All messages are JSON formatted and transmitted over TCP sockets.

1. CONNECTION PHASE
-------------------

Client -> Server:
{
    "type": "connect",
    "player_name": "Alice",
    "color": "red"
}

Server -> Client:
{
    "type": "player_state",
    "player_id": 0,
    "player_name": "Alice",
    "message": "Alice joined the game"
}

2. GAME PLAY PHASE
------------------

Client -> Server:
{
    "type": "roll_dice"
}

Server -> All Clients:
{
    "type": "roll_dice",
    "dice": [3, 4],
    "player_id": 0
}

3. PROPERTY PURCHASE
--------------------

Client -> Server:
{
    "type": "buy_property",
    "property_id": 6
}

Server -> All Clients:
{
    "type": "buy_property",
    "player_id": 0,
    "property_id": 6,
    "message": "Player purchased property"
}

4. TURN MANAGEMENT
------------------

Client -> Server:
{
    "type": "end_turn"
}

Server -> All Clients:
{
    "type": "game_state",
    "state": {...}  # Full game state
}

5. ERROR HANDLING
-----------------

Server -> Client:
{
    "type": "error",
    "error": "It's not your turn!"
}

6. CHAT
-------

Client -> Server:
{
    "type": "chat",
    "message": "Nice move!"
}

Server -> All Clients:
{
    "type": "chat",
    "player_name": "Alice",
    "message": "Nice move!",
    "timestamp": 1234567890.0
}

MESSAGE TYPES
=============
- connect: Player connection request
- disconnect: Player disconnection
- roll_dice: Dice roll request
- move: Player movement
- buy_property: Property purchase request
- sell_property: Property sale
- mortgage_property: Property mortgage
- end_turn: Turn completion
- game_state: Full game state update
- player_state: Player status update
- action_required: Prompt for player action
- error: Error message
- chat: Chat message
"""

# ============================================================================
# CLIENT API
# ============================================================================

"""
Module: client/game_client.py
==============================

class GameClient:
    '''Network client for Monopoly
    
    Attributes:
        host: str - Server hostname/IP
        port: int - Server port
        is_connected: bool - Connection status
        player_id: Optional[int] - Client's player ID
        player_name: str - Client's player name
    
    Methods:
        connect(host: str = None, port: int = None, 
               player_name: str = "Player") -> bool
            Connect to game server
        
        disconnect()
            Disconnect from server
        
        send_message(message: Dict) -> bool
            Send message to server
        
        register_handler(message_type: str, handler: Callable)
            Register callback for message type
        
        roll_dice() -> bool
            Request dice roll
        
        buy_property(property_id: int) -> bool
            Request property purchase
        
        end_turn() -> bool
            Request turn end
        
        send_chat(message: str) -> bool
            Send chat message
        
        get_messages() -> List[Dict]
            Get pending messages from queue
    
    Example:
        client = GameClient("localhost", 5000)
        client.connect(player_name="Alice")
        client.register_handler("game_state", on_game_state)
        client.roll_dice()
"""

# ============================================================================
# UI CLASSES
# ============================================================================

"""
Module: client/game_ui.py
==========================

class GameUI:
    '''Pygame-based game interface
    
    Attributes:
        client: GameClient - Network client instance
        screen: pygame.Surface - Display surface
        game_state: dict - Current game state
        animations: List[Animation] - Active animations
    
    Methods:
        run()
            Main game loop
        
        _handle_events()
            Process pygame events
        
        _update()
            Update game logic and animations
        
        _draw()
            Render game to screen
        
        _draw_board()
            Render game board
        
        _draw_players()
            Render player pieces
        
        _draw_sidebar()
            Render player information sidebar
    
    Example:
        client = GameClient()
        ui = GameUI(client)
        ui.run()
'''

class Animation:
    '''Base class for animations
    
    Methods:
        update() -> bool
            Update animation, return True if finished
        
        draw(surface)
            Render animation
    
    Example:
        anim = DiceRollAnimation(100, 100)
        while not anim.update():
            anim.draw(screen)
'''
"""

# ============================================================================
# SERVER CLASSES
# ============================================================================

"""
Module: server/monopoly_server.py
==================================

class MonopolyGameServer:
    '''Main game server
    
    Attributes:
        host: str - Server bind address
        port: int - Server port
        game: MonopolyGame - Game instance
        connected_players: Dict[int, ClientHandler] - Connected clients
    
    Methods:
        start()
            Start the server and accept connections
        
        broadcast(message: Dict)
            Send message to all connected clients
        
        is_turn_of_player(player_id: int) -> bool
            Check if it's specified player's turn
        
        stop()
            Shutdown server
    
    Example:
        server = MonopolyGameServer("0.0.0.0", 5000, num_players=2)
        server.start()
'''

class ClientHandler(threading.Thread):
    '''Handles communication with one client
    
    Methods:
        run()
            Main client handling loop
        
        send_message(message: Dict)
            Send message to this client
    '''
"""

# ============================================================================
# UTILITY CLASSES
# ============================================================================

"""
Module: core/utils.py
======================

class GameSerializer:
    @staticmethod
    to_json(obj: Any) -> str
    @staticmethod
    from_json(json_str: str) -> Any

class GameLogger:
    def log(level: str, message: str)
    def info(message: str)
    def error(message: str)
    def warning(message: str)
    def debug(message: str)

class GameConfig:
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5000
    MAX_PLAYERS = 6
    STARTING_MONEY = 1500
    ...
"""

print("API Documentation loaded. See source files for detailed docstrings.")
