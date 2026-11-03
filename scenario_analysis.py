from game_data import strategies, payoff_matrix
from visualization import (
    display_travel_cost_chart,
    display_scenario_comparison
)

def get_scenario_cost(prompt):
    """
    Get a valid travel cost from the user.
    Travel costs cannot be negative.
    """

    while True:
        try:
            cost = float(input(prompt))

            if cost < 0:
                print("Travel cost cannot be negative.")
            else:
                return cost

        except ValueError:
            print("Please enter a valid number.")


def find_nash_equilibria_for_matrix(matrix):
    """
    Find pure-strategy Nash equilibria
    for a given payoff matrix.

    Lower travel cost is better for each player.
    """

    equilibria = []

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):

            # Find Player 1's minimum cost
            player1_costs = [
                matrix[r][column][0]
                for r in range(len(matrix))
            ]

            # Find Player 2's minimum cost
            player2_costs = [
                matrix[row][c][1]
                for c in range(len(matrix[row]))
            ]

            player1_best = (
                matrix[row][column][0] == min(player1_costs)
            )

            player2_best = (
                matrix[row][column][1] == min(player2_costs)
            )

            if player1_best and player2_best:
                equilibria.append((row, column))

    return equilibria


def display_equilibria(equilibria):
    """Display the Nash equilibria found."""

    if not equilibria:
        print("No pure-strategy Nash equilibrium was found.")
        return

    for row, column in equilibria:
        print(
            f"Player 1: {strategies[row]}, "
            f"Player 2: {strategies[column]}"
        )


def analyse_scenario():
    """
    Allow users to change travel costs,
    recalculate Nash equilibria and compare results.
    """

    print("\n========== TRAFFIC SCENARIO ANALYSIS ==========")

    # Preserve the original payoff matrix
    original_matrix = [
        [cell for cell in row]
        for row in payoff_matrix
    ]

    # Create a separate matrix for the new scenario
    scenario_matrix = [
        [cell for cell in row]
        for row in payoff_matrix
    ]

    print("\nEnter new travel costs for the four route combinations.")

    for row in range(2):
        for column in range(2):

            print(
                f"\n{strategies[row]} - {strategies[column]}"
            )

            player1_cost = get_scenario_cost(
                "Enter Player 1 travel cost: "
            )

            player2_cost = get_scenario_cost(
                "Enter Player 2 travel cost: "
            )

            scenario_matrix[row][column] = (
                player1_cost,
                player2_cost
            )

    # Analyse the original and changed scenarios
    original_equilibria = find_nash_equilibria_for_matrix(
        original_matrix
    )

    scenario_equilibria = find_nash_equilibria_for_matrix(
        scenario_matrix
    )

    print("\n========== ORIGINAL SCENARIO ==========")

    display_equilibria(original_equilibria)

    print("\n========== NEW SCENARIO ==========")

    display_equilibria(scenario_equilibria)

    print("\n========== EQUILIBRIUM COMPARISON ==========")

    if original_equilibria == scenario_equilibria:
        print("The pure-strategy Nash equilibrium did not change.")
    else:
        print("The pure-strategy Nash equilibrium changed.")

    # Temporarily update the main payoff matrix
    # so the existing graph displays the new scenario.
    try:
        for row in range(2):
            for column in range(2):
                payoff_matrix[row][column] = (
                    scenario_matrix[row][column]
                )

        print("\nDisplaying the new scenario graph...")
        display_travel_cost_chart()

    finally:
        # Restore the original values after the graph closes
        for row in range(2):
            for column in range(2):
                payoff_matrix[row][column] = (
                    original_matrix[row][column]
                )

    print("\nDisplaying the scenario comparison graph...")

    display_scenario_comparison(
        original_matrix,
        scenario_matrix,
        original_equilibria,
        scenario_equilibria
)

