import random

def create_slot_machine():
  """Creates a list of 3 slots, each containing a random symbol."""
  symbols = ["🍒", "🍋", "🍇", "🍉", "🔔", "⭐", "💰"]
  slots = [random.choice(symbols) for _ in range(3)]
  return slots

def display_slots(slots):
  """Displays the slots in a visually appealing format."""
  print("-" * 15)
  for symbol in slots:
    print(f"|{symbol:^5}|")
  print("-" * 15)

def check_win(slots):
  """Checks if the player has won based on the symbols in the slots."""
  if slots[0] == slots[1] == slots[2]:
    return True
  else:
    return False

def play_slot_machine():
  """Main function to run the slot machine game."""
  print("Welcome to the Slot Machine!")
  while True:
    slots = create_slot_machine()
    display_slots(slots)
    if check_win(slots):
      print("Congratulations! You won!")
    else:
      print("Sorry, you didn't win this time.")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != 'y':
      break

if __name__ == "__main__":
  play_slot_machine()
