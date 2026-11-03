
# ==============================================
# TRAFFIC CONGESTION MANAGEMENT SYSTEM
# STAGE 3: PAYOFF MATRIX ANALYSIS
# ==============================================

from game_data import strategies, payoff_matrix
from game_data import strategies, payoff_matrix, mixed_strategy_matrix

def get_player1_best_responses(player2_strategy_index):
    """
    Find Player 1's best response to Player 2's strategy.

    Since the game minimizes travel costs, the lowest
    cost represents the best response.
    """

    player1_costs = [
        payoff_matrix[row][player2_strategy_index][0]
        for row in range(len(strategies))
    ]

    lowest_cost = min(player1_costs)

    best_responses = [
        strategies[index]
        for index, cost in enumerate(player1_costs)
        if cost == lowest_cost
    ]

    return best_responses


def get_player2_best_responses(player1_strategy_index):
    """
    Find Player 2's best response to Player 1's strategy.

    The lowest travel cost represents the best response.
    """

    player2_costs = [
        payoff_matrix[player1_strategy_index][column][1]
        for column in range(len(strategies))
    ]

    lowest_cost = min(player2_costs)

    best_responses = [
        strategies[index]
        for index, cost in enumerate(player2_costs)
        if cost == lowest_cost
    ]

    return best_responses

def analyse_best_responses():
    """
    Analyse and display the best responses of both players
    for every possible strategy of the opponent.
    """

    print("\n========== BEST RESPONSE ANALYSIS ==========")

    print("\nPLAYER 1 (DRIVER A)")
    print("Player 1's best response to each Player 2 strategy:")

    for opponent_index, opponent_strategy in enumerate(strategies):

        best_responses = get_player1_best_responses(opponent_index)

        print(
            f"\nIf Player 2 chooses {opponent_strategy}, "
            f"Player 1's best response is: "
            f"{', '.join(best_responses)}"
        )

    print("\nPLAYER 2 (DRIVER B)")
    print("Player 2's best response to each Player 1 strategy:")

    for opponent_index, opponent_strategy in enumerate(strategies):

        best_responses = get_player2_best_responses(opponent_index)

        print(
            f"\nIf Player 1 chooses {opponent_strategy}, "
            f"Player 2's best response is: "
            f"{', '.join(best_responses)}"
        )
def find_dominant_strategy(player):
    """
    Find a strictly dominant strategy for a player.

    Player 1 uses the first cost in each payoff tuple.
    Player 2 uses the second cost.

    A strategy is strictly dominant if it gives a lower
    cost than every alternative strategy for every
    possible choice of the opponent.
    """

    for strategy_index in range(len(strategies)):

        is_dominant = True

        for opponent_index in range(len(strategies)):

            if player == 1:

                selected_cost = payoff_matrix[strategy_index][opponent_index][0]

                alternative_costs = [
                    payoff_matrix[other_index][opponent_index][0]
                    for other_index in range(len(strategies))
                    if other_index != strategy_index
                ]

            else:

                selected_cost = payoff_matrix[opponent_index][strategy_index][1]

                alternative_costs = [
                    payoff_matrix[opponent_index][other_index][1]
                    for other_index in range(len(strategies))
                    if other_index != strategy_index
                ]

            if alternative_costs and not all(
                selected_cost < cost for cost in alternative_costs
            ):
                is_dominant = False
                break

        if is_dominant:
            return strategies[strategy_index]

    return None

def find_dominated_strategies(player):
    """
    Identify strictly dominated strategies.

    A strategy is strictly dominated when another
    strategy always produces a lower travel cost.
    """

    dominated_strategies = []

    for strategy_index in range(len(strategies)):

        for alternative_index in range(len(strategies)):

            if strategy_index == alternative_index:
                continue

            is_dominated = True

            for opponent_index in range(len(strategies)):

                if player == 1:

                    selected_cost = payoff_matrix[strategy_index][opponent_index][0]

                    alternative_cost = payoff_matrix[alternative_index][opponent_index][0]

                else:

                    selected_cost = payoff_matrix[opponent_index][strategy_index][1]

                    alternative_cost = payoff_matrix[opponent_index][alternative_index][1]

                if alternative_cost >= selected_cost:
                    is_dominated = False
                    break

            if is_dominated:
                dominated_strategies.append(strategies[strategy_index])
                break

    return dominated_strategies

