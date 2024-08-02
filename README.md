# Capital Yatra - AI-Driven Investment Management System

## Overview

Welcome to **Capital Yatra**, an advanced AI-driven investment management system designed to revolutionize your trading and investment strategies. Our platform leverages cutting-edge technologies, including Generative AI, to optimize portfolio allocation, manage risks, analyze real-time and historical market data, automate trading, and provide comprehensive financial education.

## Features

- **Portfolio Optimization**: Utilize advanced algorithms to optimize asset allocation, maximizing returns while minimizing risk.
- **Risk Management**: Implement robust risk management strategies to safeguard investments against market volatility.
- **Real-Time and Historical Data Analysis**: Provide insights from both real-time market data and historical trends to make informed investment decisions.
- **Automated Trading**: Enable automated trading based on predefined criteria and market signals, ensuring timely and accurate trade executions.
- **Financial Knowledge and Education**: Offer comprehensive resources and tools to educate users about financial markets and investment strategies.
- **Generative AI**: Leverage the power of GenAI for predictive analysis, sentiment assessment, personalized recommendations, and more.

## Team

**Team Name**: Sharingan  
**Team Members**:
- Somesh Mishra
- Ayush Kumar Singh
- Deboshruti Mukhopadhyay
- Shruti Shahi

## Project Setup

### Prerequisites

- Python 3.x
- Flask
- yfinance
- backtrader
- Other dependencies as listed in `requirements.txt`

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/yourusername/capitalyatra.git
   cd capitalyatra
   ```
2. ```
   pip install -r requirements.txt
   ```
3. ```
   python app.py
   ```
## Project Structure
```
capitalyatra/
├── static/
│   └── images/
│       ├── apple.png
│       ├── microsoft.png
│       ├── google.png
│       ├── amazon.png
│       └── tesla.png
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```
## API Endpoints

- **Home**: `GET /`
  - Renders the main dashboard.

- **Get Historical Data**: `GET /get_data?ticker=<ticker_symbol>`
  - Fetches historical data for the specified ticker symbol.

- **Execute Trade**: `POST /trade`
  - Executes a trade based on provided criteria.

- **Get Image Path**: `GET /get_image?ticker=<ticker_symbol>`
  - Returns the path of the image associated with the specified ticker symbol.

- **Get Additional Data**: `GET /get_additional_data`
  - Provides additional data such as bullish/bearish scenarios, net profit/loss, volume, and trade suggestions.

## Generative AI Usage

Our platform integrates Generative AI to enhance various aspects of investment management:

- **Predictive Analysis**: Utilize GenAI to forecast market trends and asset performance.
- **Sentiment Assessment**: Analyze market sentiment to gauge investor mood and market direction.
- **Personalized Recommendations**: Provide tailored investment advice and strategy suggestions.

## Contributing

We welcome contributions to improve our project. Please fork the repository, create a new branch, and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any questions or feedback, please contact us at [info@capitalyatra.com](mailto:info@capitalyatra.com) or visit our website [capitalyatra.com](https://capitalyatra.com).

