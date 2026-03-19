"""
Example Usage of Monopoly Game

This file demonstrates how to use the game programmatically.
"""

# ============================================================================
# EXAMPLE 1: LOCAL GAME WITHOUT NETWORKING
# ============================================================================

def example_local_game():
    """Run a local game simulation without networking"""
    from core.game import MonopolyGame
    
    # Create a game with 2 players
    game = MonopolyGame(["Alice", "Bob"])
    print(f"Created game: {game}")
    
    # Start the game
    game.start_game()
    print(f"\nGame state: {game.game_state.value}")
    
    # Simulate first turn
    player = game.get_current_player()
    print(f"\n{player.name}'s turn")
    
    # Roll dice
    d1, d2 = game.roll_dice()
    print(f"Rolled: {d1} + {d2} = {d1+d2}")
    
    # Move player
    passed_go, new_pos = game.move_current_player()
    print(f"Moved to position {new_pos}")
    
    if passed_go:
        print("Passed GO! Collected $200")
    
    # Check space
    space = game.board.get_space(new_pos)
    print(f"Landed on: {space.name}")
    
    if space.is_available():
        print(f"Available for purchase: ${space.purchase_price}")
        game.purchase_property(player.player_id, new_pos)
        print(f"Purchased! {player.name} now owns {space.name}")


# ============================================================================
# EXAMPLE 2: NETWORK SERVER SETUP
# ============================================================================

def example_server_setup():
    """Example of setting up and running a game server"""
    from server.monopoly_server import MonopolyGameServer
    from core.utils import GameConfig
    
    # Create server for 2-4 players
    server = MonopolyGameServer(
        host="0.0.0.0",
        port=5000,
        num_players=2
    )
    
    print(f"Server created: {server}")
    print(f"Waiting for players on {server.host}:{server.port}")
    
    # In real usage, call server.start() to accept connections
    # server.start()


# ============================================================================
# EXAMPLE 3: NETWORK CLIENT SETUP
# ============================================================================

def example_client_setup():
    """Example of setting up a network client"""
    from client.game_client import GameClient
    
    # Create client
    client = GameClient("localhost", 5000)
    
    # Register message handlers
    def on_game_state(message):
        print(f"Game state updated!")
    
    def on_error(message):
        print(f"Error: {message['error']}")
    
    client.register_handler("game_state", on_game_state)
    client.register_handler("error", on_error)
    
    # Connect to server
    if client.connect(player_name="Alice"):
        print(f"Connected to server!")
        print(f"Your player ID: {client.player_id}")
        
        # Roll dice
        client.roll_dice()
        
        # In real usage, would continue game interaction
        # Messages would be received in separate thread
        
        # Disconnect when done
        client.disconnect()
    else:
        print("Failed to connect!")


# ============================================================================
# EXAMPLE 4: PROPERTY MANAGEMENT
# ============================================================================

def example_property_management():
    """Example of property management"""
    from core.board import Board
    from core.property import PropertyType
    
    board = Board()
    
    # Get a property
    space = board.get_space(6)  # Oriental Avenue
    print(f"Property: {space.name}")
    print(f"Cost: ${space.purchase_price}")
    print(f"Base Rent: ${space.rent_base}")
    
    # Set owner
    space.set_owner(0)  # Player 0 owns it
    print(f"Owner: Player {space.owner}")
    
    # Add houses
    for i in range(3):
        if space.add_house():
            print(f"Added house {i+1}")
    
    # Calculate rent
    print(f"Rent with {space.house_count} houses: ${space.get_rent()}")
    
    # Add hotel
    space.add_house()
    if space.add_hotel():
        print("Added hotel!")
        print(f"Rent with hotel: ${space.get_rent()}")


# ============================================================================
# EXAMPLE 5: PLAYER MANAGEMENT
# ============================================================================

def example_player_management():
    """Example of player management"""
    from core.player import Player
    
    # Create player
    player = Player(0, "Alice", "red")
    print(f"Created player: {player}")
    
    # Money management
    print(f"Starting money: ${player.money}")
    player.add_money(100)
    print(f"After adding $100: ${player.money}")
    
    player.remove_money(50)
    print(f"After removing $50: ${player.money}")
    
    # Movement
    player.move_to_position(25)
    print(f"Current position: {player.position}")
    
    # Jail management
    player.go_to_jail()
    print(f"In jail: {player.in_jail}")
    
    player.release_from_jail()
    print(f"Released from jail: {not player.in_jail}")
    
    # Get out of jail free
    player.add_jail_free_card()
    print(f"Get out of jail free cards: {player.jail_free_cards}")


# ============================================================================
# EXAMPLE 6: DICE ROLLING
# ============================================================================

def example_dice_rolling():
    """Example of dice rolling"""
    from core.dice import Dice
    
    dice = Dice()
    
    # Roll dice
    d1, d2 = dice.roll()
    print(f"Rolled: {d1}, {d2}")
    print(f"Total: {dice.get_total()}")
    print(f"Is doubles: {dice.is_doubles()}")
    
    # Check doubles tracking
    print(f"Doubles count: {dice.doubles_count}")
    
    # Roll multiple times
    print("\nRolling 5 times:")
    for i in range(5):
        result = dice.roll()
        print(f"  Roll {i+1}: {result[0]} + {result[1]} = {dice.get_total()} {('DOUBLES!' if dice.is_doubles() else '')}")


