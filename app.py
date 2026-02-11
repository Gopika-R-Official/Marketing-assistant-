from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

# --- Paths ---
base_dir = os.getcwd()
hybrid_path = os.path.join(base_dir, "hybrid_user_recommendations_with_ratings.csv")
users_path = os.path.join(base_dir, "users.csv")
products_path = os.path.join(base_dir, "products.csv")
new_users_path = os.path.join(base_dir, "new_users.csv")

# --- Load Datasets ---
def load_csv(path, columns):
    try:
        df = pd.read_csv(path)
        print(f"✅ {os.path.basename(path)} loaded.")
        return df
    except FileNotFoundError:
        print(f"❌ {os.path.basename(path)} not found.")
        return pd.DataFrame(columns=columns)

hybrid_df = load_csv(hybrid_path, ["user_id", "recommended_product_id", "product_name", "rating"])
users_df = load_csv(users_path, ["user_id", "age", "gender", "preferred_category"])
products_df = load_csv(products_path, ["product_id", "product_name", "brand", "category", "price_in_inr"])

# ✅ Rename column for consistency
if "price_in_inr" in products_df.columns:
    products_df.rename(columns={"price_in_inr": "price"}, inplace=True)

# --- Merge hybrid + products ---
merged_df = hybrid_df.merge(
    products_df[["product_id", "product_name", "brand", "category", "price"]],
    left_on="recommended_product_id",
    right_on="product_id",
    how="left"
).drop(columns=["product_id"], errors="ignore")

# --- Merge with user info ---
merged_df = merged_df.merge(users_df, on="user_id", how="left")

@app.route("/", methods=["GET", "POST"])
def index():
    user_id = None
    recommendations = None
    new_user = False

    if request.method == "POST":
        user_id = request.form["user_id"].strip()

        if user_id.isdigit():
            user_id = int(user_id)

            # --- Existing User ---
            if user_id in merged_df["user_id"].values:
                user_recs = merged_df[merged_df["user_id"] == user_id]
                recommendations = (
                    user_recs.sort_values(by="rating", ascending=False)
                    .head(10)[["recommended_product_id", "product_name", "category", "brand", "price", "rating"]]
                )

            # --- New User Detected ---
            elif user_id not in users_df["user_id"].values:
                new_user = True

        else:
            recommendations = pd.DataFrame()

    return render_template("index.html", user_id=user_id, recommendations=recommendations, new_user=new_user)


@app.route("/save_preferences", methods=["POST"])
def save_preferences():
    user_id = int(request.form["user_id"])
    age = request.form["age"]
    gender = request.form["gender"]
    preferred_category = request.form["preferred_category"]

    # Save new user data
    new_data = pd.DataFrame([[user_id, age, gender, preferred_category]],
                            columns=["user_id", "age", "gender", "preferred_category"])

    if os.path.exists(new_users_path):
        new_data.to_csv(new_users_path, mode='a', header=False, index=False)
    else:
        new_data.to_csv(new_users_path, index=False)

    # Recommend popular products from that category
    recommendations = (
        products_df[products_df["category"].str.lower() == preferred_category.lower()]
        .head(10)[["product_id", "product_name", "brand", "category", "price"]]
    )
    recommendations["rating"] = "⭐ Popular"

    return render_template("index.html", user_id=user_id, recommendations=recommendations, new_user=False)


if __name__ == "__main__":
    app.run(debug=True)
