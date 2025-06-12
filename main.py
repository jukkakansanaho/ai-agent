import os
import sys
#import argparse
from dotenv import load_dotenv
from google import genai

contents = ""
if len(sys.argv) < 2:
    print("Error: no arguments. Please provide ai-agent prompt as the first argument.")
    sys.exit(1)
else:
    contents = sys.argv[1]
    print(f"Prompt: {contents}")
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
def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    '''
    Use the client.models.generate_content() method to get a response from the gemini-2.0-flash-001 model! You'll need to use two named parameters:
    model: The model name: gemini-2.0-flash-001 (this one has a generous free tier)
    contents: The prompt to send to the model (a string). Use this prompt:
    "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    In addition to printing the text response, print the number of tokens consumed by the interaction in this format:
    Prompt tokens: X
    Response tokens: Y
    The response has a .usage_metadata property that has both:

    a prompt_token_count property (tokens in the prompt)
    a candidates_token_count property (tokens in the response)
    '''
    model = "gemini-2.0-flash-001"
    #contents = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
    response = client.models.generate_content(model=model, contents=contents)

    print(response.text)
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    print(f"Total token count: {response.usage_metadata.total_token_count}")

    '''
    Response:
    Boot.dev excels as a backend development learning platform due to its hands-on, project-based approach. It emphasizes practical coding from the outset, allowing
    learners to build real-world applications while mastering core concepts through interactive courses and immediate feedback. With structured paths and a focus on
    industry-relevant skills like Go and Python, Boot.dev effectively bridges the gap between theory and practice, making complex topics accessible and preparing stu
    dents for successful careers.

    Prompt tokens: 19
    Response tokens: 89
    '''

if __name__ == "__main__":
    main()
