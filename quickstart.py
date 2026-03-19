#!/usr/bin/env python3
"""
Quick start script for Monopoly game
This script helps set up and run the game with simple options
"""

import sys
import os
import subprocess
import platform
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from config import Config

def print_banner():
    """Print game banner"""
    banner = """
    ╔════════════════════════════════════════════════════════════════╗
    ║                                                                ║
    ║           🎲 MONOPOLY - Online Edition 🏠                    ║
    ║                                                                ║
    ║                  Starter Quick Setup Guide                    ║
    ║                                                                ║
    ╚════════════════════════════════════════════════════════════════╝
    """
    print(banner)

def install_dependencies():
    """Install required packages"""
    print("\n📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("✗ Failed to install dependencies")
        print("  Please run: pip install -r requirements.txt")
        return False

def run_tests():
    """Run test suite"""
    print("\n🧪 Running tests...")
    try:
        result = subprocess.run([sys.executable, "test_game.py"], capture_output=True, text=True)
        print(result.stdout)
        if result.returncode == 0:
            print("✓ All tests passed!")
            return True
        else:
            print("✗ Some tests failed")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"✗ Error running tests: {e}")
        return False

def run_server(num_players=2):
    """Run game server"""
    print(f"\n🚀 Starting Monopoly server for {num_players} players...")
    print(f"   Host: {Config.SERVER_HOST}")
    print(f"   Port: {Config.SERVER_PORT}")
    print(f"   Waiting for {num_players} players to connect...\n")
    
    try:
        subprocess.run([sys.executable, "server/monopoly_server.py", str(num_players)])
    except KeyboardInterrupt:
        print("\n✗ Server stopped")

def run_client(host="localhost", port=5000, player_name="Player"):
    """Run game client"""
    print(f"\n🎮 Starting Monopoly client...")
    print(f"   Connecting to: {host}:{port}")
    print(f"   Player name: {player_name}\n")
    
    try:
        subprocess.run([sys.executable, "client/game_ui.py", host, str(port), player_name])
    except KeyboardInterrupt:
        print("\n✗ Client stopped")

def show_menu():
    """Show main menu"""
    print("\n" + "="*60)
    print("What would you like to do?")
    print("="*60)
    print("\n1. Run Tests (verify game logic)")
    print("2. Start Game Server (for multiplayer)")
    print("3. Start Game Client (to play)")
    print("4. Quick Demo (server + 2 clients)")
    print("5. Install Dependencies")
    print("6. About Monopoly")
    print("0. Exit")
    print()

def show_about():
    """Show about information"""
    about = """
    Monopoly - Online Edition
    Version: 1.0.0
    
    Features:
    - Complete Monopoly game rules
    - Online multiplayer (2-6 players)
    - Beautiful Pygame graphics
    - Real-time game synchronization
    - Full property management system
    - Chance and Community Chest cards
    
    Keyboard Controls:
    - SPACE: Roll Dice
    - E: End Turn
    - ESC: Exit Game
    
    System Requirements:
    - Python 3.8+
    - Pygame 2.5.0+
    - Windows, macOS, or Linux
    
    For more information, see README.md
    """
    print(about)

def demo_mode():
    """Run demo with server and clients"""
    print("\n" + "="*60)
    print("Note: Demo mode requires multiple terminals/windows")
    print("="*60)
    print("\nDemo mode will show commands to run in different terminals:")
    print("\n1. Terminal 1 - Run the server:")
    print(f"   python server/monopoly_server.py 2")
    print("\n2. Terminal 2 - Run client 1:")
    print(f"   python client/game_ui.py localhost 5000 Player1")
    print("\n3. Terminal 3 - Run client 2:")
    print(f"   python client/game_ui.py localhost 5000 Player2")
    print("\nPress Enter to copy first command to clipboard...")
    input()

def main():
    """Main menu loop"""
    print_banner()
    
    while True:
        show_menu()
        choice = input("Enter your choice (0-6): ").strip()
        
        if choice == "0":
            print("\n👋 Thanks for playing Monopoly! Goodbye!")
            sys.exit(0)
        
        elif choice == "1":
            run_tests()
        
        elif choice == "2":
            try:
                num_players = int(input("\nHow many players? (2-6, default 2): ") or "2")
                if 2 <= num_players <= 6:
                    run_server(num_players)
                else:
                    print("Invalid number of players")
            except ValueError:
                print("Invalid input")
        
        elif choice == "3":
            host = input("\nServer host (default: localhost): ").strip() or "localhost"
            try:
                port = int(input("Server port (default: 5000): ").strip() or "5000")
                player_name = input("Your player name: ").strip() or "Player"
                run_client(host, port, player_name)
            except ValueError:
                print("Invalid input")
        
        elif choice == "4":
            demo_mode()
        
        elif choice == "5":
            install_dependencies()
        
        elif choice == "6":
            show_about()
        
        else:
            print("Invalid choice. Please try again.")
        
        input("\n Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Exiting...")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
