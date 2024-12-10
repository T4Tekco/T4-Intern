from utils import second_parts


def identify_source(final_elements):
    source = None
    for idx, value in enumerate(final_elements):
        value = value.replace(',', '')  # Loại bỏ dấu phẩy nếu có
        if value == "nguồn":  # Tìm vị trí 'nguồn'
            # Duyệt từ vị trí ngay sau 'nguồn' để tìm số
            for po, element in enumerate(final_elements[idx+1:], start=idx+1):
                if element.isdigit():  # Nếu phần tử tiếp theo là số
                    source = ' '.join(final_elements[idx:po])  # Lấy phần tử từ 'nguồn' tới số
                    break 
            break  

    return source

# Get Dc
def identify_dc(final_elements):
    return final_elements[-1]

# Final list
def identify_final_elements_list_2(final_elements):

    negotiable_range = None
    # Components
    phone_number = second_parts.identify_phone_number(final_elements)
    commission = second_parts.identify_commission(final_elements)
    source = identify_source(final_elements)
    dc = identify_dc(final_elements)

    keyword_range = ['nhỏ','đến','trên']
    for word in final_elements:
        word_split = word.strip().split(' ')

        for keyword in keyword_range:
            if keyword in word_split:
                if keyword == 'nhỏ' or keyword =='trên':
                    negotiable_range = keyword + " " + word_split[word_split.index(keyword) + 1]
                else:
                    pass
                    # negotiable_range = word_split[word_split.index(keyword) - 1] + " " + keyword + " " + word_split[word_split.index(keyword) + 1]

    if source is not None:
        source = source.replace('nguồn', '')
    return [phone_number, commission, source, negotiable_range, dc]
