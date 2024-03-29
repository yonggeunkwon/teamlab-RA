## 전국 대회 선발 고사

이 문제에서는 0번부터 n - 1번까지 n명의 학생 중 전국 대회에 참여할 수 있는 학생 3명을 선발하는 과정을 다룹니다. 학생들의 등수와 참여 가능 여부가 주어지며, 참여가 가능한 학생들 중에서 가장 높은 등수의 학생 3명을 선발해야 합니다.

### 제한사항

- `rank`의 길이와 `attendance`의 길이는 동일하며, 3에서 100 사이입니다.
- `rank[i]`는 i번 학생의 선발 고사 등수를 의미하며, 1부터 n까지의 정수로 모두 다릅니다.
- `attendance[i]`는 i번 학생의 전국 대회 참석 가능 여부를 나타냅니다.
  - `true`는 참석 가능, `false`는 참석 불가능을 의미합니다.
- `attendance` 배열에서 최소 3개의 원소는 `true`입니다.

### 입출력 예

| rank                      | attendance                             | result |
|---------------------------|-----------------------------------------|--------|
| [3, 7, 2, 5, 4, 6, 1]     | [false, true, true, true, true, false, false] | 20403  |
| [1, 2, 3]                 | [true, true, true]                      | 102    |
| [6, 1, 5, 2, 3, 4]        | [true, false, true, false, false, true] | 50200  |

#### 입출력 예 설명

##### 입출력 예 #1

- 1등은 참석 불가능하므로 2등부터 확인합니다. 2등(2번 학생)은 참석 가능, 4등(4번 학생)과 5등(3번 학생) 또한 참석 가능합니다. 따라서 결과는 10000 × 2 + 100 × 4 + 3 = 20403입니다.

##### 입출력 예 #2

- 1등(0번 학생), 2등(1번 학생), 3등(2번 학생) 모두 참석 가능합니다. 따라서 결과는 10000 × 0 + 100 × 1 + 2 = 102입니다.

##### 입출력 예 #3

- 1등, 2등, 3등 모두 참석 불가능하므로 다음 순위를 확인합니다. 4등(5번 학생), 5등(2번 학생), 6등(0번 학생)은 모두 참석 가능합니다. 따라서 결과는 10000 × 5 + 100 × 2 + 0 = 50200입니다.
