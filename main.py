
# ==============================================
# PROJECT: TRAFFIC CONGESTION MANAGEMENT SYSTEM
# STAGE 2: USER INPUT AND OUTPUT
# ==============================================

# Import game information from game_data.py
from game_data import players, strategies, payoff_matrix
from visualization import display_travel_cost_chart
from scenario_analysis import analyse_scenario
from game_analysis import (
    analyse_best_responses,
    analyse_strategic_properties,
    calculate_mixed_strategy_equilibrium,
    analyse_sequential_game,
    analyse_repeated_game
)
def display_players():
    """Display the players participating in the game."""

    print("\n========== PLAYERS ==========")

    for player in players:
        print("-", player)


def display_strategies():
    """Display the available strategies for each player."""

    print("\n========== AVAILABLE STRATEGIES ==========")

    for player in players:
        print(f"\n{player}:")

        for strategy in strategies:
            print("-", strategy)


def display_payoff_matrix():
    """Display the payoff matrix showing travel costs."""

    print("\n========== PAYOFF MATRIX ==========")
    print("Values represent travel costs in minutes.")
    print("(Player 1 cost, Player 2 cost)\n")

    # Display column headings
    print(f"{'Player 1 / Player 2':<25}", end="")

    for strategy in strategies:
        print(f"{strategy:<20}", end="")

    print()

    # Display matrix rows
    for row_index, row in enumerate(payoff_matrix):

        print(f"{strategies[row_index]:<25}", end="")

        for payoff in row:
            print(f"{str(payoff):<20}", end="")

        print()

def get_valid_cost(prompt):
    """
    Ask the user to enter a valid travel cost.

    Travel costs must be numbers greater than or equal to zero.
    """

    while True:
        try:
            cost = float(input(prompt))

            if cost < 0:
                print("Travel cost cannot be negative. Try again.")
            else:
                return cost

        except ValueError:
            print("Invalid input. Please enter a number.")


def enter_custom_payoffs():
    """
    Allow users to enter new travel costs for every
    possible combination of routes.
    """

    print("\n========== ENTER CUSTOM PAYOFF VALUES ==========")
    print("Enter the travel costs in minutes.")
    print("Remember: Player 1 enters the first cost.")
    print("Player 2 enters the second cost.")

    for row in range(len(strategies)):

        for column in range(len(strategies)):

            print(
                f"\nWhen Player 1 chooses {strategies[row]} "
                f"and Player 2 chooses {strategies[column]}:"
            )

            player1_cost = get_valid_cost(
                "Enter Player 1's travel cost: "
            )

            player2_cost = get_valid_cost(
                "Enter Player 2's travel cost: "
            )

            # Update the existing payoff matrix
            payoff_matrix[row][column] = (
                player1_cost,
                player2_cost
            )

    print("\nPayoff matrix updated successfully!")
    print("Here is the new payoff matrix:")

    display_payoff_matrix()


def get_valid_choice(prompt, valid_choices):
    """
    Request input from the user and validate the choice.

    Returns a valid integer selected by the user.
    """

    while True:

        user_input = input(prompt).strip()

        try:
            choice = int(user_input)

            if choice in valid_choices:
                return choice

            print("Invalid choice. Please select an available option.")

        except ValueError:
            print("Invalid input. Please enter a number.")


def play_game():
    """Allow two players to select routes and display the outcome."""

    print("\n========== PLAY THE TRAFFIC GAME ==========")

    # Get Player 1's route selection
    print(f"\n{players[0]}")

    for index, strategy in enumerate(strategies, start=1):
        print(f"{index}. {strategy}")

    player1_choice = get_valid_choice(
        "Choose your route: ",
        range(1, len(strategies) + 1)
    )

    # Get Player 2's route selection
    print(f"\n{players[1]}")

    for index, strategy in enumerate(strategies, start=1):
        print(f"{index}. {strategy}")

    player2_choice = get_valid_choice(
        "Choose your route: ",
        range(1, len(strategies) + 1)
    )

    # Convert choices into matrix indexes
    row_index = player1_choice - 1
    column_index = player2_choice - 1

    # Retrieve the corresponding payoff
    outcome = payoff_matrix[row_index][column_index]

    player1_cost = outcome[0]
    player2_cost = outcome[1]

    # Display the results
    print("\n========== GAME RESULTS ==========")

    print(f"{players[0]} selected: {strategies[row_index]}")
    print(f"{players[1]} selected: {strategies[column_index]}")

    print("\nTRAVEL COSTS")

    print(f"Player 1: {player1_cost} minutes")
    print(f"Player 2: {player2_cost} minutes")

    print("\nTotal travel cost:", player1_cost + player2_cost, "minutes")



def display_menu():
    """Display the main application menu."""

    print("\n" + "=" * 45)
    print("TRAFFIC CONGESTION MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. View Players")
    print("2. View Available Routes")
    print("3. View Payoff Matrix")
    print("4. Play the Traffic Game")
    print("5. Analyse Best Responses")
    print("6. Enter Custom Payoff Values")
    print("7. Analyse Dominant Strategies and Nash Equilibrium")
    print("8. Calculate Mixed Strategy Equilibrium")
    print("9. Analyse Sequential Game")
    print("10. Analyse Repeated and Cooperative Games")
    print("11. View Travel Cost Graph")
    print("12. Analyse Traffic Scenarios")
    print("13. Exit")

def main():
    """Control the main application."""

    while True:

        display_menu()

        choice = get_valid_choice(
            "\nEnter your choice: ",
            range(1, 14)
        )

        if choice == 1:
            display_players()

        elif choice == 2:
            display_strategies()

        elif choice == 3:
            display_payoff_matrix()

        elif choice == 4:
            play_game()

        elif choice == 5:
            analyse_best_responses()

        elif choice == 6:
            enter_custom_payoffs()

        elif choice == 7:
            analyse_strategic_properties()

        elif choice == 8:
            calculate_mixed_strategy_equilibrium()

        elif choice == 9:
            analyse_sequential_game()

        elif choice == 10:
            rounds = get_valid_choice(
                "\nEnter the number of rounds: ",
                range(1, 101)
            )

            analyse_repeated_game(rounds)

        elif choice == 11:
            display_travel_cost_chart()
        elif choice == 12:
            analyse_scenario()
        elif choice == 13:
            print("\nThank you for using the Traffic Congestion Management System.")
            print("Goodbye!")
            break



# Run the application
if __name__ == "__main__":
    main()
