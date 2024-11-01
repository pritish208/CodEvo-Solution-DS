import json
import random
import string

# Load JSON data containing intents
def load_intents(file_path):
   
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents

# Preprocess user input to make it easier to match with intents
def preprocess_input(user_input):
   
    user_input = user_input.lower() 
    user_input = user_input.translate(str.maketrans('', '', string.punctuation))  
    return user_input.split() 

# Calculate a similarity score between user input and patterns of an intent
def calculate_similarity(input_words, pattern_words):
 
    input_set = set(input_words)
    pattern_set = set(pattern_words)
    
    # Count the number of common words
    common_words = input_set.intersection(pattern_set)
    
    # Return the number of common words as the similarity score
    return len(common_words)

# Match the user's input with one of the intents in the JSON file
def match_intent(user_input, intents):
   
    input_words = preprocess_input(user_input)  # Preprocess the user's input
    best_intent = None
    best_score = 0

    # Loop through each intent and each pattern
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_words = preprocess_input(pattern)  # Preprocess the pattern

            # Calculate the similarity score
            score = calculate_similarity(input_words, pattern_words)

            # If this pattern has a better score, update the best match
            if score > best_score:
                best_score = score
                best_intent = intent

    # If we found an intent with a matching pattern, return a random response from that intent
    if best_intent and best_score > 0:
        return random.choice(best_intent['responses'])
    
    
    return "I didn't understand that. Can you try again?"

# Main chatbot interface for interacting with users
def chatbot():
   
    intents = load_intents('intents.json')  # Load intents from the JSON file
    print("ChatBot: Hello! Ask me anything (type 'quit' to exit)")

    while True:
        user_input = input("You: ")  # Get input from the user
        if user_input.lower() == "quit":  # Exit if the user types 'quit'
            print("ChatBot: Goodbye!")
            break
        response = match_intent(user_input, intents)  # Match the input to an intent
        print(f"ChatBot: {response}")  # Output the chatbot's response

# Run the chatbot if this script is executed
if __name__ == "__main__":
    chatbot()
