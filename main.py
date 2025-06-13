import os
import sys
#import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Prepare the client
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
user_prompt = ""

# Handle arguments
if len(sys.argv) < 2:
    print("Error: no arguments. Please provide ai-agent prompt as the first argument.")
    sys.exit(1)
else:
    user_prompt = sys.argv[1]
    print(f"Prompt: {user_prompt}")

# Prepare the messages
messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]

'''
# Alternative way to handle arguments with argparse
#
parser = argparse.ArgumentParser(description="Generate content using Google Gemini AI")
parser.add_argument(
    "prompt",
    type=str,
    #required=True,
    help="The prompt to send to the model (a string)."
)
args = parser.parse_args()
contents = args.prompt
'''
# Main function
def main():
    # Generate the response
    model = "gemini-2.0-flash-001"
    response = client.models.generate_content(model=model, contents=messages)
    # Print the response
    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Total token count: {response.usage_metadata.total_token_count}")

if __name__ == "__main__":
    main()
