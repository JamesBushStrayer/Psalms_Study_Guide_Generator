import openai
import os
import sys
  
try:
  openai.api_key = os.environ['OPENAI_API_KEY']
except KeyError:
  sys.stderr.write("""
  You haven't set up your API key yet.
  
  If you don't have an API key yet, visit:
  
  https://platform.openai.com/signup

  1. Make an account or sign in
  2. Click "View API Keys" from the top right menu.
  3. Click "Create new secret key"

  Then, open the Secrets Tool and add OPENAI_API_KEY as a secret.
  """)
  exit(1)

psalm = "38"

prompts = (f"Write a very broad and generalized 5 to 6 sentence backgrounder on Psalm {psalm} based on the contextual aspects of the psalm, such as history, culture, and other points of relevance that may aid in the understanding of its origin and purpose.",
# f"Provide the full text of Psalm {psalm} using the King James Version, formatted for organizational clarity.",
# f"Create a study guide for Psalm {psalm} that includes both a brief, one-sentence summary of each main point, an extended summary for each main point, a few questions that challenge the reader's understanding for each main point, and a series of questions that ask the reader to reflect on their own life experience for each main point.",
# f"Divine attributes. Identify the nature and divine attributes of God expressed by Psalm {psalm}. Explain the similarities in as much detail as possible.",
# f"Draw connections between the person and teachings of Jesus Christ and His Apostles and Psalm {psalm}, particularly, as they resonate with him and the themes and main points of the psalm in as much detail as possible. Include supporting Bible verses for every connection made. Also, draw parallels between the words of Jesus and His Apostles and verses in this psalm, if any.",
# f"List all of the psalms that are identical or highly similar to Psalm {psalm}, whether in part or in whole. Explain the similarities in as much detail as possible.",
# f"Answer the Understanding Questions posed in the study guide (but not the Reflective Questions). Just list the questions, followed by the answers.
)

messages = [{"role": "system", "content": content} for content in prompts]

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=messages
)

with open("response.txt", "w") as file:
   for choice in response.choices:
       file.write(str(choice.message.content)+ "\n")


# response = openai.ChatCompletion.create(
#   model="gpt-4",
#   messages=[
#         {"role": "system", "content": prompt_1}
#     ]
# )

print(response)

# # Open the file in write mode
# with open("response.txt", "w") as file:
#     # Write the response to the file
#     file.write(str(response.choices[0].message.content))

