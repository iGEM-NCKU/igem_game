
# Initialize
WIDTH, HEIGHT = 800, 600
MAP_WIDTH, MAP_HEIGHT = 800, 550

BIOFILM_TYPES = {
    "TIER1": {"cooldown": 30, "range": 120},
    "TIER2": {"cooldown": 90, "range": 200},
    "TIER3": {"cooldown": 60, "range": 150}
}


# STAGE
STAGE1 = 10
STAGE2 = 5
STAGE3 = 1

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)

# Clock
FPS = 60


# Enemy Path
PATH = [(0, 300), (200, 300), (200, 500), (600, 500), (600, 100), (800, 100)]

#path

BACKGROUND_IMAGE = "src/background.jpg"