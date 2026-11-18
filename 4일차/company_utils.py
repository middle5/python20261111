# 부가가치세율: 세율이 바뀌면 이 줄만 고칩니다
VAT_RATE = 0.1 # 10%

# 공급가액에 부가가치세를 더한 최종 결제 금액 계산
def add_vat(price):
    return int(price * (1 + VAT_RATE))

# 금액을 원화 문자열로 변환
def won(amount):
    return f"{amount:,}원"

# 부가세 금액만 계산하는 함수
def vat_amount(price):
    return int(price * VAT_RATE)
