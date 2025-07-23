
# 🎂 Birthday Message Creator

An interactive web application built with Streamlit, React, and Tailwind CSS for generating and personalizing birthday messages with various themes.

## ✨ Features

  * **Thematic Templates:** Choose from a variety of beautiful themes like "Floral Spring," "Minimalist Modern," "Neon Cyber," "Vintage Elegant," "Cosmic Galaxy," and "Celebration Party."
  * **Personalized Messages:** Easily customize messages with the recipient's name, sender's name, age (optional), and select a message type (friend, family, colleague, romantic, child) to get auto-generated messages.
  * **Custom Message Input:** Write your own unique message if the auto-generated ones don't quite fit.
  * **Save & Load Messages:** Save your favorite or frequently used birthday messages locally in your browser and load them later.
  * **Copy to Clipboard:** Instantly copy the generated message text for easy sharing.
  * **Download as Image:** Export your personalized birthday card as a PNG image, perfect for sharing on social media or messaging apps.
  * **Responsive Design:** Enjoy a seamless experience on various devices, thanks to Tailwind CSS.

## 🚀 Technologies Used

  * **Streamlit:** For embedding the interactive HTML/React application and serving it as a web app.
  * **React:** For building the dynamic and interactive user interface.
  * **Tailwind CSS:** For rapid and efficient styling, providing a modern and clean look.
  * **Babel Standalone:** To enable JSX compilation directly in the browser without a separate build step.
  * **html2canvas:** To capture and download the generated birthday card as an image.

## 📂 Project Structure

```
.
├── app.py
└── index.html
```

  * `app.py`: The Streamlit application that embeds and serves the `index.html` file.
  * `index.html`: Contains the core React application, including all the UI components, logic, and styling.

## ⚙️ Setup and Installation

### Prerequisites

  * Python 3.7+
  * pip

### Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/vigneshgit2005/Birthday_Message-Generator.git
    cd birthday-message-generator
    ```

2.  **Install Streamlit:**

    ```bash
    pip install streamlit
    ```

3.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

    This command will open the application in your default web browser.

## ✍️ Usage

1.  **Choose a Theme:** Select your preferred design from the "Choose Your Theme" section.
2.  **Enter Details:** Fill in the "Recipient Name," "Your Name," and optionally "Age."
3.  **Select Relationship:** Choose the relationship type to get a relevant auto-generated message, or write your own in the "Custom Message" field.
4.  **Preview:** See your personalized birthday message update in real-time on the right panel.
5.  **Actions:**
      * **Save Message:** Store the current message locally in your browser.
      * **Saved Messages:** View, load, or delete previously saved messages.
      * **Copy Text:** Copy the message content to your clipboard.
      * **Download Image:** Download the rendered birthday card as a PNG image.

## 🤝 Contributing

Contributions are welcome\! If you have suggestions for new features, themes, or improvements, feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/your-feature-name`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add new feature'`).
5.  Push to the branch (`git push origin feature/your-feature-name`).
6.  Open a Pull Request.

## 📄 License

This project is open-sourced under the MIT License. See the `LICENSE` file for more details.

-----
