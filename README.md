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

