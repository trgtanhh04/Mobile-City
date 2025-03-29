# import streamlit as st
# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler
# from sklearn.metrics.pairwise import cosine_similarity
# import difflib
# import pickle
# from collections import Counter

# # Load dữ liệu
# df = pd.read_pickle("E:\Mobile City\models\phone_data.pkl")

# # Các thuộc tính sử dụng để tìm điện thoại tương đồng
# feature_cols = [
#     "thoi_gian_bao_hanh", "danh_gia", "so_luong_binh_luan", "gia_moi", "ram",
#     "bo_nho_trong", "dung_luong_pin", "kich_thuoc_man_hinh", "tan_so_quet",
#     "so_the_sim", "cong_suat_sac", "do_phan_giai_cam_sau", "do_phan_giai_cam_truoc"
# ]

# # Chuẩn hóa dữ liệu thuộc tính
# scaler = StandardScaler()
# normalized_feature = scaler.fit_transform(df[feature_cols])

# # Load mô hình Cosine Similarity theo thuộc tính
# with open("E:\Mobile City\models\cosine_similarity_attribute.pkl", "rb") as f:
#     model_data = pickle.load(f)
#     similarity_attribute = model_data["cosine_sim"]
#     ten_list = model_data["ten_list"]

# def recommend_by_name_and_attributes(user_input):
#     input_name = user_input.get("ten", None)

#     # Bước 1: Tìm sản phẩm có tên gần giống
#     similar_phone_indices = []
#     if input_name:
#         closest_match = difflib.get_close_matches(input_name, ten_list, n=1, cutoff=0.6)
#         if closest_match:
#             phone_index = ten_list.index(closest_match[0])
#             similar_phone_indices = np.argsort(similarity_attribute[phone_index])[::-1][:5]
    
#     # Bước 2: Tìm theo thuộc tính
#     user_input_features = {k: float(v) for k, v in user_input.items() if k in feature_cols}
#     if user_input_features:
#         user_df = pd.DataFrame([user_input_features], columns=feature_cols).fillna(0)
#         user_vector = scaler.transform(user_df)
#         similarity_scores = cosine_similarity(user_vector, normalized_feature)[0]
#         attribute_indices = np.argsort(similarity_scores)[::-1][:5]
#     else:
#         attribute_indices = []

#     # Bước 3: Kết hợp hai danh sách
#     combined_scores = Counter()
#     for idx in similar_phone_indices:
#         combined_scores[idx] += 1
#     for idx in attribute_indices:
#         combined_scores[idx] += 1

#     sorted_combined = sorted(combined_scores.keys(), key=lambda x: -combined_scores[x])
#     valid_indices = [i for i in sorted_combined[:5] if i in df.index]

#     if not valid_indices:
#         return "Không tìm thấy sản phẩm phù hợp!"

#     result_data = df.loc[valid_indices, ["ten", "gia_moi", "ram", "bo_nho_trong", "dung_luong_pin", "danh_gia"]]
#     return result_data

# # Tạo giao diện người dùng bằng streamlit
# st.title('Hệ thống gợi ý điện thoại')

# # Nhập thông tin điện thoại cần tìm
# input_name = st.text_input("Tên sản phẩm (ví dụ: Samsung Galaxy):")
# gia_moi = st.number_input("Giá mới:", min_value=0, value=7000000)
# ram = st.number_input("Ram (GB):", min_value=1, value=8)
# bo_nho_trong = st.number_input("Bộ nhớ trong (GB):", min_value=1, value=128)
# dung_luong_pin = st.number_input("Dung lượng pin (mAh):", min_value=1000, value=5000)
# danh_gia = st.number_input("Đánh giá (1-5):", min_value=1.0, max_value=5.0, value=4.5, step=0.1)

# # Nút gợi ý sản phẩm
# if st.button('Gợi ý sản phẩm'):
#     user_input = {
#         "ten": input_name,
#         "gia_moi": gia_moi,
#         "ram": ram,
#         "bo_nho_trong": bo_nho_trong,
#         "dung_luong_pin": dung_luong_pin,
#         "danh_gia": danh_gia
#     }
    
#     recommendations = recommend_by_name_and_attributes(user_input)
    
#     if isinstance(recommendations, str):
#         st.write(recommendations)
#     else:
#         st.write(recommendations)
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import difflib
import pickle
from collections import Counter

# Load dữ liệu
df = pd.read_pickle("E:\Mobile City\models\phone_data.pkl")