def find_nash_equilibria():
    """
    Identify all pure-strategy Nash equilibria.

    A combination is a Nash equilibrium if neither
    player can reduce their travel cost by changing
    their own strategy alone.
    """

    equilibria = []

    for row in range(len(strategies)):

        for column in range(len(strategies)):

            player1_cost = payoff_matrix[row][column][0]
            player2_cost = payoff_matrix[row][column][1]

            # Check whether Player 1 is choosing
            # a lowest-cost strategy.
            player1_best = all(
                player1_cost <= payoff_matrix[other_row][column][0]
                for other_row in range(len(strategies))
            )

            # Check whether Player 2 is choosing
            # a lowest-cost strategy.
            player2_best = all(
                player2_cost <= payoff_matrix[row][other_column][1]
                for other_column in range(len(strategies))
            )

            if player1_best and player2_best:

                equilibria.append(
                    (
                        strategies[row],
                        strategies[column],
                        player1_cost,
                        player2_cost
                    )
                )

    return equilibria 

def analyse_strategic_properties():
    """
    Display dominant strategies, dominated strategies
    and pure-strategy Nash equilibria.
    """

    print("\n========== STRATEGIC ANALYSIS ==========")

    # Player 1 analysis
    print("\nPLAYER 1 (DRIVER A)")

    player1_dominant = find_dominant_strategy(1)

    if player1_dominant:
        print(f"Strictly dominant strategy: {player1_dominant}")
    else:
        print("No strictly dominant strategy found.")

    player1_dominated = find_dominated_strategies(1)

    if player1_dominated:
        print(
            "Strictly dominated strategies: "
            + ", ".join(player1_dominated)
        )
    else:
        print("No strictly dominated strategies found.")

    # Player 2 analysis
    print("\nPLAYER 2 (DRIVER B)")

    player2_dominant = find_dominant_strategy(2)

    if player2_dominant:
        print(f"Strictly dominant strategy: {player2_dominant}")
    else:
        print("No strictly dominant strategy found.")

    player2_dominated = find_dominated_strategies(2)

    if player2_dominated:
        print(
            "Strictly dominated strategies: "
            + ", ".join(player2_dominated)
        )
    else:
        print("No strictly dominated strategies found.")

    # Nash equilibrium analysis
    print("\nPURE-STRATEGY NASH EQUILIBRIUM")

    equilibria = find_nash_equilibria()

    if equilibria:

        for equilibrium in equilibria:

            player1_strategy, player2_strategy, cost1, cost2 = equilibrium

            print(
                f"Player 1 chooses {player1_strategy}, "
                f"Player 2 chooses {player2_strategy}"
            )

            print(
                f"Resulting travel costs: "
                f"Player 1 = {cost1} minutes, "
                f"Player 2 = {cost2} minutes"
            )

    else:
        print("No pure-strategy Nash equilibrium found.")

def calculate_mixed_strategy_equilibrium():
    """
    Calculate the mixed-strategy Nash equilibrium
    for a two-player, two-strategy cost-minimization game.
    """

    # Extract the four payoff combinations.
    a = mixed_strategy_matrix[0][0][0]
    b = mixed_strategy_matrix[0][1][0]
    c = mixed_strategy_matrix[1][0][0]
    d = mixed_strategy_matrix[1][1][0]

    e = mixed_strategy_matrix[0][0][1]
    f = mixed_strategy_matrix[0][1][1]
    g = mixed_strategy_matrix[1][0][1]
    h = mixed_strategy_matrix[1][1][1]

    # Calculate the denominators.
    denominator_q = a - b - c + d
    denominator_p = e - f - g + h

    if denominator_q == 0 or denominator_p == 0:
        print("Cannot calculate a unique interior mixed strategy.")
        return

    # Calculate the equilibrium probabilities.
    q = (d - b) / denominator_q
    p = (h - g) / denominator_p

    # Check whether the probabilities form an
    # interior mixed-strategy equilibrium.
    if not (0 < p < 1 and 0 < q < 1):
        print("No interior mixed-strategy equilibrium found.")
        return

    # Calculate expected travel costs.
    player1_expected_cost = (
        q * a + (1 - q) * b
    )

    player2_expected_cost = (
        p * e + (1 - p) * f
    )

    print("\n========== MIXED STRATEGY ANALYSIS ==========")

    print("\nPLAYER 1 (DRIVER A)")
    print(f"Probability of choosing Route 1: {p:.2f}")
    print(f"Probability of choosing Route 2: {1 - p:.2f}")

    print("\nPLAYER 2 (DRIVER B)")
    print(f"Probability of choosing Route 1: {q:.2f}")
    print(f"Probability of choosing Route 2: {1 - q:.2f}")

    print("\nEXPECTED TRAVEL COSTS")
    print(f"Player 1: {player1_expected_cost:.2f} minutes")
    print(f"Player 2: {player2_expected_cost:.2f} minutes")

