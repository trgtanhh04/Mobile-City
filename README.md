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

# Cấu trúc dự án

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

# Hệ thống tư vấn điện thoại
Hệ thống yêu cầu người dùng nhập đủ các thông tin về điện thoại mà mình mong muốn, hệ thống sẽ tiếp nhập input và đưa vào xử lý, lable dữ liệu. Áp dụng các thuật toán học máy để tìm ra các sản phẩm điện thoại có độ tương đồng cao nhất mà người dùng mong muốn. Cuối cùng hệ thống sẽ hiển thị những điện thoại mà người dùng mong muốn.
<p align="center">
  <img src=https://github.com/trgtanhh04/Mobile-City/blob/main/img1.png width="60%" alt="Admin Dashboard">
  <img src=https://github.com/trgtanhh04/Mobile-City/blob/main/img2.png width="60%" alt="Client Dashboard">
</p>

# So sánh ba mô hình Machine Learning

## 1. Giới thiệu
Dự án này nhằm so sánh ba mô hình Machine Learning: Logistic Regression, Random Forest và XGBoost. Mục tiêu là đánh giá hiệu suất và chọn ra mô hình tốt nhất dành cho bài toán dự báo.

## 2. Mô hình so sánh

### 2.1 Logistic Regression
- Là một mô hình tháng tuyến đơn giản, dễ hiểu và dễ triển khai.
- Thích hợp với các bài toán dự báo nhị phân.
- Hiệu suất không cao khi dữ liệu phức tạp và không tuyến tính.

### 2.2 Random Forest
- Là mô hình tập hợp cây quyết định, giảm overfitting so với cây quyết định đơn lẻ.
- Không yêu cầu nhiều xử lý dữ liệu, hoạt động tốt trên tập dữ liệu lớn.
- Hiệu suất tốt nhưng có thể chậm hơn so với các mô hình khác.

### 2.3 XGBoost
- Là mô hình boosting dựa trên cây quyết định, tối ưu hóa tốc độ và hiệu suất.
- Xử lý tốt các dữ liệu phức tạp, giảm thiểu overfitting.
- Thường được dùng trong các cuộc thi Machine Learning nhờ hiệu suất vượt trội.

## 3. Kết luận
Sau khi so sánh và đánh giá hiệu suất của ba mô hình, chúng tôi quyết định chọn **XGBoost** do:
- Hiệu suất cao nhất trên tập dữ liệu.
- Giảm overfitting tốt hơn Random Forest.
- Tốc độ nhanh hơn khi dự báo.

Mô hình XGBoost là sự lựa chọn tối ưu cho bài toán này.


# Cách cài đặt project

1. Tải đồ án về máy cá nhân
```bash
git clone https://github.com/trgtanhh04/Mobile-City.git
cd Mobile-City
```

2. Tạo môi trường
```bash
conda create -n mobile_city_env python=3.8 -y
conda activate mobile_city_env
```

3. Tải các thư viện cần thiết.

```bash
pip install -r requirements.txt
```

# Cách chạy project
```bash
streamlit run app.py
```
