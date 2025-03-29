import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from sklearn.feature_extraction.text import CountVectorizer

# Load dữ liệu
df = pd.read_csv("../data/cleaned_data.csv")

# Các cột đặc trưng để tính toán
feature_cols = [
    "thoi_gian_bao_hanh", "danh_gia", "so_luong_binh_luan", "gia_moi", "ram",
    "bo_nho_trong", "dung_luong_pin", "kich_thuoc_man_hinh", "tan_so_quet",
    "so_the_sim", "cong_suat_sac", "do_phan_giai_cam_sau", "do_phan_giai_cam_truoc"
]

# Chuẩn hóa dữ liệu
scaler = StandardScaler()
normalized_feature = scaler.fit_transform(df[feature_cols])

# Tính Cosine Similarity
similarity_attribute = cosine_similarity(normalized_feature)

with open("../models/cosine_similarity_attribute.pkl", "wb") as f:
    pickle.dump({"cosine_sim": similarity_attribute, "ten_list": df["ten"].tolist()}, f)

df.to_pickle("../models/phone_data.pkl")
