import pandas as pd
import re

# Get data.

def import_district_city_data(path):
    district_city = pd.read_excel(path)
    return district_city


def split_raw_data (path):

    # Get data
    raw_data = pd.read_excel(path)

    # Split data
    real_estate_data = raw_data.iloc[:, :3]
    real_estate_infor = raw_data.iloc[:, 1]
    seller_description = raw_data.iloc[:,3]

    return real_estate_data, real_estate_infor, seller_description


# Find city & district  from string
def find_district_city_in_text(text, geo, column):

    values = geo[column].unique()
    for value in values:
        if value in text:
            # Remove element from string
            text = text.replace(value + " ", '').strip()
            return value, text
    return None, text

# split district_city string
def split_district_city(text, geo):
    district_in_text = None
    city_in_text = None

    district_in_text, text = find_district_city_in_text(text, geo, 'district')
    city_in_text, text = find_district_city_in_text(text, geo, 'city')

    if district_in_text is None:
        pass

    if city_in_text is None:
        pass

    return district_in_text, city_in_text

def identify_elements_after_ty(sp_list, location_ty):

    unit = sp_list[location_ty]
    price = sp_list[location_ty-1]
    nums_room = sp_list[location_ty-2]
    area = sp_list[location_ty-4]
    if area.isalpha() or re.findall(r"[^\w\s/]", area):
        area = sp_list[location_ty-3]

    # Find number of floors
    nums_floor_with_t = None
    for element in sp_list:
        if element.startswith('T') and element[0:].isdigit():
            nums_floor_with_t = element
            break

    if nums_floor_with_t is None:
        nums_floor = sp_list[location_ty-3]
    else:
        nums_floor = nums_floor_with_t

    return area, nums_floor, nums_room, price, unit


























    








