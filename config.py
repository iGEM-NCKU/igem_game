
# Initialize
WIDTH, HEIGHT = 1280, 720
MAP_WIDTH, MAP_HEIGHT = 1280, 670

TILE_SIZE = 40

BIOFILM_TYPES = {
    "TIER1": {"cooldown": 30, "range": 120},
    "TIER2": {"cooldown": 90, "range": 200},
    "TIER3": {"cooldown": 60, "range": 150}
}


# STAGE
STAGE1 = {
    "S_a_forming_ratio" : 0.55,
    "S_forming_ratio" : 0.2,
    "E_coli_forming_ration" : 0.1,
    "P_aeruginosa" : 0.1,
    "Mycobacterium" : 0.05,
    "hearts": 10
}
GENERATION_WEIGHTS_STAGE_1 = [
    STAGE1["S_a_forming_ratio"],
    STAGE1["S_forming_ratio"],
    STAGE1["E_coli_forming_ration"],
    STAGE1["P_aeruginosa"],
    STAGE1["Mycobacterium"]
    
]

STAGE2 = 5
STAGE3 = 1

# Colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)
BLACK = (0, 0, 0)
GRAY = (87,87,87)
# Clock
FPS = 60


# Enemy Path
PATH = [(20, 300), (200, 300), (200, 500), (600, 500), (600, 100), (800, 100), (1000, 600)]

#path

BACKGROUND_IMAGE = "src/background.jpg"
USER_HEART = "src/heart.png"