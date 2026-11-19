# 실습파일만들기3.py : 23번 슬라이드(연습문제) 실습용 파일 만들기
import shutil
from pathlib import Path

desk = Path(__file__).resolve().parent / "바탕화면"
shutil.rmtree(desk, ignore_errors=True)   # 다시 실행하면 처음 상태로
desk.mkdir()

files = [
    "매출_11월.xlsx", "고객명단.csv",                      # 엑셀
    "견적서_A상사.pdf", "계약서.PDF",                      # 문서
    "회의록_1105.docx", "주간보고.hwp",
    "로고.PNG", "현장사진.jpg", "스크린샷_1108.png",        # 이미지
    "자료모음.zip", "메모.txt", "크롬.lnk",                # 정리 대상 아님
]
for name in files:
    (desk / name).write_bytes(b"")

(desk / "프로젝트").mkdir()                              # 하위 폴더 (정리 대상 아님)
(desk / "프로젝트" / "일정표.xlsx").write_bytes(b"")

print("완료: 파일", len(files), "개, 폴더 1개")