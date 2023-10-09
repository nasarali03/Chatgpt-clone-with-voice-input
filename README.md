## Blog Hub

![enter image description here](/static/images/lugx.png)

Welcome to the ChatGPT Clone with Voice Input project! This project aims to provide a conversational AI experience similar to OpenAI's GPT-3, with the added capability of accepting voice input. Users can interact with the AI using text or speech, making it a versatile and user-friendly tool for various applications. The database is design in such a way that all the questions and the responses from the chatbt are stores in the database. When the user enter the prompt it first search for it inthe database, when it is not in the database then it call the API. This reduces our API calls.
<br>
Connect your database accordingly.
Make sure that the document name in the MongoDB URI and inside the code must be same.

### Built With

- ![HTML](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

<br>
 <a href="https://github.com/othneildrew/Best-README-Template">
    
  </a>
<br>

### Installation

To run the ChatGPT Clone with Voice Input locally, you'll need to set up the project and integrate it with the OpenAI GPT-3 API. Follow these steps to get started:

1. Clone this repository to your local machine using Git:
   ```sh
   git clone https://github.com/your-username/chatgpt-voice-clone.git
   ```
2. Change directory to the project folder:

   ```sh
   cd chatgpt-voice-clone
   ```

3. Sign up for an OpenAI GPT-3 API key if you haven't already. You can do this by visiting the <a href="https://openai.com/">OpenAI website.</a>

4. Place your API key in the code as required.

5. Install the required Python packages:
   Install all the packages with the help of "pip".

6. Start the application:
   ```sh
   python app.py
   ```

The ChatGPT Clone with Voice Input should now be running locally. You can access it by opening a web browser and navigating to http://localhost:5000.

Please replace your-username with your actual GitHub username or the repository URL as needed. Additionally, ensure that you have Python and Git installed on your system before following these steps.

This setup allows you to run the ChatGPT clone with voice input locally and have it interact with the OpenAI GPT-3 API for generating responses.
