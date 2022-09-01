# 웹 사이트의 구성 요소
> HTML(구조), CSS(표현), Javascript(동작)

- html : 문서의 최상위(root) 요소
- head : 문서 메타데이터 요소
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- body : 문서 본문 요소
  - 실제 화면 구성과 관련된 내용


```
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>Document</title>
</head>
<body>

</body>
</html>
```

## 요소(element)
- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 내용이 없는 태그들도 존재 (닫는 태그가 없음)
  - ex. br(띄어쓰기), hr(수평선), img, input, link, meta
- 요소는 중첩될 수 있음
  - 요소는 중첩을 통해 하나의 문서를 구조화

## 속성(attribute)
> <a href="https://google.com"></a>
- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공
- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관없이 사용 가능한 속성들도 있음 -> HTML Global Attribute

### HTML Global Attribute
- 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성
  - id : 문서 전체에서 유일한 고유 식별자 지정
  - class : 공백으로 구분된 해당 요소의 클래스의 목록
  - style : inline 스타일

### DOM(Documet Object Model) 트리
- 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공
  - ex. <h1> 태그의 부모 태그는 <body> 태그이고, <h1>과 <li>는 형제관계