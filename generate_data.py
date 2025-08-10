import pandas as pd
import numpy as np
import random

np.random.seed(42)

genders = ['Nam', 'Nữ']
cities = ['Hà Nội', 'TP.HCM', 'Đà Nẵng', 'Nha Trang']
times_of_day = ['Sáng', 'Chiều', 'Tối']
payment_methods = ['Ví điện tử', 'Thẻ tín dụng', 'Chuyển khoản', 'Tiền mặt']

data = []

for _ in range(1000):
    tuoi = np.random.randint(18, 65)
    gioi_tinh = random.choice(genders)
    lich_su_dat_ve = np.random.poisson(2)
    so_tien_trung_binh = np.random.randint(500_000, 5_000_000)
    thoi_diem_tim_kiem = np.random.randint(1, 30)
    diem_di = random.choice(cities)
    diem_den = random.choice([c for c in cities if c != diem_di])
    thoi_gian_bay_ua_thich = random.choice(times_of_day)
    hinh_thuc_thanh_toan = random.choice(payment_methods)
    click_vao_chuyen_bay = np.random.choice([0, 1], p=[0.3, 0.7])

    tham_gia_chuyen_bay = 1 if (lich_su_dat_ve > 1 and click_vao_chuyen_bay == 1 and thoi_diem_tim_kiem < 10) else 0
    if np.random.rand() < 0.05:
        tham_gia_chuyen_bay = 1 - tham_gia_chuyen_bay

    data.append([
        tuoi, gioi_tinh, lich_su_dat_ve, so_tien_trung_binh,
        thoi_diem_tim_kiem, diem_di, diem_den, thoi_gian_bay_ua_thich,
        hinh_thuc_thanh_toan, click_vao_chuyen_bay, tham_gia_chuyen_bay
    ])

columns = [
    'tuoi', 'gioi_tinh', 'lich_su_dat_ve', 'so_tien_trung_binh',
    'thoi_diem_tim_kiem', 'diem_di', 'diem_den', 'thoi_gian_bay_ua_thich',
    'hinh_thuc_thanh_toan', 'click_vao_chuyen_bay', 'tham_gia_chuyen_bay'
]

df = pd.DataFrame(data, columns=columns)
df.to_csv('data/flight_data.csv', index=False)
print("✅ Đã tạo xong file flight_data.csv")
