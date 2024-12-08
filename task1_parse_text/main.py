from utils import handle_string

if __name__ == "__main__":
    raw_path = "./data/raw_data/raw_real.xlsx"
    district_city_path = "./data/dictrict_city.xlsx"

    df = handle_string.parse_text(raw_path,district_city_path )
    df.to_excel('output.xlsx')


    # Tính số lượng NaN trong mỗi dòng
    nan_count_per_row = df.isna().sum(axis=1)

    # Lọc các dòng có số lượng NaN vượt quá ngưỡng  50%
    threshold = len(df.columns) / 2
    rows_with_too_many_nans = df[nan_count_per_row > threshold]


    # Lọc các dòng không có quá nhiều NaN (số lượng NaN <= ngưỡng)
    rows_without_too_many_nans = df[nan_count_per_row <= threshold]
    rows_without_too_many_nans.to_excel('output.xlsx')


    
    
    print('Dòng dữ liệu nghi ngờ thiếu thông tin')
    print(rows_with_too_many_nans)

    print('Dòng dữ liệu có thể đạt chuẩn')
    print(rows_without_too_many_nans)