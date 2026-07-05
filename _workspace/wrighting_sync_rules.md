# Codex-wrighting 연동 운영 규칙

이 문서는 로컬 luckyapt 프로젝트와 wrighting 작품 **「대기업 경리과장이 아파트에 위장취업했다」**를 함께 운용하기 위한 연결 규칙이다.

## 기본 연결

- 로컬 프로젝트: `C:/aegis_dx/reference/luckyapt`
- wrighting projectId: `6197e79b-dabe-4727-857e-1ac84dcc0064`
- 로컬 매핑 원장: `_workspace/.wrighting_map.json`
- 로컬 에이전트 지침: `AGENTS.md`, `CLAUDE.md`
- wrighting 대응 item id: `2cf057af-1275-4627-bdb4-0be3dd42c8be`

## 동기화 원칙

- 회차, 설정, 인물, 플롯, 검수, 윤문, 투고용 문서 작업은 로컬 파일과 wrighting item 양쪽에 반영한다.
- 로컬 파일을 수정할 때는 `_workspace/.wrighting_map.json`에서 대응 item id를 확인한다.
- 새 wrighting 문서를 만들면 로컬 매핑 원장에도 상대경로와 item id를 추가한다.
- wrighting은 제목 칸이 따로 있으므로, 로컬 마크다운을 wrighting document 본문에 반영할 때는 맨 앞 `# 제목` 줄과 그 직후 빈 줄을 제거하고 본문만 올린다.
- 내용 충돌 시 로컬 `_workspace/00_INDEX.md`의 정본 위계를 우선하되, 충돌과 선택 근거를 작업 결과에 남긴다.
- 개인정보가 섞인 원천 소재는 양쪽 모두에서 가명화, 합성, 각색한 허구 형태로만 반영한다.

## 현재 도구 기록

현재 Codex 세션의 MCP 도구 목록은 지연 로드될 수 있다. Wrighting 도구가 보이지 않아도 곧바로 "도구 없음"으로 판단하지 말고, 먼저 `tool_search`로 `wrighting MCP tools resolve_project find_items get_document patch_document create_document`를 검색해 `mcp__wrighting` 네임스페이스를 노출한다.

필수 확인 순서는 다음과 같다.

1. `wrighting_status`로 서버 상태가 `ok`인지 확인한다.
2. `resolve_project(projectId="6197e79b-dabe-4727-857e-1ac84dcc0064")`로 작품 연결을 확인한다.
3. `_workspace/.wrighting_map.json`에서 로컬 상대경로와 item id 매핑을 확인한다.
4. 매핑이 있으면 `get_document(itemId)`로 기존 본문을 읽고, `patch_document`의 `expectedText` 또는 exact-match patch로 반영한다.
5. 매핑이 없으면 `find_items`로 기존 문서를 찾는다. 대상이 없으면 `create_document`로 새 문서를 만들고 `_workspace/.wrighting_map.json`에 상대경로와 item id를 추가한다.
6. 작업 결과에는 반영된 item id와 미동기 항목을 반드시 남긴다.

위 검색과 상태 확인을 모두 실행했는데도 `mcp__wrighting` 도구가 노출되지 않거나 필요한 생성/패치 도구가 없을 때만 미동기로 처리한다. 이 경우에는 어떤 도구가 없었는지 도구명까지 적는다.

2026-07-05 동기화 절차 보강

- 원인: Codex 세션의 Wrighting MCP 도구가 지연 로드 상태였는데, 도구 검색을 먼저 하지 않아 "도구 없음"으로 잘못 보고한 사례가 있었다.
- 조치: 모든 Wrighting 동기화 작업 전 `tool_search` → `wrighting_status` → `resolve_project` → 매핑 확인 → 읽기/패치/생성 → 결과 보고 순서를 필수화한다.
- 기준 도구: `wrighting_status`, `resolve_project`, `find_items`, `get_document`, `patch_document`, `create_document`.

동기화 메모 — 2026-07-03 1~52화 대화 AI 패턴 검수

- 로컬 검수 산출물: `_workspace/reviews/dialogue_ai_pattern_audit_ep_001_052.md`
- 보조 동기화 메모: `_workspace/wrighting_sync/2026-07-03_dialogue_ai_pattern_audit_ep_001_052_sync_note.md`
- 결론: 1~52화 전체가 AI스럽게 규칙적이라고 보기는 어렵지만, 26~36화, 39~43화, 50~52화에서 민원 응대와 기준화 대화가 "접수 → 공감 → 기준 → 처리/확인 예정" 순서로 반복되는 경향이 있다.
- 우선 수정 후보: 27화, 30화, 35~36화, 39~43화, 50~52화.
- 윤문 방향: 문장 치환보다 현장 인물의 끼어들기, 말끝 흐림, 생활어, 작은 실패를 넣어 공문체 리듬을 깨는 쪽이 적합하다.
- wrighting 반영 방식: 현재 세션에 새 document 생성 도구가 노출되지 않아 기존 `wrighting_sync_rules.md` 대응 item에 보조 동기화 메모로 append한다.
