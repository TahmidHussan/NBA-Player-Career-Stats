import tkinter as tk
from tkinter import messagebox
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

# Get all players
player_dict = players.get_players()

# Function to calculate and print averages
def calculate_and_print_averages(career_df, player_name):
    games_played = career_df['GP'].sum()
    ppg = career_df['PTS'].sum() / games_played
    apg = career_df['AST'].sum() / games_played
    rpg = career_df['REB'].sum() / games_played

    # Return the averages as a string
    return f"{player_name} has played {games_played} games in his career.\n{ppg:.1f} ppg, {apg:.1f} apg, {rpg:.1f} rpg"


# Function to check the player
def check_player():
    player_name = player_name_entry.get().title()

    # Check if player exists
    if not any(player['full_name'] == player_name for player in player_dict):
        messagebox.showerror("Error", f"No player named {player_name} found.")
        return

    # Assigns the player to a variable called player
    player = [player for player in player_dict if player['full_name'] == player_name]

    # Get player's career stats
    player_career = playercareerstats.PlayerCareerStats(player_id=player[0]['id'])
    career_df = player_career.get_data_frames()[0]

    # Calculate and display averages
    averages = calculate_and_print_averages(career_df, player_name)  # pass player_name here
    messagebox.showinfo("Player Averages", averages)


# Function to clear the entry field
def clear_entry():
    player_name_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.geometry("500x150")

# Create a label and entry for the player name
player_name_label = tk.Label(root, text="Enter an NBA Player's name:")
player_name_label.pack(fill=tk.X)
player_name_entry = tk.Entry(root, font=("sylfaen", 14))
player_name_entry.pack(fill=tk.X)

# Create a button to check the player
check_button = tk.Button(root, text="Check Player", command=check_player, font=("sylfaen", 10))
check_button.pack(fill=tk.Y)

# Create a button to clear the entry field
clear_button = tk.Button(root, text="Clear", command=clear_entry, font=("sylfaen", 10))
clear_button.pack(fill=tk.Y)

# Start the main loop
root.mainloop()