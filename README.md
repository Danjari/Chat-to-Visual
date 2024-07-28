# Chat to Visual

## Overview

Welcome to the "Chat to Visual" app! This innovative application allows you to interact with a GPT-4 powered chatbot that not only provides insightful responses but also turns your queries into well-designed and easy-to-understand diagrams.

Simply input your questions, and the app will generate visual diagrams to help you grasp complex concepts quickly and effectively. Whether you're looking to understand a process, an algorithm, or any intricate idea, "Chat to Visual" transforms your queries into clear visual representations, making learning and comprehension a breeze.

## Features

- **Intelligent Responses**: Ask any question, and receive insightful responses from a GPT-4 powered chatbot.
- **Visual Diagrams**: For complex concepts, the chatbot provides visual diagrams using Mermaid syntax.
- **Interactive Interface**: Built with Streamlit, the app ensures a smooth and interactive user experience.

## How to Use

1. **Input Your Question**: Type your question or request into the chat interface.
2. **Receive a Response**: The chatbot processes your query and provides a detailed text response.
3. **View Diagrams**: For technical or complex queries, the chatbot generates and displays a visual diagram to help you understand the concept better.

## Installation

To run the app locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/chat-to-visual.git
    cd chat-to-visual
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the project root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your_openai_api_key_here
    ```

4. **Run the App**:
    ```bash
    streamlit run app.py
    ```

## Dependencies

- `streamlit`
- `openai`
- `python-dotenv`
- `shelve`
- `streamlit-mermaid`

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [OpenAI](https://www.openai.com/)
- [Mermaid](https://mermaid-js.github.io/)

