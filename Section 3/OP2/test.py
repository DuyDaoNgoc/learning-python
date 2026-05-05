import sys

def system():
  hp = 10
  try:
      print(f"Processing item {"❤" * hp}")
  except Exception as e:
      print(f"An error occurred: {e}")

system()
