# WiFi Test Application

This project is a WiFi testing tool designed to help users diagnose and analyze the performance of their WiFi network. The application provides essential information like signal strength, speed, and connectivity status, helping users identify potential issues and optimize their WiFi setup.

## Features

- **Signal Strength Monitoring**: Real-time updates on WiFi signal strength.
- **Speed Test**: Measures download, upload, and ping to evaluate WiFi speed.
- **Connectivity Analysis**: Provides information on network stability and any detected issues.
- **Network Information**: Displays SSID, BSSID, IP address, and other network details.

## Technologies Used

- **Python**: Backend logic and network analysis.
- **Tkinter**: GUI for desktop interface.
- **Requests**: For speed testing by connecting to public servers.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/username/WiFiTestApp.git
   cd WiFiTestApp
   ```

2. **Install Dependencies**:
   Make sure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   ```bash
   python wifi_test.py
   ```

## Usage

- **Start the Application**: Run the script to launch the GUI.
- **Perform Tests**: Use the provided buttons to perform speed tests or view network information.
- **Analyze Results**: The application will display the test results in an easy-to-read format.

## Troubleshooting

- **Python Errors**: Ensure all dependencies are installed correctly by running `pip install -r requirements.txt`.
- **Network Connection Issues**: Verify your WiFi is connected and working before running the tests.

## License

This project is licensed under the MIT License.
