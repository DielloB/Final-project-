 # Currency Converter Project

## Introduction

The Currency Converter Project is an online application implemented using Flask that makes it convenient for users to convert amounts between two currencies seamlessly. Leveraging a live exchange rate API, the application guarantees accurate and seamless currency conversions. With a focus on a simple user interface, it provides an effortless experience for individuals, businesses, and tourists who need speedy conversions.

## Purpose of the Project

As the world becomes more globalized, having the power to exchange currencies quickly and efficiently is a must. This project will develop an easy-to-use and lightweight currency converter that pulls live exchange rates, enabling users to make sound financial choices. From traveling overseas to international shopping, or tracking currency fluctuations, this application is a trusted solution.

## Features

The Currency Converter Project incorporates a number of major features:

- Source and Target Currency Choice: The user has the option to choose from a wide range of currencies using a basic dropdown list.
- Real-Time Exchange Rate Fetching: The application fetches the latest exchange rates from an external API to perform accurate conversions.
- Immediate Display of the Converted Amount: Once the amount and the source and target currencies are entered, the converted amount is shown immediately.
- Simple and Clean User Interface: The web interface is developed with CSS for a seamless and user-friendly experience.
- Error Handling and Validation: The system easily handles the incorrect inputs and API failures to make it seamless to use.
- Unit Testing: An independent test file ensures the main functionalities are in good working condition.

---

## Installation Guide

For installation and running the Currency Converter Project, we followed these steps:

### 1. Clone the Repository

Begin by cloning the project repository from GitHub using the following command:

```bash
git clone <repository_link>
cd <folder_name>
```

### 2. Create a Virtual Environment (Optional)

Using a virtual environment effectively handles dependencies:

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

Start the application with the following command:

```bash
python project.py
```

### 5. Access the Web Interface

Once the server has been started, open a web browser and go to:

```
http://127.0.0.1:5000
```

---

## Project Structure

The project structure follows a clean directory organization:

```
???? Project  
│-- project.py          # Flask main application
│-- templates/
│   └── index.html      # Frontend user interface
│-- static/
```
│   └── style.css       # CSS styles
│-- test_project.py     # Pytest unit tests
│-- requirements.txt    # Python package requirements
│-- README.md           # Project doc
```

---

## Code Overview

The `project.py` script contains the main logic to fetch exchange rates, handle user input, and render the web page. The steps involved are:

1. Fetching Real-Time Exchange Rates: The application sends a request to a currency exchange API.
2. Handling User Input: The user selects source and target currencies, enters an amount, and submits the form.
3. Calculating the Converted Amount: The fetched exchange rate is utilized to perform the conversion.
4. Displaying the Results: The result amount is shown on the interface to the user.

---

## Running Tests

Unit tests are included in `test_project.py` to verify the accuracy of the application. To run the tests, use:

```bash
pytest test_project.py
```

The tests include:
- Successful currency conversions
- Invalid input scenarios
- Failing API requests
- Edge cases like converting zero or the same currency

---

## Dependencies

The following Python libraries need to be installed for the project:

- Flask – To build the web application
- requests – To fetch exchange rates from an API
- pytest – To run unit tests

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## Possible Improvements

There are several ways to improve and expand the project:

1. Add More Currencies: Add more currencies, so more people can use our program
2.Historical Exchange Rates: Allow users to view past exchange rates for trend analysis.
3. Visual Representation of Data: Include charts to represent changes in currencies.
4. User Accounts & Conversion History: Add authentication to save user conversion history.
5. Multi-Language Support: Provide the interface in various languages to cater to more users.
6. Mobile Optimization: Include a responsive design for mobile support.

---

## Challenges Faced

While developing, we have encountered the following challenges:

- API Rate Limits: There are certain free exchange rate APIs with limited requests that require optimization.
- Error Handling: Handling invalid input and API non-availability was important for user experience.
- Maintaining the UI Clean: Creating an easy-to-use interface that provides a seamless user experience required careful design choices.

---

## Authors

Diello Barry and Diallo Oumou developed this project as a hands-on tutorial on Flask-based web development.

---

## Conclusion

The Currency Converter Project provides an easy and efficient way of performing live currency conversions. With an easy-to-use interface, live data retrieval, and good error handling, it is an excellent learning tool as well as a useful application for everyday financial needs.

Welcome to our project!



