import matplotlib.pyplot as plt

from game_data import strategies, payoff_matrix


def display_travel_cost_chart():

    # Store the route combinations
    combinations = [
        "Route 1 - Route 1",
        "Route 1 - Route 2",
        "Route 2 - Route 1",
        "Route 2 - Route 2"
    ]

    # Extract the travel costs for each player
    player1_costs = []
    player2_costs = []

    for row in payoff_matrix:
        for outcome in row:
            player1_costs.append(outcome[0])
            player2_costs.append(outcome[1])

    # Set the positions of the bars
    positions = range(len(combinations))
    bar_width = 0.35

    # Create the graph
    plt.figure(figsize=(10, 6))

    plt.bar(
        [position - bar_width / 2 for position in positions],
        player1_costs,
        bar_width,
        label="Player 1"
    )

    plt.bar(
        [position + bar_width / 2 for position in positions],
        player2_costs,
        bar_width,
        label="Player 2"
    )

    # Add graph labels and title
    plt.xlabel("Route Combinations")
    plt.ylabel("Travel Cost (Minutes)")
    plt.title("Travel Cost Comparison Between Two Drivers")

    plt.xticks(positions, combinations)
    plt.legend()

    plt.tight_layout()

    # Display the graph
    plt.show()


def display_scenario_comparison(
    original_matrix,
    scenario_matrix,
    original_equilibria,
    scenario_equilibria
):
    """
    Compare the combined travel costs of the original
    and new traffic scenarios.

    Mark route combinations that are Nash equilibria.
    """

    combinations = [
        "Route 1 - Route 1",
        "Route 1 - Route 2",
        "Route 2 - Route 1",
        "Route 2 - Route 2"
    ]

    original_totals = []
    scenario_totals = []

    # Calculate combined travel costs.
    for row in range(2):
        for column in range(2):

            original_total = (
                original_matrix[row][column][0]
                + original_matrix[row][column][1]
            )

            scenario_total = (
                scenario_matrix[row][column][0]
                + scenario_matrix[row][column][1]
            )

            original_totals.append(original_total)
            scenario_totals.append(scenario_total)

    positions = range(len(combinations))
    bar_width = 0.35

    plt.figure(figsize=(11, 6))

    original_bars = plt.bar(
        [p - bar_width / 2 for p in positions],
        original_totals,
        bar_width,
        label="Original Scenario"
    )

    scenario_bars = plt.bar(
        [p + bar_width / 2 for p in positions],
        scenario_totals,
        bar_width,
        label="New Scenario"
    )

    # Add numerical values above the bars.
    for bar in original_bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:g}",
            ha="center",
            va="bottom"
        )

    for bar in scenario_bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height:g}",
            ha="center",
            va="bottom"
        )

    # Mark Nash equilibria.
    for row, column in original_equilibria:
        index = row * 2 + column

        plt.text(
            index - bar_width / 2,
            original_totals[index] + 1,
            "Nash",
            ha="center",
            fontsize=8
        )

    for row, column in scenario_equilibria:
        index = row * 2 + column

        plt.text(
            index + bar_width / 2,
            scenario_totals[index] + 1,
            "Nash",
            ha="center",
            fontsize=8
        )

    plt.xlabel("Route Combinations")
    plt.ylabel("Combined Travel Cost (Minutes)")
    plt.title("Original vs New Traffic Scenario")
    plt.xticks(positions, combinations)
    plt.legend()

    plt.tight_layout()
    plt.show()