## 문자열 겹쳐쓰기

문자열 `my_string`, `overwrite_string`과 정수 `s`가 주어질 때, `my_string`의 인덱스 `s`부터 `overwrite_string`의 길이만큼을 `overwrite_string`으로 대체하는 문제입니다. 수정된 문자열을 반환하는 `solution` 함수를 작성합니다.

### 제한사항

- `my_string`과 `overwrite_string`은 숫자와 알파벳으로 구성됩니다.
- `overwrite_string`의 길이는 최소 1이며 `my_string`의 길이를 초과하지 않습니다. `my_string`의 최대 길이는 1,000입니다.
- `s`는 0부터 `my_string`의 길이에서 `overwrite_string`의 길이를 뺀 값까지 가능합니다.

### 입출력 예

| my_string       | overwrite_string | s  | result           |
|-----------------|------------------|----|------------------|
| "He11oWor1d"    | "lloWorl"        | 2  | "HelloWorld"     |
| "Program29b8UYP"| "merS123"        | 7  | "ProgrammerS123" |

#### 입출력 예 설명

##### 입출력 예 #1

- `my_string` "He11oWor1d"에서 인덱스 2부터 "lloWorl"의 길이만큼인 "11oWor1"을 "lloWorl"로 대체하여 "HelloWorld"를 반환합니다.

##### 입출력 예 #2

- `my_string` "Program29b8UYP"에서 인덱스 7부터 "merS123"의 길이만큼인 "29b8UYP"을 "merS123"로 대체하여 "ProgrammerS123"를 반환합니다.
