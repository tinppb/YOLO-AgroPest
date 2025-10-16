import pandas as pd

# Đọc file Excel
file_path = r"D:/Yolo1/vdv_U18_Nam.xlsx"
df = pd.read_excel(file_path)

# Chuẩn hóa tên cột: bỏ khoảng trắng, đưa về chữ thường
df.columns = df.columns.str.strip().str.lower()

# Kiểm tra tên cột
print("Các cột có trong file:", df.columns)

# Lọc các VĐV tham gia U18 và giới tính Nam
if "giai" in df.columns and "giới tính" in df.columns:
    u18_nam = df[
        (df["giai"].str.contains("U18", case=False, na=False)) &
        (df["giới tính"].str.strip().str.lower() == "nam")
    ]

    # Xuất ra file Excel mới
    output_file = "vdv_U18_Nam.xlsx"
    u18_nam.to_excel(output_file, index=False)
    print(f"Đã lọc xong VĐV U18 Nam, lưu vào {output_file}")
else:
    print("⚠️ Không tìm thấy cột 'giai' hoặc 'giới tính'. Hãy kiểm tra lại tên cột trong file Excel.")
