## Blog Hub

![enter image description here](/static/images/chatgpt.jpg)

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

### Google Authentication

Certainly, here are the steps to obtain the OAuth 2.0 credentials for Google Authentication:

1. Go to the Google Developers Console:

   Visit the [Google Developers Console](https://console.developers.google.com/) and sign in with your Google account if you're not already signed in.

2. Create a New Project:

   Click on the project dropdown at the top of the page and then click on the "New Project" button to create a new project for your application.

3. Configure the OAuth Consent Screen:

   - Click on "OAuth consent screen" in the left sidebar.
   - Select "External" as the user type and click "Create."
   - Fill in the required fields like "App name," "User support email," and "Developer contact information." You can add more details if needed.
   - Add your authorized domains for the application. For local development, you can add `localhost:5000` as an authorized domain.
   - Specify the scopes needed for your application in the "Scopes for Google APIs" section.
   - Save the changes.

4. Create OAuth 2.0 Client ID:

   - In the left sidebar, click on "Credentials."
   - Click on "Create credentials" and select "OAuth client ID."
   - Choose "Web application" as the application type.
   - Add a name for your OAuth 2.0 client ID.
   - Under "Authorized JavaScript origins," add the URLs from which your application will be making requests. For local development, you can add `http://localhost:5000`.
   - Under "Authorized redirect URIs," add the redirect URL for your application's callback endpoint. For example, if your callback route is `/auth/google/callback`, add `http://localhost:5000/auth/google/callback`.
   - Click "Create" to generate your OAuth 2.0 client ID and client secret.

5. Note Your Client ID and Client Secret:

   After creating the OAuth 2.0 client ID, Google will provide you with a client ID and client secret. Make sure to note these down, as you'll need them to configure your application for Google Authentication.

With these credentials, you can now integrate Google Authentication into your ChatGPT Clone project by using the client ID and client secret in your application's configuration. Make sure to keep these credentials secure and never share them publicly.

The ChatGPT Clone with Voice Input should now be running locally. You can access it by opening a web browser and navigating to http://localhost:5000.

Please replace your-username with your actual GitHub username or the repository URL as needed. Additionally, ensure that you have Python and Git installed on your system before following these steps.

This setup allows you to run the ChatGPT clone with voice input locally and have it interact with the OpenAI GPT-3 API for generating responses.
