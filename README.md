#  Email Spam Detection using Machine Learning

##  Project Overview

This project is a Machine Learning-based Email Spam Detection System that predicts whether an email is **Spam** or **Not Spam** using numerical email features.

The project includes:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning Model Training
- Streamlit Web Application
- GitHub Deployment

---

##  Features

- Predicts Spam or Not Spam
- User-friendly Streamlit Interface
- Trained using Scikit-learn
- Cleaned dataset before training
- Easy to use and deploy

---

## 📂 Dataset Features

| Feature | Description |
|---------|-------------|
| Email_Length | Total length of the email |
| Num_Links | Number of links in the email |
| Num_Special_Chars | Number of special characters |
| Capital_Words | Number of capital words |
| Has_Attachment | Whether the email has an attachment |

**Target Variable**

- Spam (0 = Not Spam, 1 = Spam)

---

##  Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 🤖 Machine Learning Models

The following models were trained and compared:

- Logistic Regression
- Naive Bayes
- Decision Tree
- Random Forest

Random Forest was selected as the final model because it achieved the best performance.

---

## 📁 Project Structure

```
Email-Spam-Detection/
│
├── app.py
├── spam_model.pkl
├── requirements.txt
├── README.md
├── email_spam_detection_cleaned.csv
├── Data_Cleaning.ipynb
├── Model_Training.ipynb
```

---

##  Run Locally

Clone the repository

```bash
git clone https://github.com/your-username/Email-Spam-Detection.git
```

Go to project folder

```bash
cd Email-Spam-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit app

```bash
streamlit run app.py
```

---

## 📸 Application

The Streamlit application allows users to enter:

- Email Length
- Number of Links
- Number of Special Characters
- Capital Words
- Attachment Status

and predicts whether the email is Spam or Not Spam.

---

##  Future Improvements

- NLP using TF-IDF
- Email Subject Analysis
- Deep Learning Model
- Deployment on AWS/Render
- Real-time Email Classification

---

##  Author

**Harsh Pratap Singh**

B.Tech CSE Student

Machine Learning & Data Science Enthusiast

GitHub: https://github.com/your-username
