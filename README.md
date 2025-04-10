![an-aesthetically-pleasing-4k-hd-poster-i_XZdn0WGgR8mpT3D8E-xDQg_nljHz1vCS1e9qe3xsCpLSg (1)](https://github.com/user-attachments/assets/d5ef8398-124d-45a2-bf1c-2ce4b0f46424)
<img src="https://github.com/user-attachments/assets/d5ef8398-124d-45a2-bf1c-2ce4b0f46424" alt="Project Screenshot" width="600" height="400">
----
# 🎬 Movie Recommender System

An interactive content-based movie recommendation system built using **Streamlit**, powered by **cosine similarity** and enriched with **TMDB API** for fetching posters. It analyzes movie metadata like **overview, genres, cast, crew, and keywords** to recommend the top 5 similar movies. Deployed using **Render** via GitHub, with large `.pkl` files handled via **Git LFS**.

---



## ✨ Features

- 🔍 Select any movie and get top 5 content-based recommendations
- 🧠 Uses NLP, stemming, and cosine similarity for similarity scoring
- 🎞 TMDB API used to fetch high-quality movie posters dynamically
- 📊 CountVectorizer used for vectorizing textual features (Bag-of-Words)
- ⚡ Fast & responsive UI built with Streamlit
- 🌐 Live deployment on Render with GitHub integration

---


## 🛠 Tech Stack

- **Language**: Python 3
- **Libraries**: Streamlit, Pandas, Scikit-learn, NLTK, Pickle, Requests
- **Vectorization**: CountVectorizer (Bag-of-Words)
- **Similarity Metric**: Cosine Similarity
- **API**: TMDB (The Movie Database)
- **IDE**: PyCharm
- **Deployment**: Render
- **Large File Handling**: Git LFS

## 🖼️ Screenshot of the Web App
###### Here’s a glimpse of the web app in action:
![Screenshot 2025-04-09 214754](https://github.com/user-attachments/assets/0c514131-118a-497c-a196-66d7eecdaa0d)


  ## 🚀 Deployment (via Render)

1. Push your project to a GitHub repository.
2. Go to [Render.com](https://render.com) → New Web Service → Connect GitHub Repo.
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py`
4. Deploy. Your app goes live with a public URL.

> Note: Use **Git LFS** to upload files >100MB (`movie_dict.pkl`, `similarity.pkl`).

---

## 📁 Project Structure
movie-recommender-system/ 
###### ├── app.py → Streamlit web app script 
###### ├── movie_dict.pkl → Preprocessed movie metadata 
###### ├── similarity.pkl → Precomputed similarity matrix 
###### ├── requirements.txt → All project dependencies 
###### ├── Procfile → For deployment platforms like Render/Heroku 
###### ├── setup.sh → Optional for Heroku (Streamlit config) 
###### └── README.md → Project documentation

## **Naveen Dhawan**  
🎓 B.Tech – Data Analytics | Machine Learning  
🔗 [LinkedIn](https://linkedin.com/in/newnaveendhawan)  
💼 [GitHub](https://github.com/newnaveendhawan)
