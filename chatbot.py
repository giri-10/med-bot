import requests

def bard_response(prompt):
  """
  Sends a prompt to the Bard API and returns the response.
  """
  # Replace with your Bard API key
  api_key = "XAg0_B40cwSPvEeWX5x03f4JV3LsLe7g1PHRyjw8oq8xUVn-Qork9Xf5te-qooqVs4Z2Vg"

  url = "http://localhost:8080/bot/chat"
  headers = {"Authorization": f"Bearer {api_key}"}
  data = {"input": prompt}

  response = requests.post(url, headers=headers, json=data)
  response.raise_for_status()

  return response.json()["text"]

def main():
  # Prompt the user for input
  user_input = input("What would you like to talk about? ")

  # Send the prompt to Bard and get the response
  bard_text = bard_response(user_input)

  # Print the Bard response
  print(f"\nBard: {bard_text}")

if __name__ == "__main__":
  main()