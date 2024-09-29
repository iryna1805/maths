from flask import Flask, request, Response
import json

app = Flask(__name__)


def calculate_line_equation(x1, y1, x2, y2):
    if x1 == x2:
        return {"error": "Пряма є вертикальною, її рівняння не може бути у вигляді y = mx + b."}

    m = (y2 - y1) / (x1 - x2)
    b = y1 - m * x1
    return {"equation": f"y = {m}x + {b}"}


@app.route('/', methods=['POST'])
def get_line_equation():
    try:
        data = request.get_json()

        x1 = float(data.get("x1"))
        y1 = float(data.get("y1"))
        x2 = float(data.get("x2"))
        y2 = float(data.get("y2"))

        if None in [x1, y1, x2, y2]:
            return {"error": "Необхідно передати координати двох точок: x1, y1, x2, y2."}, 400

        result = calculate_line_equation(x1, y1, x2, y2)

        return result, 200  

    except Exception as e:
        return {"error": str(e)}, 400


if __name__ == '__main__':
    app.run(debug=True)
