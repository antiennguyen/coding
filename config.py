"""Configuration file for Monopoly game"""
import os


class Config:
    """Base configuration"""
    
    # Game settings
    GAME_NAME = "Monopoly - Online Edition"
    GAME_VERSION = "1.0.0"
    
    # Default player settings
    DEFAULT_NUM_PLAYERS = 2
    MIN_PLAYERS = 2
    MAX_PLAYERS = 6
    
    # Server settings
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5000
    MAX_CONNECTIONS = 6
    
    # Game mechanics
    STARTING_MONEY = 1500
    PASS_GO_MONEY = 200
    JAIL_BAIL = 50
    INCOME_TAX = 200
    LUXURY_TAX = 75
    
    # Board
    BOARD_SIZE = 40
    GO_POSITION = 0
    JAIL_POSITION = 10
    FREE_PARKING_POSITION = 20
    GO_TO_JAIL_POSITION = 30
    
    # UI Settings (pygame)
    WINDOW_WIDTH = 1400
    WINDOW_HEIGHT = 900
    FPS = 60
    
    # Colors (RGB tuples)
    COLORS = {
        "white": (255, 255, 255),
        "black": (0, 0, 0),
        "gray": (128, 128, 128),
        "light_gray": (200, 200, 200),
        "dark_gray": (64, 64, 64),
        "red": (220, 20, 60),
        "blue": (30, 144, 255),
        "green": (34, 139, 34),
        "yellow": (255, 215, 0),
        "orange": (255, 165, 0),
        "purple": (147, 112, 219),
    }
    
    # Logging
    LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
    LOG_FILE = os.path.join(LOG_DIR, "monopoly.log")
    
    @classmethod
    def ensure_log_dir(cls):
        """Ensure log directory exists"""
        os.makedirs(cls.LOG_DIR, exist_ok=True)


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    SERVER_HOST = "localhost"
    TESTING = False


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SERVER_HOST = "0.0.0.0"
    TESTING = False


class TestingConfig(Config):
    """Testing configuration"""
    DEBUG = True
    SERVER_HOST = "localhost"
    TESTING = True
    DEFAULT_NUM_PLAYERS = 2


# Default configuration
current_config = DevelopmentConfig
