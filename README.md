# Giới thiệu đồ án
Điện thoại là một công cụ không thể thiếu trong cuộc sống hiện đại. Với sự đa dạng về thương hiệu, mẫu mã, thiết kế và giá cả, việc phân tích thị trường điện thoại di động giúp cung cấp những thông tin quan trọng về nhu cầu của khách hàng và xu hướng thị trường tại Việt Nam.
---

# Chi tiết đồ án

**Chủ đề**: Phân tích thị trường điện thoại di động thông qua cửa hàng Mobile City tại Việt Nam.

**Nguồn dữ liệu:** Dữ liệu được thu thập bằng các công cụ như Selenium và Beautiful Soup từ  [Mobile City website](https://mobilecity.vn), một nhà bán lẻ thiết bị điện tử như điện thoại, máy tính, linh kiện và phụ kiện.

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
<p align="center">
  <img src="https://github.com/trgtanhh04/Mobile-City/blob/main/workflow.png" width="60%" alt="Workflow">
</p>

# Quy Trình Xử Lý Dữ Liệu
1. Thu Thập Dữ Liệu:
- Crawler định kỳ chạy theo lịch trình để thu thập dữ liệu về điện thoại từ nhiều nguồn đa dạng. Quá trình này đảm bảo tất cả các nguồn dữ liệu liên quan đều được thu thập một cách đầy đủ.

2. Lưu Trữ Thô:
- Dữ liệu thu thập được ban đầu được lưu trữ dưới dạng csv trong hệ thống tệp cục bộ, tạo thành kho chứa dữ liệu thô cho các bước xử lý tiếp theo.

3. Xử lý và làm sạch dữ liệu:
- Dùng các kỹ thuật phân tích và quan sát, chuẩn hóa dữ liệu theo đúng định dạng, xử lý dữ liệu bị thiếu, bị sai..vv
4. Ứng Dụng:
- API: Xây dựng API cho hệ thống tư vấn điện thoại, cho phép truy vấn dữ liệu theo yêu cầu và đưa ra các sản phẩm tương tự.

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
