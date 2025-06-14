import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Main function
def main():
    load_dotenv()

    # Handle arguments
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith(("-", "--", "v"))]

    if not args:
        print(f"AI Code Assistant")
        print(f'\nUsage: python main.py "your prompt here" [--verbose]')
        print(f'\nExample: python main.py "How do I build a calculator app?"')
        sys.exit(1)
    user_prompt = " ".join(args)
 
    # Prepare the client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Prepare the messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Generate the response
    generate_content(client, messages, verbose)

def generate_content(client, messages, verbose):
    model = "gemini-2.0-flash-001"
    #model = "gemini-2.0-flash-lite"
    response = client.models.generate_content(
        model=model, 
        contents=messages
    )
    
    # If verbose, print the prompt tokens, response tokens, and total token count
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total token count: {response.usage_metadata.total_token_count}")

    # Print the response
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
