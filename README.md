 # Currency Converter Project

## Introduction

The Currency Converter Project is a web application built using Flask that enables users to convert amounts between different currencies seamlessly. By leveraging a real-time exchange rate API, this application ensures accurate and efficient currency conversions. Designed with a user-friendly interface, it provides an intuitive experience for individuals, businesses, and travelers needing quick conversions.

## Purpose of the Project

In an increasingly globalized world, the ability to convert currencies quickly and accurately is essential. This project aims to create a lightweight and accessible currency converter that retrieves real-time exchange rates, allowing users to make informed financial decisions. Whether someone is traveling abroad, making international purchases, or monitoring currency trends, this application provides a reliable solution.

## Features

The Currency Converter Project includes several core features:

- Selection of Source and Target Currency: Users can choose from a wide range of currencies using an intuitive dropdown menu.
- Real-Time Currency Conversion: The application fetches the latest exchange rates from an external API to perform accurate conversions.
- Instant Display of Conversion Results: Once the amount and currencies are selected, the converted amount appears immediately.
- Simple and Elegant User Interface: The web interface is designed with CSS for a clean and user-friendly experience.
- Error Handling and Validation: The system manages incorrect inputs and API failures gracefully to ensure smooth operation.
- Unit Testing: A dedicated testing file ensures the core functionalities work as expected.

---

## Installation Guide

To set up and run the Currency Converter Project, we followed these steps:

### 1. Clone the Repository

Begin by cloning the project repository from GitHub using the following command:

```bash
git clone <repository_link>
cd <folder_name>
```

### 2. Create a Virtual Environment (Recommended)

Using a virtual environment helps manage dependencies efficiently:

```bash
python -m venv venv  
source venv/bin/activate  
venv\Scripts\activate  
```

### 3. Install Dependencies

Install the required dependencies by running:

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

Start the application with the command:

```bash
python project.py
```

### 5. Access the Web Interface

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000
```

---

## Project Structure

The project follows a well-organized directory structure:

```
📂 Project  
│-- project.py          # Main Flask application  
│-- templates/  
│   └── index.html      # Frontend user interface  
│-- static/  
│   ├── style.css       # CSS styling  
│-- test_project.py     # Unit tests using pytest  
│-- requirements.txt    # Python dependencies  
│-- README.md           # Project documentation  
```

---

## Code Overview

The `project.py` file contains the main logic for fetching exchange rates, handling user input, and rendering the web page. The workflow consists of:

1. Fetching Real-Time Exchange Rates: The application sends a request to a currency exchange API.
2. Processing User Input: The user selects source and target currencies, enters an amount, and submits the form.
3. Calculating the Converted Amount: The fetched exchange rate is applied to perform the conversion.
4. Displaying the Results: The calculated amount is displayed on the interface for the user.

---

## Running Tests

To ensure the accuracy of the application, unit tests are provided in `test_project.py`. Run the tests using:

```bash
pytest test_project.py
```

These tests cover various scenarios, including:
- Valid currency conversions
- Handling invalid input cases
- API request failures
- Edge cases such as converting zero or the same currency

---

## Dependencies

The following Python libraries are required for the project:

- Flask – For building the web application
- requests – For fetching exchange rates from an API
- pytest – For running unit tests

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Potential Enhancements

There are several ways to improve and expand the project:

1. Historical Exchange Rates: Allow users to view past exchange rates for trend analysis.
2. Graphical Data Representation: Integrate charts to visualize currency fluctuations.
3. User Accounts & Conversion History: Implement authentication to save user conversion history.
4. Multi-Language Support: Enable the interface in multiple languages for broader accessibility.
5. Mobile Optimization: Ensure a responsive design that works well on mobile devices.

---

## Challenges Faced

During development, we encountered several challenges:

- API Rate Limits: Some free exchange rate APIs impose request limits, requiring optimization.
- Error Handling: Managing invalid inputs and API downtime was crucial for user experience.
- Ensuring a Clean UI: Creating an intuitive interface that provides a seamless user experience required thoughtful design choices.

---

## Authors

This project was developed by Diello Barry and Diallo Oumou as a practical demonstration of Flask-based web development.

If you have any feedback, suggestions, or would like to contribute, feel free to reach out!

---

## Conclusion

The Currency Converter Project provides an easy and efficient way to perform real-time currency conversions. With a clean user interface, real-time data fetching, and robust error handling, it serves as an excellent learning tool and a useful application for everyday financial needs.

Thank you for exploring our project!

