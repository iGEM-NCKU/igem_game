
# Initialize
WIDTH, HEIGHT = 800, 600

# Tower type
TOWER_TYPES = {
    "Fast": {"cooldown": 30, "range": 120},
    "Sniper": {"cooldown": 90, "range": 200},
    "Normal": {"cooldown": 60, "range": 150}
}

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