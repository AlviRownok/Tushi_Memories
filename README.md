# Tushi Memories

**Tushi Memories** is a heartfelt web application where friends, family, and loved ones can share their fond memories and experiences with Tushi. This app allows users to input their personal details and a special memory dedicated to Tushi, creating a growing collection of memories. These memories are stored in a CSV file, which will later be processed to create a unique and special gift for Tushi.

The project is built using **Streamlit** for the interface and provides a fun, retro-inspired design to make the experience enjoyable for users.

## Repository

[https://github.com/AlviRownok/Tushi_Memories](https://github.com/AlviRownok/Tushi_Memories)

## Features

- **User Input Form**: Users can enter:
  - First Name
  - Surname
  - Number of years they've known Tushi
  - A memory dedicated to Tushi (up to 500 words)
  
- **Memory Recording**: Each submission is saved in a CSV file (`tushi_memories.csv`), which appends new entries automatically.

- **Auto Refresh**: After form submission, the input fields are cleared, allowing the next person to submit their entry easily.

- **View Past Entries**: A table at the bottom of the page shows all the memories submitted so far, allowing users to see their entry alongside others.

## Purpose

This project is a personal endeavor dedicated to the love of my life, **Tushi**. It aims to collect cherished memories from everyone who knows and loves her. These memories will later be compiled from the CSV file and turned into a special, sentimental gift for her.

## Tech Stack

- **Streamlit**: A Python framework used to build the user interface and handle form submissions.
- **Pandas**: For storing and managing the CSV file containing user entries.
- **Python**: The primary language used for the application logic.
- **Custom CSS**: Retro-inspired styling to make the app visually appealing and fun.

## Prerequisites

To run the application locally, ensure you have the following installed:

- Python 3.x
- Streamlit (`pip install streamlit`)
- Pandas (`pip install pandas`)

## Installation and Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/AlviRownok/Tushi_Memories.git
   cd Tushi_Memories
   ```

2. **Install dependencies**:
   Install the required Python packages using the following command:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   Start the Streamlit app by running:
   ```bash
   streamlit run app.py
   ```

4. **Access the app**:
   Once the app is running, a new tab will open in your browser where the app can be accessed.

## Application Flow

1. **Initial Screen**: The user is greeted with a custom-styled interface titled "Memories with Tushi."
   
2. **Form Submission**:
   - The user fills out their first name, surname, number of years they've known Tushi, and writes a memory (with a 500-word limit).
   - On submitting the form, the memory is saved to the CSV file.

3. **Auto Refresh**:
   - Once the memory is submitted, the form fields are cleared automatically, making it easy for the next person to contribute.

4. **Display of Entries**:
   - After submission, all the previous entries, including the newly added memory, are displayed at the bottom of the page in a table format.

### CSV File Structure

Each entry is stored in the CSV file named `tushi_memories.csv` in the following format:

| Name   | Surname | Years Known | Memory                             |
|--------|---------|-------------|------------------------------------|
| Alvi   | Rownok  | 5           | Tushi always brightened my day...  |
| John   | Doe     | 2           | She is an amazing friend and...    |

This CSV file continues to grow as more memories are added, providing a comprehensive collection of experiences shared with Tushi.

## Deployment

The application is deployed on **Streamlit Cloud**, making it accessible online for all users who wish to contribute memories. To access the live version, simply visit the deployment link below:

[Streamlit Cloud Deployment Link]()

## Future Enhancements

At this stage, the project is focused solely on memory collection. No additional features are planned for now, but ideas such as memory search and CSV export functionality may be considered in the future.

## How to Contribute

This project is a solo development effort dedicated to Tushi, and external contributions are not needed at the moment. However, if you have feedback or suggestions, feel free to raise an issue in the repository.

## License

This project is licensed under the **Apache License 2.0**. You may freely use, modify, and distribute this project under the terms of the license. For more details, refer to the [LICENSE](LICENSE) file.