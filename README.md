💡 Hybrid Marketing Assistant

A smart hybrid recommendation system that merges collaborative and content-based filtering to provide personalized product suggestions.
Built with Flask, this system intelligently recommends products for both existing users and new users using a cold-start strategy.

🚀 Features

1.🤝 Hybrid Recommendation Engine – Combines collaborative and content-based methods for higher accuracy.

2.🆕 Cold Start Solution – Collects minimal user preferences (age, gender, category) for new users.

3.📊 Dynamic Recommendations – Displays detailed product info (name, brand, price, rating).

4.🧠 Marketing Insights – Helps understand user behavior for better targeting.

5.💻 Simple UI – Clean HTML interface for user interaction.

🧰 Tech Stack
Component	Technology
Backend 	Flask (Python)
Frontend	HTML, CSS
Data	    CSV files (users.csv, products.csv,new_users.csv)
Logic	    Collaborative + Content-Based Filtering 

🧩 How It Works

1.Existing Users – Enter user ID → system retrieves purchase history → generates hybrid recommendations.

2.New Users – Prompted to answer a few preference questions → data saved in new_users.csv → personalized results shown instantly.

📁 Folder Structure

MARKETING_ASSISTANT/
│
├── templates/
│   └── index.html              # Frontend UI
│
├── app.py                      # Main Flask application
│
├── users.csv                   # Existing user data
├── new_users.csv               # Stores new user info
├── products.csv                # Product details (price, brand, etc.)
├── user_recommendations.csv    # Collaborative results
└── hybrid_user_recommendations.csv  # Final hybrid recommendations


▶️ Run Locally
# Clone repository
git clone https://github.com/<Gopika-R-Official>/Marketing-assistant.git
cd Marketing-assistant

# Run the app
python app.py

🌱 Future Enhancements

Integrate with real-time APIs for product updates
Add sentiment-based feedback to refine recommendations
Deploy on a cloud platform 


👩‍💻 Author
R.Gopika  
Engineering | Machine Learning & Marketing Systems  
🔗 [GitHub](https://github.com/<Gopika-R-Official>)