def analyse_sequential_game():
    """
    Analyse a sequential game using backward induction.

    Player 1 chooses first.
    Player 2 observes Player 1's decision and responds.

    Both players aim to minimize their travel costs.
    """

    print("\n========== SEQUENTIAL GAME ANALYSIS ==========")

    print("\nPlayer 1 makes the first decision.")
    print("Player 2 observes and then chooses a route.")

    # Store Player 2's best response to each
    # possible decision by Player 1.
    player2_responses = {}

    print("\nSTEP 1: PLAYER 2'S DECISIONS")

    for row in range(len(strategies)):

        player2_costs = [
            payoff_matrix[row][column][1]
            for column in range(len(strategies))
        ]

        best_cost = min(player2_costs)

        # Find the first route with the lowest cost.
        best_column = player2_costs.index(best_cost)

        best_response = strategies[best_column]

        player2_responses[row] = best_column

        print(
            f"\nIf Player 1 chooses {strategies[row]}, "
            f"Player 2 chooses {best_response}."
        )

        print(f"Player 2's travel cost: {best_cost} minutes.")

    # Work backwards to determine Player 1's decision.
    print("\nSTEP 2: PLAYER 1'S DECISION")

    player1_outcomes = []

    for row in range(len(strategies)):

        column = player2_responses[row]

        player1_cost = payoff_matrix[row][column][0]

        player1_outcomes.append(player1_cost)

        print(
            f"If Player 1 chooses {strategies[row]}, "
            f"the resulting Player 1 cost is "
            f"{player1_cost} minutes."
        )

    lowest_cost = min(player1_outcomes)

    best_row = player1_outcomes.index(lowest_cost)

    best_column = player2_responses[best_row]

    # Display the final predicted outcome.
    final_outcome = payoff_matrix[best_row][best_column]

    print("\nSTEP 3: FINAL SEQUENTIAL GAME OUTCOME")

    print(f"Player 1 chooses: {strategies[best_row]}")
    print(f"Player 2 chooses: {strategies[best_column]}")

    print(
        f"Player 1 travel cost: {final_outcome[0]} minutes"
    )

    print(
        f"Player 2 travel cost: {final_outcome[1]} minutes"
    )

    print("\nSequential game analysis completed.")

def analyse_repeated_game(rounds):
    """
    Simulate repeated interactions between two drivers.

    Compare repeated independent route choices with
    a simple cooperative route arrangement.
    """

    print("\n========== REPEATED GAME ANALYSIS ==========")

    # Scenario 1: Both drivers repeatedly choose Route 1.
    independent_costs = [0, 0]

    # Scenario 2: Drivers coordinate by choosing
    # different routes.
    cooperative_costs = [0, 0]

    print(f"\nNumber of rounds: {rounds}")

    print("\nSCENARIO 1: INDEPENDENT ROUTE CHOICES")
    print("Both drivers choose Route 1 in every round.")

    for round_number in range(1, rounds + 1):

        outcome = payoff_matrix[0][0]

        independent_costs[0] += outcome[0]
        independent_costs[1] += outcome[1]

        print(
            f"Round {round_number}: "
            f"Player 1 = {outcome[0]} minutes, "
            f"Player 2 = {outcome[1]} minutes"
        )

    print("\nSCENARIO 2: COOPERATIVE ROUTE ARRANGEMENT")
    print("Player 1 chooses Route 1.")
    print("Player 2 chooses Route 2.")

    for round_number in range(1, rounds + 1):

        outcome = payoff_matrix[0][1]

        cooperative_costs[0] += outcome[0]
        cooperative_costs[1] += outcome[1]

        print(
            f"Round {round_number}: "
            f"Player 1 = {outcome[0]} minutes, "
            f"Player 2 = {outcome[1]} minutes"
        )

    # Calculate average travel costs.
    independent_averages = [
        cost / rounds for cost in independent_costs
    ]

    cooperative_averages = [
        cost / rounds for cost in cooperative_costs
    ]

    # Display the comparison.
    print("\n========== FINAL COMPARISON ==========")

    print("\nINDEPENDENT DECISIONS")
    print(f"Player 1 total cost: {independent_costs[0]} minutes")
    print(f"Player 2 total cost: {independent_costs[1]} minutes")

    print("\nCOOPERATIVE ARRANGEMENT")
    print(f"Player 1 total cost: {cooperative_costs[0]} minutes")
    print(f"Player 2 total cost: {cooperative_costs[1]} minutes")

    print("\nAVERAGE TRAVEL COST PER ROUND")

    print(
        f"Independent decisions: "
        f"Player 1 = {independent_averages[0]:.2f}, "
        f"Player 2 = {independent_averages[1]:.2f} minutes"
    )

    print(
        f"Cooperative arrangement: "
        f"Player 1 = {cooperative_averages[0]:.2f}, "
        f"Player 2 = {cooperative_averages[1]:.2f} minutes"
    )