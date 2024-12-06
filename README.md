# Time-Series-Sales-Forecasting-with-Flask-Analyze-Predict-Business-Sales-Trends

This project demonstrates how to use time series analysis for sales forecasting by leveraging the power of Facebook’s Prophet library and a Flask-based web interface. The application allows users to input a date range and receive accurate sales forecasts, making it a valuable tool for businesses seeking data-driven decision-making solutions.

Features

	•	Interactive Web Interface: Simple and intuitive interface for selecting date ranges and viewing forecasts.
	•	Prophet Time Series Model: Predict sales trends using Facebook’s robust Prophet library.
	•	Real-time Predictions: Get quick, accurate sales forecasts based on user input.
	•	Scalable Design: Built with Flask, allowing seamless integration into larger systems.

 Project Structure

 time-series-project/
│
├── app.py               # Main Flask application
├── templates/
│   ├── index.html       # Frontend user interface
├── static/
│   ├── styles.css       # Optional: Custom styles for the interface
├── data/
│   ├── sales_data.csv   # Sample dataset for the project
├── model/
│   ├── forecasting_model.pkl  # Serialized Prophet model
│
└── requirements.txt     # Project dependencies


Dataset

The project uses a sample dataset (sales_data.csv) with daily sales data for 20 days. You can replace this file with your own data to customize the forecasting model. Ensure the dataset has two columns:
	1.	Date (ds)
	2.	Sales (y)

 How It Works

	1.	Load the Prophet model with pre-trained sales data.
	2.	Enter the desired start and end dates for forecasting in the web interface.
	3.	The application predicts sales for the given date range and displays the results.

 Technologies Used

	•	Flask: Lightweight Python web framework for creating the user interface.
	•	Prophet: Time series forecasting library by Facebook.
	•	Pandas: Data manipulation and preprocessing.
	•	HTML & CSS: For building the web interface.

 Future Scope

	•	Add support for multiple forecasting models.
	•	Integrate with databases for live data analysis.
	•	Deploy on cloud platforms for production use.


 Contact

If you have any questions or suggestions, feel free to reach out via GitHub or LinkedIn.
