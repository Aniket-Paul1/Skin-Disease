# 🩺 AI-Based Skin Disease Detection & Healthcare Recommendation System

## 📌 Project Overview
This project is an AI-powered web application designed to detect common skin diseases from uploaded images and recommend nearby dermatology hospitals based on the user’s location. The system leverages deep learning for image classification and integrates real-time hospital search using Google Places API.

The application aims to assist users in early identification of skin conditions and guide them toward appropriate medical support.

---

## 🎯 Objectives
- To detect skin diseases accurately using deep learning techniques  
- To provide instant disease prediction from uploaded skin images  
- To recommend nearby dermatology hospitals based on user-selected location  
- To create a user-friendly web interface for easy interaction  

---

## 🧠 System Architecture
1. **Image Upload Module** – User uploads a skin image  
2. **CNN-Based Classification Model** – Predicts the skin disease  
3. **Result Analysis Module** – Displays disease name, confidence score, and recommendations  
4. **Location-Based Hospital Finder** – Fetches nearby dermatology hospitals  
5. **Frontend UI** – Interactive dashboard for users  

---

## 🛠️ Technologies Used

### 🔹 Machine Learning & AI
- Convolutional Neural Network (CNN)
- TensorFlow
- skin clip
- Image preprocessing

### 🔹 Backend
- Python
- FastAPI

### 🔹 Frontend
- React.js
- Tailwind CSS


### 🔹 Database & Tools
- Supabase (User & history management)\
- postgresql

---

## 📊 Dataset
- Source: Kaggle  
- Contains labeled images of multiple skin diseases  
- Dataset split into:
  - Training set
  - Validation set
  - Testing set  

Data augmentation was applied to handle class imbalance and improve model performance.

---

## 🚀 Features
- Upload skin image for disease prediction  
- Confidence score for prediction results  
- Location-based dermatology hospital recommendations  
- Real-time hospital availability (Open / Closed status)  
- Responsive and clean UI  
- User scan history tracking  

---

## ⚙️ Installation & Setup

### 🔹 Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
## 🔹 Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

---
## 🔐 Environment Variables

Create a .env file in the backend directory:
```bash
GOOGLE_PLACES_API_KEY=your_google_places_api_key
```
---
## ⚠️ Challenges Faced & Solutions

-Low confidence due to unbalanced dataset
→ Solved using data augmentation techniques

-Generalization beyond trained disease classes
→ Improved model robustness and validation strategy

-API restriction & billing issues
→ Proper API configuration and fallback mechanisms

---
## 📚 Learnings & Skills Gained

-Deep learning model development and optimization

-Image preprocessing and data augmentation

-API integration and backend development

-Frontend-backend communication

-Debugging real-world deployment issues

-Team collaboration and project management

---

## 🔮 Future Enhancements

-Support for more skin disease categories

-Mobile application development

-Doctor–patient consultation feature


---
## 📌 Conclusion

This project successfully demonstrates how artificial intelligence and web technologies can be combined to build a practical healthcare solution. It enhanced our understanding of deep learning, system integration, and real-world problem-solving while creating an impactful and user-friendly application.