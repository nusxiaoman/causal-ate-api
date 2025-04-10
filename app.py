#####################################################################
#### app.py ####

from flask import Flask, request, jsonify
import pandas as pd
import statsmodels.api as sm

app = Flask(__name__)

@app.route("/estimate_ate", methods=["POST"])
def estimate_ate():
    data = request.get_json()
    df = pd.DataFrame(data)

    X = df[["Treatment_W", "Sustainability_Spending_X"]]
    X = sm.add_constant(X)
    y = df["Engagement_Score_Y"]

    model = sm.OLS(y, X).fit()

    tau = model.params["Treatment_W"]
    with open("output.txt", "w") as f:
        f.write(f"Estimated ATE (tau): {tau}\n")

    result = {
        "alpha": model.params["const"],
        "tau (ATE)": tau,
        "beta": model.params["Sustainability_Spending_X"],
        "p_value_tau": model.pvalues["Treatment_W"]
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
