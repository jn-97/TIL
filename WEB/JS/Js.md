# Java Script

## addEventListener

- 두 개의 입력 값을 받는 메서드로, 각각 수신할 이벤트 유형(click)을 가리키는 문자열과, 이벤트가 발생하면 실행할 코드
- querySelectorAll() 함수를 사용하면 현재 페이지 내의 모든 버튼을 선택할 수 있다. 

```
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}

```

1. 선언
  1. var : 변수를 선언. 추가로 동시에 값을 초기화
  2. let : 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화. (변경 가능)
  3. const : 블록 스코프 읽기 전용 상수를 선언. (변경 불가능)

2. 변수
> `var x = 42` , `let y = 13`

- 할당되지 않은 변수

```
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```

```
var myArray = [];
if (!myArray[0]) myFunction();
```

3. 제어문

- 블록문 : 명령문들을 그룹으로 묶을 수 있고, 제어 흐름 명령문과 많이 사용된다. (if, for, while)

```
while (x < 10) {
  x++; // 블록문
}
```

- 조건문

```
if (condition) {
  statement_1;
} else {
  statement_2;
}
```

- switch문

```
switch (expression) {
  case label_1:
    statements_1;
    break;
  case label_2:
    statements_2;
    break;
    …
  default:
    statements_default;
}
```

- throw문

```
throw 'Error2'; // String
throw 42; // Number
throw true; // Boolean
throw {
  toString: function () {
    return '저는 객체예요';
  },
};
```

- try...catch문

```
function getMonthName(mo) {
  mo = mo - 1; // 배열 인덱스에 맞춰 월 조절 (1 = Jan, 12 = Dec)
  let months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
  if (months[mo]) {
    return months[mo];
  } else {
    throw 'InvalidMonthNo'; // 여기서 throw 키워드 사용
  }
}

try {
  // 시도할 명령문
  monthName = getMonthName(myMonth); // 예외가 발생할 수 있는 함수
} catch (e) {
  monthName = 'unknown';
  logMyErrors(e); // 오류 처리기에 예외 객체 전달
}
```

4. 함수

```
function square(number) {
  return number * number;
}
```