# SEE_GenAI


# Gemini

This project consists of two Streamlit applications that leverage the capabilities of the Gemini AI model provided by Google's GenerativeAI. The Gemini model is a powerful text and image generation model that can be used for various creative and informative purposes.

## Table of Contents
  - [Installation](#installation)
  - [Usage](#usage)
  - [Text Generation](#text-generation)
  - [Text and Image Generation](#text-and-image-generation)
  - [Configuration](#configuration)
## Installation

1. Clone the repository:

```bash
git clone https://github.com/Sukiiin/SEE_GenAI.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage
To run the Streamlit app for text generation, execute the following command:

```bash
streamlit run Gemini.py
```

## Configuration

In both apps, you need to enter your API key to authenticate with the Gemini model. The API key can be entered through the Streamlit sidebar. Make sure to enter a valid API key to access the model.

Additionally, you can configure various model parameters such as temperature, top_p, top_k, and max_output_tokens to control the generation process.
