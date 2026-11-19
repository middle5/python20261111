# 실습파일만들기1.py : 10번 슬라이드 실습용 거래명세서 만들기
import shutil
from pathlib import Path
from openpyxl import Workbook

base = Path(__file__).resolve().parent / "거래명세서"
shutil.rmtree(base, ignore_errors=True)   # 다시 실행하면 처음 상태로
base.mkdir()

files = [
    ("20261103", "A상사"), ("20261103", "B물산"), ("20261104", "A상사"),
    ("20261104", "C유통"), ("20261105", "B물산"), ("20261105", "D테크"),
    ("20261106", "A상사"), ("20261106", "C유통"), ("20261107", "B물산"),
]

for day, client in files:
    wb = Workbook()
    ws = wb.active
    ws.append(["거래일자", day])
    ws.append(["거래처", client])
    ws.append(["품목", "수량", "단가"])
    ws.append(["A4 복사용지", 5, 5200])
    wb.save(base / f"거래명세서_{day}_{client}.xlsx")

(base / "메모.txt").write_text("정리 대상이 아닌 파일", encoding="utf-8")
print("완료:", len(files), "개")