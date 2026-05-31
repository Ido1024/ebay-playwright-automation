import re


class StringUtils:

    @staticmethod
    def extract_float_number(text: str) -> float:
        if not text:
            raise ValueError("The provided text is empty or None")
        clean_text = re.sub(r'[^0-9.]', '', text)
        if clean_text:
            return float(clean_text)
        raise ValueError(f"No numeric value found in text: '{text}'")
