# 실습파일만들기2.py : 19번 슬라이드(사례 ②) 실습용 현장 사진 만들기
import os, shutil
from datetime import datetime
from pathlib import Path

photos = Path(__file__).resolve().parent / "현장사진"
shutil.rmtree(photos, ignore_errors=True)   # 다시 실행하면 처음 상태로
photos.mkdir()

# 현장 사진 12장 (수정한 날짜 = 촬영일)
days = [datetime(2026, 11, 6)] * 4 + [datetime(2026, 11, 7)] * 5 + [datetime(2026, 11, 8)] * 3
for i, day in enumerate(days, 1):
    f = photos / f"IMG_{i:04d}.jpg"
    f.write_bytes(b"")
    os.utime(f, (day.timestamp(), day.timestamp()))

(photos / "촬영메모.txt").write_text("정리 대상이 아닌 파일", encoding="utf-8")
print("완료: 현장사진 12장")