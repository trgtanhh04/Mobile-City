# Đồ án cuối kỳ môn Nhập môn khoa học dữ liệu
## Thông tin nhóm 2

| **STT** | **Họ và tên** | **MSSV** | **Ghi chú** | 
|-------|---------------|---------|----|
| 1     | Bùi Đình Bảo | 21120201 | |
| 2     | Trương Tiến Anh | 22120017 |  |
| 3     | Lê Nguyễn Gia Bảo | 22120023 |    |
| 4     | Nguyễn Hữu Bền | 22120029 |  *  |
| 5     | Đoàn Minh Cường | 22120043 |  |

## Đóng góp công việc

| **STT** | **Họ và tên** | **MSSV** | **Đóng góp** | **Đánh giá** |
|-------|---------------|---------|--------| -------|
| 1     | Bùi Đình Bảo | 21120201 | Thực hiện tạo template cho đồ án, thu thập dữ liệu, tiền xử lý dữ liệu, cố vấn cho các thành viên còn lại trong những công việc khác. | 100% |
| 2     | Trương Tiến Anh | 22120017 | Thực hiện phân tích 2 vấn đề chuyên sâu giải thích được bằng dữ liệu, thực hiện mô hình dữ liệu, viết báo cáo đồ án. | 100% |
| 3     | Lê Nguyễn Gia Bảo | 22120023 |  Thực hiện phân tích 2 vấn đề chuyên sâu giải thích được bằng dữ liệu, thực hiện mô hình dữ liệu, đánh giá mô hình.  | 100% |
| 4     | Nguyễn Hữu Bền | 22120029 |  Tổ chức không gian làm việc cho nhóm, thực hiện khám phá và xử lí dữ liệu, tổng hợp, nhận xét và đánh giá bài làm các thành viên còn lại trong nhóm, quản lí tiến độ công việc, viết báo cáo.  | 100% |
| 5     | Đoàn Minh Cường | 22120043 | Thực hiện phân tích 2 vấn đề chuyên sâu giải thích được bằng dữ liệu, thực hiện mô hình dữ liệu, làm bài thuyết trình cho nhóm. | 100% |

---
# Tổng quan đề tài

Đây là đồ án môn học Nhập môn Khoa học dữ liệu, do thầy Lê Ngọc Thành giảng dạy và thầy Lê Nhựt Nam hướng dẫn. Đồ án được thực hiện xuyên suốt trong quá trình học tập như đã đề ra trong proposal.

Nhận thấy điện thoại di động là một dụng cụ cần thiết trong thế giới hiện đại ngày nay, điện thoại rất đa dạng từ hãng sản xuất, mẫu mã, kiểu thiết đến giá. Việc phân tích này giúp đưa ra nhiều cái nhìn về thị trường điện thoại ở Việt Nam.
---
# Cụ thể đồ án

**Chủ đề**: Phân tích về thị trường điện thoại di động thông qua một cửa hàng điện thoại (Mobile City) ở Việt Nam.

**Nguồn dữ liệu**: Dữ liệu được cào bằng các công cụ Selenium, Beautiful Soup ở trang web Mobile City, là một cửa hàng thiết bị điện tử như: điện thoại, máy tính, linh kiện và phụ kiện điện thoại.
Link: mobilecity.vn

**Ý tưởng**: Thực hiện một quy trình nghiên cứu khao học dữ liệu, bao gồm:
- Thu thập dữ liệu.
- Khám phá và tiền xử lí dữ liệu.
- Phân tích các vấn đề chuyên sâu, giải thích được bằng dữ liệu.
- Mô hình hóa dữ liệu: Dự đoán giá của một chiếc điện thoại dựa trên những đặc trưng của nó.

---
# Tổ chức GitHub
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

----
## Các khó khăn gặp phải 
- Tìm nguồn dữ liệu hợp lí, mang tính thực tế cao, còn giới hạn về nhiều ý nghĩa, các kĩ năng cào dữ liệu.
- Xử lý dữ liệu phức tạp, xử lý nhiều với dạng chuỗi để chọn ra được nhiều đặc trưng có ý nghĩa phân tích.
- Gặp khó khăn trong vấn đề số hóa các kiểu dữ liệu phân loại.

## Những bài học và kinh nghiệm rút ra 
- Cải thiện được kĩ năng phân tích dữ liệu, có nhiều cái nhìn về cách phân tích dựa trên dữ liệu.
- Bổ sung kĩ năng cào dữ liệu và chọn ra các thuộc tính có ý nghĩa.
- Sử dụng đa dạng và kết hợp nhiều thưu viện bổ trợ cho quá trình phân tích.

## Nếu có thêm thời gian
- Suy nghĩ thêm về các câu hỏi phân tích có thể trả lời được bằng dữ liệu.
- Làm thêm mô hình gợi ý sản phẩm dựa trên nhu cầu của người mua.

----

# Không gian làm việc
- Sử dụng git và github để quản lý version. Sử dụng google meet, docs, sheets, zalo để bàn bạc, ghi chú và tổ chức công việc.
## Trello 

## Canva 
- Link:
---
# Tham khảo
- Link: