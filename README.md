
# Traffic Congestion Management System

## Project Description

This project is a Python-based application that uses game theory
to model strategic route-selection decisions between road users.

The initial model considers two players who must choose between
two alternative routes.

The purpose is to demonstrate how individual route choices can
influence travel costs and traffic congestion.

## Technologies Used

- Python 3
- Visual Studio Code

## Project Structure

Traffic_Congestion_Game/
    main.py
    game_data.py
    README.md

## Game Representation

### Players

- Player 1 (Driver A)
- Player 2 (Driver B)

### Available Strategies

- Route 1
- Route 2

### Payoff Representation

Each payoff is represented as a tuple:

(Player 1 travel cost, Player 2 travel cost)

The values represent illustrative travel costs in minutes.

Lower values represent better outcomes for individual players.

The current values are assumed for demonstration and are
not actual traffic measurements.

## How to Run the Application

1. Install Python 3.
2. Open the project folder in Visual Studio Code.
3. Open the terminal.
4. Execute:

   python main.py

5. Follow the displayed menu.

## Implemented Features

- Player representation
- Strategy representation
- Payoff matrix representation
- Displaying game information
- Interactive menu
- User route selection
- Input validation
- Displaying travel costs

## Current Limitations

- The model uses two players.
- Only two alternative routes are considered.
- Travel costs are predefined.
- The application does not use live traffic data.
- Advanced game-theoretic analysis has not yet been implemented.

## Future Development

Future stages will introduce:

- Payoff matrix analysis
- Best-response calculations
- Dominant and dominated strategies
- Nash equilibrium analysis
- Mixed-strategy analysis where appropriate
- Visualization
- Scenario analysis
