"""Example/Test file for running Monopoly locally"""
import sys
import os
import time
import threading

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.game import MonopolyGame
from core.player import Player
from core.board import Board
from core.dice import Dice


def test_game_logic():
    """Test basic game logic without networking"""
    print("=" * 50)
    print("MONOPOLY - Local Game Logic Test")
    print("=" * 50)
    
    # Create a game with 2 players
    game = MonopolyGame(["Alice", "Bob"])
    
    print(f"\nCreated game with {len(game.players)} players:")
    for player in game.players:
        print(f"  - {player.name}: ${player.money} at position {player.position}")
    
    # Start the game
    game.start_game()
    print(f"\nGame started! State: {game.game_state.value}")
    
    # Simulate some turns
    print("\n" + "=" * 50)
    print("SIMULATING GAME PLAY")
    print("=" * 50)
    
    for turn in range(5):
        print(f"\n--- TURN {turn + 1} ---")
        
        player = game.get_current_player()
        print(f"\n{player.name}'s turn (Money: ${player.money})")
        
        # Roll dice
        dice_result = game.roll_dice()
        print(f"  Rolled: {dice_result[0]}, {dice_result[1]} = {sum(dice_result)}")
        
        # Move player
        passed_go, new_pos = game.move_current_player()
        if passed_go:
            print(f"  Passed GO! Collected $200")
        print(f"  Moved to position {new_pos}: {game.board.get_space(new_pos).name}")
        
        # Handle landing
        space = game.board.get_space(new_pos)
        if space.is_available():
            print(f"  Space is available for purchase! Cost: ${space.purchase_price}")
            # Purchase property
            if game.purchase_property(player.player_id, new_pos):
                print(f"  ✓ {player.name} purchased {space.name}!")
            else:
                print(f"  ✗ Not enough money to purchase")
        elif space.owner is not None:
            print(f"  Space is owned by {game.players[space.owner].name}")
        else:
            print(f"  Special space: {space.name}")
        
        # Next turn
        game.next_turn()
        
        # Print current state
        print(f"\nCurrent standings:")
        for p in game.players:
            print(f"  {p.name}: ${p.money}, {len(p.owned_properties)} properties")
    
    print("\n" + "=" * 50)
    print("TEST COMPLETED")
    print("=" * 50)


def test_board():
    """Test board initialization"""
    print("\n" + "=" * 50)
    print("BOARD TEST")
    print("=" * 50)
    
    board = Board()
    
    print(f"\nBoard has {len(board.spaces)} spaces:")
    
    # Print first 10 spaces
    print("\nFirst 10 spaces:")
    for i in range(10):
        space = board.spaces[i]
        print(f"  [{i:2d}] {space.name:25} - Type: {space.property_type.value}")
    
    # Print some specific properties
    print("\n\nSample Properties:")
    props_to_show = [1, 6, 11, 39]
    for idx in props_to_show:
        space = board.spaces[idx]
        if space.property_type.value == "street":
            print(f"\n{space.name}:")
            print(f"  Cost: ${space.purchase_price}")
            print(f"  Base Rent: ${space.rent_base}")
            print(f"  With 1 House: ${space.rent_with_houses[0]}")
            print(f"  With Hotel: ${space.rent_with_hotel}")


def test_dice():
    """Test dice roller"""
    print("\n" + "=" * 50)
    print("DICE TEST")
    print("=" * 50)
    
    dice = Dice()
    
    print("\nRolling dice 10 times:")
    doubles_count = 0
    for i in range(10):
        result = dice.roll()
        is_double = "DOUBLES!" if dice.is_doubles() else ""
        if dice.is_doubles():
            doubles_count += 1
        print(f"  Roll {i+1}: [{result[0]}, {result[1]}] = {dice.get_total()} {is_double}")
    
    print(f"\nDoubles rolled: {doubles_count} times")


def test_player():
    """Test player class"""
    print("\n" + "=" * 50)
    print("PLAYER TEST")
    print("=" * 50)
    
    player = Player(0, "TestPlayer", "red")
    
    print(f"\nCreated player: {player}")
    print(f"  Starting money: ${player.money}")
    print(f"  Position: {player.position}")
    
    # Test money operations
    print(f"\nTesting money operations:")
    player.add_money(100)
    print(f"  After adding $100: ${player.money}")
    
    player.remove_money(50)
    print(f"  After removing $50: ${player.money}")
    
    # Test movement
    print(f"\nTesting movement:")
    print(f"  Starting position: {player.position}")
    passed_go = player.move_to_position(25)
    print(f"  Moved to position 25: {player.position}")
    print(f"  Passed GO: {passed_go}")
    
    passed_go = player.move_to_position(5)
    print(f"  Moved to position 5: {player.position}")
    print(f"  Passed GO: {passed_go}")
    print(f"  Final money: ${player.money}")
    
    # Test jail
    print(f"\nTesting jail:")
    player.go_to_jail()
    print(f"  In jail: {player.in_jail}")
    print(f"  Position: {player.position}")
    player.release_from_jail()
    print(f"  Released from jail: {not player.in_jail}")


def run_all_tests():
    """Run all test functions"""
    print("\n\n")
    print("╔" + "=" * 48 + "╗")
    print("║" + " MONOPOLY GAME - LOCAL TEST SUITE ".center(48) + "║")
    print("╚" + "=" * 48 + "╝")
    
    test_dice()
    test_player()
    test_board()
    test_game_logic()
    
    print("\n" + "=" * 50)
    print("ALL TESTS COMPLETED SUCCESSFULLY! ✓")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    try:
        run_all_tests()
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
        import traceback
        traceback.print_exc()
