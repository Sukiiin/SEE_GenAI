# SEE_GenAI


# Gemini

This project consists of two Streamlit applications that leverage the capabilities of the Gemini AI model provided by Google's GenerativeAI. The Gemini model is a powerful text and image generation model that can be used for various creative and informative purposes.

## Usage
To run the Streamlit app for text generation, execute the following command:

```bash
streamlit run Gemini.py
```

## Configuration

In both apps, you need to enter your API key to authenticate with the Gemini model. The API key can be entered through the Streamlit sidebar. Make sure to enter a valid API key to access the model.

Additionally, you can configure various model parameters to control the generation process.

The parameters are

- **Temperature**: This parameter helps control the randomness of predictions by scaling the logits before applying softmax. A low temperature value (e.g., 0.1) results in less random completions, making the model more confident but also more conservative. On the other hand, a high temperature (e.g., 1.0) produces more diverse and creative outputs, but they might not always make sense.

- **Top_p (also known as nucleus sampling)**: Instead of sampling from the most likely `top_k` tokens, you can sample from the smallest possible set of tokens whose cumulative probability exceeds a certain value, typically 0.9. This dynamic set can increase diversity of the generated text.

- **Top_k**: This parameter is used in top-k sampling. The model will only consider the top `k` most likely predictions at each step. This can prevent the model from generating low probability tokens and make the output more focused.

- **Max_output_tokens**: This is the maximum length of the sequence that will be generated. It's used to control how much text the model generates.

These parameters can be tuned based on the specific requirements of your application to generate the desired output.
