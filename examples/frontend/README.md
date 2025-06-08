# Frontend Example

This example demonstrates how to use `twstock` with a small Flask
application. It allows users to query realtime prices by stock code and
renders a candlestick chart using Chart.js.

## Usage

1. Install the required packages:
   ```bash
   python -m pip install -r requirements.txt
   ```
2. Run the application locally:
   ```bash
   python app.py
   ```
3. Open `http://localhost:5000` in your browser and enter a stock code.

### Deploying to Render

在 Render 建立新的 **Web Service**，並將 `Build Command` 設定為：
```bash
pip install -r examples/frontend/requirements.txt
```
`Start Command` 則為：
```bash
python examples/frontend/app.py
```
