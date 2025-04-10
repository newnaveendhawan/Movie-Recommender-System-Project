
<img src="https://github.com/user-attachments/assets/7b9ee967-d1dc-4921-8a07-0a4255572d04" alt="Project Screenshot" width="800" height="400">
---

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
- **Libraries**: Streamlit, Pandas, Scikit-learn, Pickle, Requests
- **NLP**: Vectorization: CountVectorizer (Bag-of-Words), Stemming: Reduces words to root form
- **Similarity Metric**: Cosine Similarity
- **API**: TMDB (The Movie Database)
- **IDE**: PyCharm
- **Deployment**: Render
- **Large File Handling**: Git LFS

## 🖼️ Screenshot of the Web App
###### Here’s a glimpse of the web app in action:
![Screenshot 2025-04-09 214754](https://github.com/user-attachments/assets/0c514131-118a-497c-a196-66d7eecdaa0d)


## How the Movie Recommender System works
##### 📥 User Interaction

##### 🎬 Selects a Movie from the Dropdown

##### 🔎 System Locates the Movie Index in the Dataset

##### 📊 Retrieves Similarity Scores from Precomputed Matrix

##### 📈 Sorts Scores and Picks Top 5 Similar Movies

##### 🌐 Fetches Posters for Each Movie using TMDB API

##### 🖼 Displays Movie Posters and Titles in Streamlit UI

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

  ## 🚀 Deployment (via Render)

1. Push your project to a GitHub repository.
2. Go to [Render.com](https://render.com) → New Web Service → Connect GitHub Repo.
3. Configure:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `sh setup.sh && streamlit run main.py`
4. Deploy. Your app goes live with a public URL.

> Note: Use **Git LFS** to upload files >100MB (`movie_dict.pkl`, `similarity.pkl`).

## 🧪 Testing
##### - Try selecting various genres: Action, Drama, Romance
##### - Compare system recommendations with IMDb or other engines
##### - Check the correctness of the poster and name mapping
##### - Test UI on different screen sizes (Streamlit handles responsiveness)

## 🔗 Project Resources

- 📁 [Google Drive – All Project Files](https://drive.google.com/drive/folders/1KdxqSE0mEzqfGKzWBFYCdM-CLMpxAteq?usp=drive_link)
- 📝 [Notion Document – Project Notes](https://morning-cast-4fb.notion.site/Movie-Recommender-System-Using-Content-Based-Filtering-1d0c0db6457880b59307fd9cafab0780)
- 🎥 [Live Demo Video: Watch Project in Action](https://drive.google.com/file/d/1uiUpBBcdp4c_dupE-mTkFNbOveQTOVrH/view?usp=drive_link)

## 👨‍💻 About the Author
### **Naveen Dhawan**  
🎓 B.Tech – Data Analytics | Machine Learning  
🔗 [LinkedIn](https://linkedin.com/in/newnaveendhawan)  
💼 [GitHub](https://github.com/newnaveendhawan)
