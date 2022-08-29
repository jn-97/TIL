## Git 

### $ git status
HEAD detached from 7dceb20

> Detached HEAD란 HEAD가 브랜치를 통해 간접적으로 commit을 가리키지 않고, 직접 커밋을 가리키는 것을 말한다.

#### $ git reflog

> 내 HEAD가 이동했던 히스토리를 통해 이전 commit을 찾아 다시 가볼 수 있다.

#### git checkout -b <new branch name>

> 깃이 권장하는 방법이기도 하고 이를 위해 브랜치 만드는 비용(저장공간이나 컴퓨팅 파워 등)도 저렴하다. 커밋은 브랜치에 하고 혹시 모르는 사이에 detached HEAD가 된 커밋은 브랜치를 따로 만들거나 기존 브랜치에 변경사항을 이동하도록 하자.

