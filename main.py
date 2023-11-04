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

psalms = ("40", "10", "12", "23", "35", "38", "41", "88", "139", "141")
for psalm in psalms:
  filename = f"Psalm_{psalm}.txt"
  conversation_history = []
  prompts = (
    f"Write a 5 to 6 sentence introduction to the spiritual and emotional elements of Psalm {psalm}, and try to connect its meaning and purpose with that of Christian faith.",
    f"Provide the full text of Psalm {psalm} using the King James Version, formatted for organizational clarity.",
    f"Create a study guide for Psalm {psalm} that includes both a brief, one-sentence summary of each main point along with the Bible verses they correspond to (be sure to cover every verse in the psalm; do not call the summary “main point”; include the verses being summarized at the end), an extended summary for each main point (do not label the extended summary),  questions that challenge the reader's understanding of each main point (label the challenge questions, “EVALUATE”; omit the colon), and a few questions that ask the reader to reflect on their own life experience for each main point (label the reflection questions, “REFLECT”; omit the colon). Provide answers to the challenge questions, but not the questions for reflection.",
    f"Describe all the ways Psalm {psalm} embodies or reflects God’s nature in two sections: 1. divine (incommunicable) attributes; and, 2. communicable  attributes. Include biblical references, if applicable.",
    f"Relate the person and teachings of Jesus Christ and Psalm {psalm}, particularly, as the pertain to the gospel. Include supporting Bible verses for every connection made, especially if there is a match between the words of Jesus and verses in this psalm.",
    f"List all of the psalms that are identical or highly similar to Psalm {psalm}, whether in part or in whole. Explain the similarities in as much detail as possible."
  )

  for prompt in prompts:
    conversation_history.append({"role": "user", "content": prompt})
    response = openai.ChatCompletion.create(
      model="gpt-4",
      messages=conversation_history,
 #     max_tokens=400,
      temperature=1,
      top_p=1,
      n=3
    )
    # Append the AI's response to the conversation history
    conversation_history.append({
      "role":
      "user",
      "content":
      response.choices[0].message["content"]
    })

    # Optional: Print the conversation as it goes
    print(str(f"User: {prompt}") +
    '\n\n')
    print(
      str(f"AI: {response.choices[0].message['content']}") +
      '\n\n-------------------------\n\n')
    # print(str(response.choices[0].message.content) + '\n\n-------------------------\n\n')
    # # Open the file in write mode
    with open(filename, "a") as file:
      # Write the response to the file
      file.write(
        str(response.choices[0].message.content) +
        '\n\n-------------------------\n\n')
