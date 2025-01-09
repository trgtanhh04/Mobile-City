# Overview of the Project
Mobile phones are essential tools in the modern world. With diverse brands, models, designs, and prices, analyzing the mobile phone market provides valuable insights into customer needs and market trends in Vietnam.

---

# Project Details

**Topic**: Analyzing the mobile phone market through a mobile phone store (Mobile City) in Vietnam.

**Data Source**: Data was scraped using tools like Selenium and Beautiful Soup from the [Mobile City website](https://mobilecity.vn), a retailer of electronic devices such as phones, computers, components, and accessories.

**Idea**: Conducting a comprehensive data science workflow, including:
- Data collection.
- Data exploration and preprocessing.
- In-depth analysis to interpret issues using data.
- Data modeling: Predicting the price of a mobile phone based on its features.

---

# GitHub Structure

```
├── README.md                                  <- The top-level README for developers using this project.
│
├── data
│   ├── raw_data.csv                              <- Data crawled from website.
│   ├── processed_data.csv                          <- Data after preprocessing.
│   ├── links.csv                          <- Data after preprocessing.
│   ├── new_processed_data.csv                          <- Data after preprocessing.
│
├── notebooks                                  <- Jupyter notebooks.
│   ├── figures                                <- Contain plotly export.
│   │    ├── plot.html                         <- For question about Genre in eda.
│   │    ├── correlation_actual_predict.html   <- For model comparison in score prediction.
│   ├── 0.0-introduction.ipynb                 <- Unimportant!
│   ├── 0.1-introduction.ipynb                 <- Contain project and group information.
│   ├── 1.0-data-collecting.ipynb              <- Notebook for crawling data.
│   ├── 2.0-preprocessing.ipynb                <- Notebook for preprocessing.
│   ├── 3.0-eda.ipynb                          <- Notebook for exploratory data analysis.
│   ├── 4.0-data-modelling.ipynb               <- Notebook for data modelling.
│   ├── 5.0-reflection.ipynb                   <- Contain reflection information of our group and each team member.
│
├── submit                                     <- Folder for submitting Moodle.
│   ├── ...
│                     
├── ...                                        <- Other unimportant files and folders.
```

# How to Run the Project

### **1. Clone the Repository**
First, download the project by cloning it to your local machine:

```bash
git clone https://github.com/trgtanhh04/Mobile-City.git
cd Mobile-City
```

### **2. Set Up the Conda Environment**

- **Create a new Conda environment:**

```bash
conda create -n mobile_city_env python=3.8 -y
conda activate mobile_city_env
```

- **Install required libraries:**

```bash
pip install -r requirements.txt