# 스타일을 지정하기 위한 언어
> 선택하고, 스타일을 지정한다.

- CSS 구문은 선택자를 통해 스타일을 지정할 `HTML 요소를 선택`
- 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
  - 속성 : 어떤 스타일 기능을 변경할지 결정
  - 값 : 어떻게 스타일 기능을 변경할지 결정

## CSS 정의 방법 (내부 참조)
```
h1 {
  color: blue;
  font-size: 15px;
}
```
- 유지보수성, 가독성, 수정용이성
- CSS 적용에는 우선순위가 있다.
- 같은 레벨이라면 나중에 `선언`된 것이 적용된다. 
- id(#), class(.), 태그는 서로 다른 레벨이다.
- id > class > 태그 순으로 우선순위를 가진다.
- 다만 일반적으로 CSS 스타일링은 클래스로만 한다.
- id는 잘 활용하지 않고, JS(자바스크립트)로 개발할 때 보통 활용한다.
- id는 문서에서 1번만 사용된다.

## CSS 기본 스타일
1. 크기 단위
- px (픽셀)
  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적임
- % 
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음 
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - 상속의 영향을 받지 않음
  - 최상위 요소의 사이즈를 기준으로 배수 단위를 가짐

## CSS 적용 우선순위
1. 중요도 : 사용시 주의
- !important
2. 우선 순위
- 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element
3. CSS 파일 로딩 순서

## CSS 원칙
- 모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)
1. Inline -> 한줄 배치
2. Block -> Block 배치

## Box model
1. margin
- 테두리 바깥의 외부 여백
- 배경색을 지정할 수 없다
2. border
- 테두리 영역
3. padding
- 테두리 안쪽의 내부 여백 요소에 적용된 배경색, 이미지는 padding 까지 적용
4. content
- 글이나 이미지 등 요소의 실제 내용

### Box model 구성
- .margin {
  margin: 10px 20px 30px 40px;
}
> 반시계 방향 (상 -> 우 -> 하 -> 좌)

- .border {
  border-width: 2px;
  border-style: dashed;
  border-color: black;
}

- box-sizing
  - 기본적으로 모든 요소의 box-sizing은 content-box
    - padding을 제외한 순수 contents 영역만을 box로 지정
  - 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
    - 그 경우 box-sizing을 border-box로 설정

### 대표적으로 활용되는 display
1. display: block
- 줄바꿈이 일어나는 요소
- 화면 크기 전체의 가로 폭을 차지한다.
- 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
2. display: Inline
- 줄바꿈이 일어나지 않는 요소
- content 너비만큼 가로 폭을 차지한다.
- width, height, margin-top, margin-bottom을 지정할 수 없다. 
- 상하 여백은 line-height로 지정한다.

### CSS position
- 문서 상에서 요소의 위치를 지정
- static: 모든 태그의 기본 값(기준 위치)
  - 일반적인 요소의 배치 순서에 따름(좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치 됨

- 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능
  - relative (상대위치)
    - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)
  
  - absolute (절대위치)
     - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  
  - fixed (고정 위치)
    - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
    - 부모 요소과 관계없이 viewport를 기준으로 이동
      - 스크롤 시에도 항상 같은 곳에 위치
 
  - sticky

### float
- 박스를 왼쪽 혹은 오른쪽으로 이동시켜 텍스트를 포함 인라인 요소들이 주변을 wrapping 하도록 함
- 요소가 Normal flow를 벗어나도록 함

```
.left {
  float: left;
}
```

### Flexbox
- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
- 축
  - 메인 축
  - 교차 축
- 구성 요소
  - Flex Container (부모 요소)
    - display 속성을 flex 혹은 inline-flex로 지정
    ```
    .flex-container {
      display: flex;
    }
    ```
  - Flex Item (자식 요소)
    - 컨테이너에 속해 있는 컨텐츠 (박스)

- flex 속성
  - 배치 설정 : flex-direction
     - row, row-reverse, colume, column-reverse
  - 공간 나누기 : justify-content (main axis)
  - 정렬 : align-items (개별 아이템)