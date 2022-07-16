import webbrowser

# HTML 수정 함수
def write(name, desc):
  Element(name).element.innerText = desc

# 하단 버튼 링크 연결 함수
def button(*args):
  link = "https://www.youtube.com/watch?v=xfR0iTh8PSI" # https:// 꼭 붙여야 연결됩니다!
  webbrowser.open(link)

# 배경 색깔 설정 함수
def background(color):
  for i in range(0, 2):
    write("g" + str(i), color[i])

def information(info):
  key = list(info.keys())
  for i in range(0, 4):
    write("a" + str(i), key[i])
    write("b" + str(i), info[key[i]])

# 배경 색깔 설정
colors = ["white", "blue"]
background(colors)

# 이름과 설명, 버튼에 들어갈 글 설정
write("name", "이진식")
write("description", "관천중학교")
write("button", "페이스북")

# 상세설명에 들어갈 제목과 글 설정
informations = {
  "생일": "2/10",
  "좋아하는것": "만화, 건담",
  "싫어하는것": "(빠른)포기?",
  "처음시작한 언어": "파이썬"
}
information(informations)
