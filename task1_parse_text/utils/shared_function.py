import pandas as pd
import re

# Get data.
def split_raw_data (path):

    # Get data
    raw_data = pd.read_excel(path)

    # Split data
    real_estate_data = raw_data.iloc[:, :3]
    real_estate_infor = raw_data.iloc[:, 1]
    seller_description = raw_data.iloc[:,3]

    return real_estate_data, real_estate_infor, seller_description


def process_district_city(text, district_city_df):
    """
    Tìm kiếm quận và thành phố từ chuỗi nhập vào bằng cách tham chiếu dữ liệu từ file Excel.
    
    Parameters:
    - text (str): Chuỗi chứa tên quận và thành phố.
    - path (str): Đường dẫn tới file Excel chứa dữ liệu quận và thành phố.

    Returns:
    - tuple: (district_in_text, city_in_text)
    """
    
    # Lấy danh sách giá trị quận và thành phố
    district_values = district_city_df['district'].dropna().unique()
    city_values = district_city_df['city'].dropna().unique()

    district_in_text = None
    city_in_text = None

    # Tìm và loại bỏ quận trong text
    for value in district_values:
        if value in text:
            district_in_text = value.strip()
            break

    # Tìm và thành phố trong text
    for value in city_values:
        if value in text:
            city_in_text = value.strip()
            break

    return district_in_text, city_in_text



























    








