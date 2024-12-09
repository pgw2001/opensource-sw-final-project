# Opensource SW Final Project
2024년 2학기, "오픈소스SW의이해" 8조 기말 프로젝트.
<br><br>



## 1. 팀원 🧑‍🤝‍🧑
<table border="1">
  <thead>
    <tr>
      <th>팀원</th>
      <th>학번</th>
      <th>역할</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/pgw2001">
        <img src="https://github.com/user-attachments/assets/f9657b55-cf05-48ff-83a6-278e87cb28c1" width="100px;" alt=""/><br/><sub>박건웅</sub></a><br/>
      <td>20205164</td>
      <td>문서 작성(요구사항 명세서, WBS)</td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/JustHello02">
        <img src="https://github.com/user-attachments/assets/16c8460c-590a-49f0-80c8-b9270edf86af" width="100px;" alt=""/><br/><sub>박성민</sub></a><br/>
      <td>20215155</td>
      <td>문서 작성(화면 설계서), 발표 자료 준비</td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/JooSungEom">
        <img src="https://github.com/user-attachments/assets/f64efb77-88ab-4aec-8092-090eac52fafb" width="100px;" alt=""/><br/><sub>엄주성</sub></a><br/>
      </td>
      <td>20205202</td>
      <td>게임 개발 감독</td>
    </tr>
    <tr>
      <td align="center"><a href="https://github.com/Jinmiru">
        <img src="https://github.com/user-attachments/assets/c5292883-2903-41d2-a1f1-ace700ab6159" width="100px;" alt=""/><br/><sub>정진영</sub></a><br/>
      </td>
      <td>20205252</td>
      <td>프로젝트 계획 및 GitHub Repository 정리</td>
    </tr>
  </tbody>
</table>

**※게임 개발(코드 작성)은 협력 활동 기록을 위해 공동 제작**
<br><br>



## 2. 프로젝트 개요 📋
- 미니 게임들을 모아서 플레이할 수 있도록 **파이썬 & Streamlit**을 사용.
- **파이썬 언어로 개발**을 진행하며, 플레이어와 상호작용 시스템 구축을 위해 **프론트 엔드는 Streamlit**을 사용.
- 랭킹, 업적 기능을 추가하여 플레이어가 게임 플레이에 대한 흥미를 끌어올리도록 구현.
- 플레이 가능한 게임은 실시간으로 계속 추가 예정(2048, 스도쿠 등).
<br>



## 3. 사용방법 🎮
### 3-1. 배포용 Stremalit 링크에 접속하는 경우
1. Streamlit 링크로 이동 - https://opensource-sw-final-project-h27sngpsyhlayqbyxbhytu.streamlit.app/
2. 성공적으로 로딩완료 시, 튜토리얼(게임소개) 화면으로 이동
3. 원하는 게임을 사이드바에서 선택하면, 해당 게임 페이지로 이동
4. 플레이 방법
    - 게임 종류에 따라 **일반 이동키(화살 키) 또는 단축키**로 진행 (추천)
    - 마우스 클릭으로 진행

### 3-2. 설치해서 사용하고자 하는 경우
1. "**<> Code**"를 눌러 나오는 URL을 사용해 `git clone <URL>` 명령어로 파일 다운로드
    - 또는 밑에 "**Download ZIP**"을 눌러 다운로드
2. `pip install -r requirements.txt` 명령어로 필요한 모듈 설치
3. `streamlit run main.py` 명령어로 실행하면 열리는 페이지로 이동
4. 상술한 **3-1**의 2번부터 설명 참고

<br>



## 4. 플레이 화면(Streamlit) 🎮
<img width="1280" alt="플레이 화면 1" src="https://github.com/user-attachments/assets/aedbce9b-77d6-43e3-8a71-7c9987794e48">
<img width="1280" alt="플레이 화면 2" src="https://github.com/user-attachments/assets/f18707b2-112b-4310-9efd-6fd2c20997fa">
<img width="1280" alt="플레이 화면 3" src="https://github.com/user-attachments/assets/42a4fed7-2f9c-46de-b266-00ebeef2f450">
<br><br>



## 5. requirements.txt 📰
```
altair==5.5.0
attrs==24.2.0
blinker==1.9.0
cachetools==5.5.0
certifi==2024.8.30
charset-normalizer==3.4.0
click==8.1.7
colorama==0.4.6
gitdb==4.0.11
GitPython==3.1.43
idna==3.10
Jinja2==3.1.4
jsonschema==4.23.0
jsonschema-specifications==2024.10.1
markdown-it-py==3.0.0
MarkupSafe==3.0.2
mdurl==0.1.2
narwhals==1.16.0
numpy==2.1.3
packaging==24.2
pandas==2.2.3
pillow==11.0.0
protobuf==5.29.1
pyarrow==18.1.0
pydeck==0.9.1
Pygments==2.18.0
python-dateutil==2.9.0.post0
pytz==2024.2
referencing==0.35.1
requests==2.32.3
rich==13.9.4
rpds-py==0.22.3
six==1.17.0
smmap==5.0.1
streamlit==1.40.2
streamlit-shortcuts==0.1.9
tenacity==9.0.0
toml==0.10.2
tornado==6.4.2
typing_extensions==4.12.2
tzdata==2024.2
urllib3==2.2.3
watchdog==6.0.0
```
<br><br>