# Các thuộc tính sử dụng để tìm điện thoại tương đồng
feature_cols = [
    "thoi_gian_bao_hanh", "danh_gia", "so_luong_binh_luan", "gia_moi", "ram",
    "bo_nho_trong", "dung_luong_pin", "kich_thuoc_man_hinh", "tan_so_quet",
    "so_the_sim", "cong_suat_sac", "do_phan_giai_cam_sau", "do_phan_giai_cam_truoc"
]

# Chuẩn hóa dữ liệu thuộc tính
scaler = StandardScaler()
normalized_feature = scaler.fit_transform(df[feature_cols])

# Load mô hình Cosine Similarity theo thuộc tính
with open("E:\Mobile City\models\cosine_similarity_attribute.pkl", "rb") as f:
    model_data = pickle.load(f)
    similarity_attribute = model_data["cosine_sim"]
    ten_list = model_data["ten_list"]

def recommend_by_name_and_attributes(user_input):
    input_name = user_input.get("ten", None)

    # Bước 1: Tìm sản phẩm có tên gần giống
    similar_phone_indices = []
    if input_name:
        closest_match = difflib.get_close_matches(input_name, ten_list, n=1, cutoff=0.6)
        if closest_match:
            phone_index = ten_list.index(closest_match[0])
            similar_phone_indices = np.argsort(similarity_attribute[phone_index])[::-1][:5]
    
    # Bước 2: Tìm theo thuộc tính
    user_input_features = {k: float(v) for k, v in user_input.items() if k in feature_cols}
    if user_input_features:
        user_df = pd.DataFrame([user_input_features], columns=feature_cols).fillna(0)
        user_vector = scaler.transform(user_df)
        similarity_scores = cosine_similarity(user_vector, normalized_feature)[0]
        attribute_indices = np.argsort(similarity_scores)[::-1][:5]
    else:
        attribute_indices = []

    # Bước 3: Kết hợp hai danh sách
    combined_scores = Counter()
    for idx in similar_phone_indices:
        combined_scores[idx] += 1
    for idx in attribute_indices:
        combined_scores[idx] += 1

    sorted_combined = sorted(combined_scores.keys(), key=lambda x: -combined_scores[x])
    valid_indices = [i for i in sorted_combined[:5] if i in df.index]

    if not valid_indices:
        return "Không tìm thấy sản phẩm phù hợp!"

    result_data = df.loc[valid_indices, ["ten", "gia_moi", "ram", "bo_nho_trong", "dung_luong_pin", "danh_gia"]]
    return result_data

# Tạo giao diện người dùng bằng streamlit
st.set_page_config(page_title='Hệ thống gợi ý điện thoại', layout='wide')

# Tiêu đề và mô tả
st.title('Hệ thống Gợi ý Sản phẩm Điện thoại')
st.markdown("""
    **Chọn các thông tin dưới đây để hệ thống gợi ý các sản phẩm phù hợp với yêu cầu của bạn.**
    Tìm kiếm sản phẩm dựa trên tên hoặc các thuộc tính như giá, RAM, bộ nhớ, dung lượng pin và đánh giá.
""")

# Chia layout thành các cột để nhập thông tin
col1, col2 = st.columns([2, 3])

with col1:
    input_name = st.text_input("Tên sản phẩm (ví dụ: Samsung Galaxy):")

with col2:
    gia_moi = st.number_input("Giá mới:", min_value=0, value=7000000)
    ram = st.number_input("Ram (GB):", min_value=1, value=8)
    bo_nho_trong = st.number_input("Bộ nhớ trong (GB):", min_value=1, value=128)
    dung_luong_pin = st.number_input("Dung lượng pin (mAh):", min_value=1000, value=5000)
    danh_gia = st.number_input("Đánh giá (1-5):", min_value=1.0, max_value=5.0, value=4.5, step=0.1)

# Nút gợi ý sản phẩm
if st.button('Gợi ý sản phẩm'):
    user_input = {
        "ten": input_name,
        "gia_moi": gia_moi,
        "ram": ram,
        "bo_nho_trong": bo_nho_trong,
        "dung_luong_pin": dung_luong_pin,
        "danh_gia": danh_gia
    }
    
    recommendations = recommend_by_name_and_attributes(user_input)
    
    if isinstance(recommendations, str):
        st.error(recommendations)
    else:
        st.success("Các sản phẩm gợi ý:")
        st.dataframe(recommendations)

