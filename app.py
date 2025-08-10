import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Dự đoán khách hàng tiềm năng", layout="centered")

# Load mô hình
with open('model/flight_model.pkl', 'rb') as f:
    model, encoders = pickle.load(f)

st.title("✈️ Dự đoán khả năng người dùng tham gia chuyến bay")

# Form nhập liệu
with st.form("input_form"):
    tuoi = st.slider("Tuổi", 18, 65, 30)
    gioi_tinh = st.selectbox("Giới tính", ['Nam', 'Nữ'])
    lich_su_dat_ve = st.slider("Lịch sử đặt vé", 0, 10, 1)
    so_tien_trung_binh = st.number_input("Giá vé trung bình (VND)", min_value=500_000, max_value=5_000_000, value=1_000_000, step=100_000)
    thoi_diem_tim_kiem = st.slider("Tìm kiếm trước (ngày)", 1, 30, 5)
    diem_di = st.selectbox("Điểm đi", ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Nha Trang'])
    diem_den = st.selectbox("Điểm đến", [x for x in ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Nha Trang'] if x != diem_di])
    thoi_gian_bay_ua_thich = st.selectbox("Thời gian bay ưa thích", ['Sáng', 'Chiều', 'Tối'])
    hinh_thuc_thanh_toan = st.selectbox("Hình thức thanh toán", ['Ví điện tử', 'Thẻ tín dụng', 'Chuyển khoản', 'Tiền mặt'])
    click_vao_chuyen_bay = st.selectbox("Click vào chuyến bay?", ['Không', 'Có'])

    submit = st.form_submit_button("Dự đoán")

# Dự đoán
if submit:
    input_data = {
        'tuoi': tuoi,
        'gioi_tinh': encoders['gioi_tinh'].transform([gioi_tinh])[0],
        'lich_su_dat_ve': lich_su_dat_ve,
        'so_tien_trung_binh': so_tien_trung_binh,
        'thoi_diem_tim_kiem': thoi_diem_tim_kiem,
        'diem_di': encoders['diem_di'].transform([diem_di])[0],
        'diem_den': encoders['diem_den'].transform([diem_den])[0],
        'thoi_gian_bay_ua_thich': encoders['thoi_gian_bay_ua_thich'].transform([thoi_gian_bay_ua_thich])[0],
        'hinh_thuc_thanh_toan': encoders['hinh_thuc_thanh_toan'].transform([hinh_thuc_thanh_toan])[0],
        'click_vao_chuyen_bay': 1 if click_vao_chuyen_bay == 'Có' else 0
    }

    df_input = pd.DataFrame([input_data])
    prob = model.predict_proba(df_input)[0][1]
    st.success(f"🚀 Xác suất người dùng sẽ tham gia chuyến bay: **{prob * 100:.2f}%**")