# ============================================================================
# EXAMPLE 7: CARD DRAWING
# ============================================================================

def example_card_drawing():
    """Example of drawing cards"""
    from core.board import Board
    
    board = Board()
    
    # Draw chance card
    print("Drawing Chance card:")
    card = board.chance_deck.draw_card()
    print(f"Card: {card.description}")
    print(f"Value: {card.value}")
    
    # Draw community chest card
    print("\nDrawing Community Chest card:")
    card = board.community_chest_deck.draw_card()
    print(f"Card: {card.description}")
    print(f"Value: {card.value}")
    
    # Draw multiple cards
    print("\nDrawing 3 Chance cards:")
    for i in range(3):
        card = board.chance_deck.draw_card()
        print(f"  {i+1}. {card.description[:50]}...")


# ============================================================================
# EXAMPLE 8: BOARD NAVIGATION
# ============================================================================

def example_board_navigation():
    """Example of navigating the board"""
    from core.board import Board
    
    board = Board()
    
    # Get all spaces
    print("Board Spaces Summary:")
    print(f"Total spaces: {len(board.spaces)}")
    
    # Print some key spaces
    key_positions = [0, 10, 20, 30, 39]
    print("\nKey positions:")
    for pos in key_positions:
        space = board.get_space(pos)
        print(f"  [{pos:2d}] {space.name:25} - {space.property_type.value}")
    
    # Get next railroad
    current_pos = 5
    next_rail = board.get_next_railroad(current_pos)
    print(f"\nNext railroad from position {current_pos}: {next_rail}")
    
    # Get next utility
    next_util = board.get_next_utility(current_pos)
    print(f"Next utility from position {current_pos}: {next_util}")


# ============================================================================
# EXAMPLE 9: GAME STATE SERIALIZATION
# ============================================================================

def example_serialization():
    """Example of serializing game state"""
    from core.game import MonopolyGame
    from core.utils import GameSerializer
    import json
    
    # Create and setup game
    game = MonopolyGame(["Alice", "Bob"])
    game.start_game()
    
    # Get game state
    state = game.get_game_state_dict()
    
    # Serialize to JSON
    json_str = GameSerializer.to_json(state)
    print("Serialized game state:")
    print(json_str[:200] + "...")  # Print first 200 chars
    
    # Deserialize
    restored = GameSerializer.from_json(json_str)
    print(f"\nRestored state type: {type(restored)}")
    print(f"Number of players: {len(restored['players'])}")


# ============================================================================
# EXAMPLE 10: COMPLETE GAME FLOW
# ============================================================================

def example_complete_game_flow():
    """Example of a complete game flow"""
    from core.game import MonopolyGame
    
    print("=" * 50)
    print("MONOPOLY GAME - EXAMPLE GAME FLOW")
    print("=" * 50)
    
    # Create game
    game = MonopolyGame(["Alice", "Bob"])
    game.start_game()
    
    print(f"\nGame started with {len(game.players)} players\n")
    
    # Play 10 turns
    for turn in range(10):
        print(f"--- TURN {turn + 1} ---")
        
        player = game.get_current_player()
        print(f"{player.name}'s turn (Money: ${player.money})")
        
        # Roll
        d1, d2 = game.roll_dice()
        print(f"  Rolled: {d1} + {d2}")
        
        # Move
        passed_go, new_pos = game.move_current_player()
        print(f"  Moved to: {game.board.get_space(new_pos).name}")
        
        if passed_go:
            print(f"  Passed GO! +$200")
        
        # Try to buy
        space = game.board.get_space(new_pos)
        if space.is_available() and player.money > space.purchase_price:
            game.purchase_property(player.player_id, new_pos)
            print(f"  Bought {space.name}!")
        
        # Next turn
        game.next_turn()
        print()


# ============================================================================
# MAIN - Run examples
# ============================================================================

if __name__ == "__main__":
    import sys
    
    examples = {
        "1": ("Local Game Simulation", example_local_game),
        "2": ("Server Setup", example_server_setup),
        "3": ("Client Setup", example_client_setup),
        "4": ("Property Management", example_property_management),
        "5": ("Player Management", example_player_management),
        "6": ("Dice Rolling", example_dice_rolling),
        "7": ("Card Drawing", example_card_drawing),
        "8": ("Board Navigation", example_board_navigation),
        "9": ("Game State Serialization", example_serialization),
        "10": ("Complete Game Flow", example_complete_game_flow),
    }
    
    print("\n" + "=" * 50)
    print("MONOPOLY GAME - USAGE EXAMPLES")
    print("=" * 50 + "\n")
    
    # Run specific example or all
    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice in examples:
            name, func = examples[choice]
            print(f"\nRunning: {name}\n")
            func()
        else:
            print("Invalid choice!")
    else:
        # Run all examples
        for key, (name, func) in sorted(examples.items()):
            print(f"\n{'=' * 50}")
            print(f"EXAMPLE {key}: {name}")
            print('=' * 50)
            try:
                func()
            except Exception as e:
                print(f"Error: {e}")
