# Giới thiệu đồ án
Điện thoại là một công cụ không thể thiếu trong cuộc sống hiện đại. Với sự đa dạng về thương hiệu, mẫu mã, thiết kế và giá cả, việc phân tích thị trường điện thoại di động giúp cung cấp những thông tin quan trọng về nhu cầu của khách hàng và xu hướng thị trường tại Việt Nam.
---

# Chi tiết đồ án

**Topic**: Phân tích thị trường điện thoại di động thông qua cửa hàng Mobile City tại Việt Nam.
**Data Source**: Nguồn dữ liệu: Dữ liệu được thu thập bằng các công cụ như Selenium và Beautiful Soup từ  [Mobile City website](https://mobilecity.vn), một nhà bán lẻ thiết bị điện tử như điện thoại, máy tính, linh kiện và phụ kiện.

**Idea**: Conducting a comprehensive data science workflow, including:
- Thu thập dữ liệu.
- Khám phá và tiền xử lý dữ liệu.
- Phân tích chuyên sâu để rút ra các vấn đề từ dữ liệu.
- Xây dựng mô hình dự đoán giá điện thoại dựa trên các đặc điểm của sản phẩm.
- Xây dựng mô hình đề xuất điện thoại dựa trên yêu cầu của người dùng.
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

# Diagram
![Workflow](https://github.com/trgtanhh04/Mobile-City/blob/main/workflow.png)


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
