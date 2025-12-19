연습 문제 (Exercises)
각 연습 문제에 대해 Cursor를 사용하여 현재 할 일 추출기 애플리케이션에 지정된 개선 사항을 구현하는 데 도움을 받으세요.

과제를 수행하면서 writeup.md를 사용하여 진행 상황을 문서화하세요. 사용한 프롬프트와 본인 또는 Cursor가 변경한 내용을 반드시 포함하세요. writeup.md의 내용을 기준으로 채점할 예정입니다. 또한 코드 변경 사항을 문서화하기 위해 코드 전체에 주석을 포함해 주세요.

TODO 1: 새로운 기능 스캐폴딩 (Scaffold a New Feature)

현재 사전 정의된 휴리스틱을 사용하여 할 일 항목을 추출하는 week2/app/services/extract.py의 기존 extract_action_items() 함수를 분석하세요.

여러분의 과제는 Ollama를 활용하여 거대 언어 모델(LLM)을 통해 할 일 항목 추출을 수행하는 LLM 기반 대안인 extract_action_items_llm()을 구현하는 것입니다.

몇 가지 팁:

구조화된 출력(예: 문자열의 JSON 배열)을 생성하려면 다음 문서를 참조하세요: https://ollama.com/blog/structured-outputs

사용 가능한 Ollama 모델을 찾아보려면 다음 문서를 참조하세요: https://ollama.com/library. 더 큰 모델은 리소스를 더 많이 소모하므로 작은 모델부터 시작하세요. 모델을 가져와 실행하려면: ollama run {MODEL_NAME}

TODO 2: 단위 테스트 추가 (Add Unit Tests)

week2/tests/test_extract.py에 다양한 입력(예: 글머리 기호 목록, 키워드 접두사가 있는 줄, 빈 입력)을 다루는 extract_action_items_llm()에 대한 단위 테스트를 작성하세요.

TODO 3: 명확성을 위한 기존 코드 리팩토링 (Refactor Existing Code for Clarity)

잘 정의된 API 계약/스키마, 데이터베이스 계층 정리, 앱 수명 주기/구성, 오류 처리에 중점을 두고 백엔드 코드를 리팩토링하세요.

TODO 4: 에이전트 모드를 사용하여 작은 작업 자동화 (Use Agentic Mode to Automate Small Tasks)

LLM 기반 추출을 새로운 엔드포인트로 통합하세요. 프론트엔드를 업데이트하여 "Extract LLM" 버튼을 포함시키고, 이 버튼을 클릭하면 새 엔드포인트를 통해 추출 프로세스가 트리거되도록 하세요.

모든 메모를 가져오는 하나의 최종 엔드포인트를 노출하세요. 프론트엔드를 업데이트하여 "List Notes" 버튼을 포함시키고, 이 버튼을 클릭하면 메모들을 가져와 표시하도록 하세요.

TODO 5: 코드베이스에서 README 생성 (Generate a README from the Codebase)

학습 목표: 학생들은 AI가 어떻게 코드베이스를 내부적으로 검사하고 문서를 자동으로 생성하는지 배우며, 코드 맥락을 파싱하고 사람이 읽을 수 있는 형태로 번역하는 Cursor의 능력을 확인합니다.

Cursor를 사용하여 현재 코드베이스를 분석하고 잘 구조화된 README.md 파일을 생성하세요. README에는 최소한 다음 내용이 포함되어야 합니다:

프로젝트에 대한 간략한 개요

프로젝트 설정 및 실행 방법

API 엔드포인트 및 기능

테스트 스위트 실행 지침

결과물 (Deliverables)
제공된 지침에 따라 week2/writeup.md를 작성하세요. 모든 변경 사항이 코드베이스에 문서화되어 있는지 확인하세요.

평가 기준 (총 100점) (Evaluation rubric (100 pts total))
1-5 부분당 20점 (생성된 코드에 10점, 각 프롬프트에 10점).

📄 writeup.md 번역

Week 2 작성 (Week 2 Write-up)

지침 (INSTRUCTIONS)
이 파일의 모든 TODO를 작성하세요.

제출 세부 정보 (SUBMISSION DETAILS)
이름: TODO

SUNet ID: TODO

인용(Citations): TODO

이 과제를 수행하는 데 약 TODO 시간이 걸렸습니다.

귀하의 답변 (YOUR RESPONSES)
각 연습 문제에 대해 답변을 생성하는 데 사용한 프롬프트와 생성된 응답의 위치를 포함해 주세요. 코드에서 생성된 부분이 어디인지 문서화하는 주석을 명확하게 추가해 주세요.

연습 문제 1: 새로운 기능 스캐폴딩 (Exercise 1: Scaffold a New Feature)

프롬프트:

TODO
생성된 코드 스니펫:

TODO: 수정된 모든 코드 파일과 관련 줄 번호를 나열하세요.
연습 문제 2: 단위 테스트 추가 (Exercise 2: Add Unit Tests)

프롬프트:

TODO
생성된 코드 스니펫:

TODO: 수정된 모든 코드 파일과 관련 줄 번호를 나열하세요.
연습 문제 3: 명확성을 위한 기존 코드 리팩토링 (Exercise 3: Refactor Existing Code for Clarity)

프롬프트:

TODO
생성/수정된 코드 스니펫:

TODO: 수정된 모든 코드 파일과 관련 줄 번호를 나열하세요. (여기에는 흩어져 있는 여러 변경 사항이 있을 것으로 예상되므로 가능한 포괄적인 목록을 작성하세요.)
연습 문제 4: 에이전트 모드를 사용하여 작은 작업 자동화 (Exercise 4: Use Agentic Mode to Automate a Small Task)

프롬프트:

TODO
생성된 코드 스니펫:

TODO: 수정된 모든 코드 파일과 관련 줄 번호를 나열하세요.
연습 문제 5: 코드베이스에서 README 생성 (Exercise 5: Generate a README from the Codebase)

프롬프트:

TODO
생성된 코드 스니펫:

TODO: 수정된 모든 코드 파일과 관련 줄 번호를 나열하세요.
제출 지침 (SUBMISSION INSTRUCTIONS)
Command (⌘) + F (또는 Ctrl + F)를 눌러 이 파일에 남아 있는 TODO가 있는지 찾으세요. 결과가 없다면 축하합니다 – 모든 필수 필드를 완료했습니다.

채점을 위해 모든 변경 사항을 원격 저장소(remote repository)에 푸시했는지 확인하세요.

Gradescope를 통해 제출하세요.