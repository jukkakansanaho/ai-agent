import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Main function
def main():
    load_dotenv()

    # Handle arguments
    args = sys.argv[1:]
    if not args:
        print(f"AI Code Assistant")
        print(f"\nUsage: python main.py <prompt>")
        print(f"\nExample: python main.py 'What is the capital of France?'")
        sys.exit(1)
    print(f"Args: {args}")
    user_prompt = " ".join(args[0])

    '''
    # Handle arguments - alternative
    parser = argparse.ArgumentParser(
        description='AI Code Assistant',
        usage='%(prog)s [options] <prompt>',
        )
    parser.add_argument(
        'prompt',
        type=str,
        help='The prompt to send to the model (a string).'
    )
    parser.add_argument(
        '-v', '--verbose',
        type=str
    )
    args = parser.parse_args()
    user_prompt = args.prompt
    ''' 
    # Prepare the client
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    # Prepare the messages
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    # Generate the response
    generate_content(client, messages, args)

def generate_content(client, messages, args):
    user_prompt = args[0] #"".join(messages[0].parts[0].text)
    optional_args = args[1:]
    model = "gemini-2.0-flash-001"
    #model = "gemini-2.0-flash-lite"
    response = client.models.generate_content(model=model, contents=messages)
    # Print the response
    print("Response:")
    print(response.text)

    # Print the user prompt, prompt tokens, response tokens, and total token count
    if "--verbose" in optional_args or "-v" in optional_args:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"Total token count: {response.usage_metadata.total_token_count}")

if __name__ == "__main__":
    main()
