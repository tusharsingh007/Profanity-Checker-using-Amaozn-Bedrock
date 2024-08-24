import streamlit as st
import boto3
import json
import re
from botocore.exceptions import ClientError

# Initialize the Bedrock client
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Specify the model ID
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

def get_claude_response(prompt):
    # Payload format
    native_request = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 512,
        "temperature": 0.5,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    }

    # Convert the native request to JSON.
    request = json.dumps(native_request)

    try:
        # Invoke the model with the request.
        response = client.invoke_model(modelId=model_id, body=request)
        
        # Decode the response body.
        model_response = json.loads(response["body"].read())
        
        # Extract and return the response text.
        response_text = model_response["content"][0]["text"]
        return response_text

    except (ClientError, Exception) as e:
        st.error(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
        return None

def mask_profanity(text, profanity_list):
    # Mask each word in the text if it matches a word in the profanity list.
    words = text.split()
    masked_words = []

    for word in words:
        # Clean the word to match against the profanity list
        clean_word = re.sub(r'[^\w\s]', '', word).lower()
        if clean_word in [profanity.lower() for profanity in profanity_list]:
            masked_words.append('#' * len(word))
        else:
            masked_words.append(word)
    
    return ' '.join(masked_words)

def main():
    st.title("Profanity Checker")
    
    # Take input sentence from the user
    user_sentence = st.text_area("Enter a sentence for profanity checking:")
    
    if st.button("Check Profanity"):
        if user_sentence:
            # Define the prompt for the Claude model
            prompt = f"Analyze the following sentence and identify any profane or offensive words: '{user_sentence}'. The answer should only contain the profane words in a comma-separated single line. Do not include any other information or words."
            
            # Get the response from Claude
            claude_response = get_claude_response(prompt)
            
            if claude_response:
                # Strip punctuation and split by commas
                detected_profanities = [re.sub(r'[^\w\s]', '', word).strip() for word in claude_response.split(",") if word.strip()]
                
                # Mask the detected profanities in the original sentence
                masked_sentence = mask_profanity(user_sentence, detected_profanities)
                
                # Display the original and masked sentence
                st.subheader("Original Sentence")
                st.write(user_sentence)
                
                st.subheader("Masked Sentence")
                st.write(masked_sentence)
                
                st.subheader("Detected Profane Words")
                st.write(detected_profanities)
            else:
                st.error("Failed to get a response from Claude.")
        else:
            st.warning("Please enter a sentence before checking.")
            
if __name__ == "__main__":
    main()
