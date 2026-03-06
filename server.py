from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from config import SYMBOL_DEFAULT

from services.last_change import get_change
from services.leverage_table import leverage_table
from services.color_detection import get_candle_colors



# Trend Engine Wrapper
# -----------------------------
def check_trend_engine(symbol):


        price, btc_h1_change, btc_d1_change = get_change()
        leverage = leverage_table(price)

        # candle color detection 
        # colors = get_candle_colors()

        return {
            "symbol": symbol,
            "price": round(price),
            "btc_h1_change": f"{btc_h1_change}%",
            "btc_d1_change": f"{btc_d1_change}%",
            "leverage_table": leverage
            # "colors" : colors
        }
        

# -----------------------------
# Flask App
# -----------------------------
app = Flask(__name__)
CORS(app)


# -----------------------------
# API Route
# -----------------------------
@app.route("/api/trend")
def trend_api():
    symbol = request.args.get("symbol", SYMBOL_DEFAULT).upper()

    data = check_trend_engine(symbol)

    # If engine failed, return early
    if "error" in data:
        return jsonify(data)

    return jsonify(data)


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Run App
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)