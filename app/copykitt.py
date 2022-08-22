import os
import openai
import argparse
import re
from typing import List

MAX_INPUT_LENGTH = 24

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input
    
    print(f"User input: {user_input}")
    if validate_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else: 
        raise ValueError(f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}: this won't be processed."
        )
    
# validate length of prompt is less than 12
def validate_length(prompt: str) -> bool:
    return len(prompt) <= 12
    
def generate_keywords(prompt: str) -> List[str]: # return a LIST of Strings
# Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate related keywords for {prompt}: " 
    print(enriched_prompt)
    response = openai.Completion.create(
            model="text-davinci-002", prompt= enriched_prompt, temperature=1, max_tokens=32)
    
    # Extract output text.
    keywords_text = response['choices'][0]["text"]
    # strip the leading and trailing white space
    keywords_text = keywords_text.strip()
    # Return a list of the keywords
    keywords_array = re.split(", | \n, | ; | - ", keywords_text)
    # List comprehension to creat a new array and remove white spaces from each element
    keywords_array = [k.strip().lower() for k in keywords_array]
    # Remove any elements that are EMPTY
    keywords_array = [k for k in keywords_array if len(k)> 0]
    print(f"Keywords: {keywords_array}")
    return keywords_array

def generate_branding_snippet(prompt: str) -> str:
# Load your API key from an environment variable or secret management service
    openai.api_key = os.getenv("OPENAI_API_KEY")
    enriched_prompt = f"Generate related upbeat branding snippet for {prompt}: " 
    print(enriched_prompt)
    response = openai.Completion.create(
            model="text-davinci-002", prompt= enriched_prompt, temperature=2, max_tokens=32)
    
    # Extract output text.
    branding_text = response['choices'][0]["text"]
    # strip the leading and trailing white space
    branding_text = branding_text.strip() 
    
    # Check if the last character does not end in these, append the elipses
    last_character = branding_text[-1]   
    if last_character not in { ".", "!", "?"}:
        branding_text += "..."
    print(f"Snippet: {branding_text}")
    return branding_text


if __name__ == "__main__":
    main()