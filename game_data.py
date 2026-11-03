
# ==========================================
# PROJECT: TRAFFIC CONGESTION MANAGEMENT
# STAGE 2: GAME REPRESENTATION
# ==========================================

# Define the players participating in the game
players = [
    "Player 1 (Driver A)",
    "Player 2 (Driver B)"
]

# Define the available strategies for each player
strategies = [
    "Route 1",
    "Route 2"
]

# Define the payoff matrix.
# Each tuple represents:
# (Player 1 travel cost, Player 2 travel cost)
#
# These are illustrative assumed travel costs.
# They are not real traffic measurements.

payoff_matrix = [
    [(12, 14), (10, 20)],
    [(18, 11), (22, 16)]
]

# ==========================================
# STAGE 5: MIXED STRATEGY TEST GAME
# ==========================================

# This is an illustrative game designed to
# demonstrate mixed-strategy Nash equilibrium.

mixed_strategy_matrix = [
    [(1, 2), (2, 1)],
    [(2, 1), (1, 2)]
]