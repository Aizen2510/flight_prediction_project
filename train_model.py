import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import pickle
import os

# Load dữ liệu
df = pd.read_csv('data/flight_data.csv')

# Encode dữ liệu dạng text
label_cols = ['gioi_tinh', 'diem_di', 'diem_den', 'thoi_gian_bay_ua_thich', 'hinh_thuc_thanh_toan']
label_encoders = {}

for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Tách dữ liệu
X = df.drop('tham_gia_chuyen_bay', axis=1)
y = df['tham_gia_chuyen_bay']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Huấn luyện mô hình
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Lưu mô hình và encoders
os.makedirs("model", exist_ok=True)
with open('model/flight_model.pkl', 'wb') as f:
    pickle.dump((model, label_encoders), f)

print("Đã huấn luyện và lưu mô hình thành công.")
