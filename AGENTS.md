# 럭키아파트 (LuckyApt) — 『대기업 경리과장이 아파트에 위장취업했다』 · Codex 하네스 라우터

재미(코미디)와 힐링이 절반씩인 현대 직장/생활물 웹소설(420화 5부 계절제) 집필 프로젝트. 실제 카카오톡 '경리들모임' 단톡방(`docs/`)이 소재 원천이다. 작품 콘셉트·캐논·정본 위계는 `_workspace/00_INDEX.md`(단일 정본 인덱스)와 `_workspace/12_canon_인물조직_확정.md`가 관리한다 — 여기에 중복 기재하지 않는다.

## 작업 라우팅 (Codex 필수 절차)

럭키아파트 관련 모든 작업(소재 분석, 세계관/인물/플롯/장면 설계, 회차 집필, 유머·명대사 설계, 정합·개연 검수, 휴머나이즈 윤문, 작품성 비평)은 **작업 시작 전에 오케스트레이터 문서를 먼저 읽는다**:

1. **`.agents/skills/luckyapt-novel/SKILL.md`** ← 오케스트레이터 정본. 에이전트 구성(상시 4/필요 6)·집필 루프·데이터 컨벤션·모델 독립 품질 게이트·에러 핸들링이 전부 여기 있다.
2. 수행할 역할에 맞는 **에이전트 정의**를 읽는다: `.codex/agents/{역할}.toml` (동일 내용 정본: `.claude/agents/{역할}.md`). 역할 = plot-architect · prose-writer · humanizer · continuity-editor (상시 4) / humor-designer · critic · character-designer · scene-director · story-architect · source-miner (필요 6).
3. 에이전트 정의가 "○○ 스킬을 따른다"라고 하면 그 스킬은 도구가 아니라 **파일**이다 — `.agents/skills/{스킬명}/SKILL.md`를 읽어라:
   - webnovel-prose(집필) · continuity-check(검수) · humanizer(윤문) · webnovel-plot(플롯) · humor-design(웃음) · critique(비평) · character-design(인물) · scene-design(장면) · story-bible(세계관) · kakao-mining(소재)

## 품질 게이트 (모델·도구 무관 실행 의무)

품질의 하한은 모델 지능이 아니라 **게이트의 실행**이 보장한다. 게이트를 생략한 산출물은 무효 — 상세는 오케스트레이터 §모델 독립 품질 게이트.
- **프리플라이트:** 에이전트 정의의 '입력' 정본(12_canon·06·07 §0~§0-C·09 떡밥 원장)을 실제로 열었는지 확인.
- **집필 저장 전:** prose-writer 7-체크 전 항목 답변 + 분량 측정 **실제 실행**. 분량 = 본문(상단 `<!-- -->` 메타 헤더 제외) **공백 제외 5,500자 내외(5,200~5,800)**. 측정: `python3 -c "import re;t=open(파일,encoding='utf-8').read();b=re.sub(r'<!--.*?-->','',t,flags=re.DOTALL);print(len(re.sub(r'\s','',b)))"`
- **검수:** 축 A(정합)/B(개연)/C(흡입력) 전 항목 명시 답변 + `python3 .agents/skills/humanizer/scripts/pattern_check.py _workspace/chapters --last 5` 실행 결과 첨부.
- **윤문:** humanizer 강제 체크 5항 선실행, 윤문 전/후 분량 측정으로 하한 5,200 사수 증명.
- **떡밥:** 심기/상기/회수는 `_workspace/09_foreshadow_ledger.md` 원장과 동기 갱신.

## 데이터 컨벤션 (요약 — 정본은 오케스트레이터)

회차 `_workspace/chapters/ep_{n}_{제목}.md`(정본, 039·040 결번) · 검수 `reviews/review_ep_{n}.md`(구간 배치는 `review_ep_{a}_{b}.md`) · 윤문 `reviews/humanize_ep_{n}.md` · 장면 `scene_plans/scene_ep_{n}.md`(복잡 회차만) · 기획 정본 `00_INDEX`·`12_canon`·`01~09`. wrighting 동기화는 MCP 도구가 있는 세션에서만(없으면 건너뛰고 미동기 목록 보고).

## 미러 규칙 (중요)

**정본은 `.claude/`(agents·skills)와 `_workspace/`다.** `.agents/skills/`·`.codex/agents/*.toml`은 Codex용 미러: 하네스를 수정할 땐 `.claude/` 쪽을 고친 뒤 미러에 복사한다(toml은 에이전트 md 본문을 내장하므로 재생성 — 방법은 `.claude/harness-changelog.md` 참조). 이 AGENTS.md는 CLAUDE.md의 사본이 아니라 **Codex 전용 라우터** — 하네스 구조가 바뀔 때만 갱신한다.

## 책임 경계

실제 단톡방 참여자의 개인정보(실명·연락처·식별 가능 사생활)는 산출물·본문에 옮기지 않는다. 실화는 반드시 가명화·각색해 허구로 변환한다. 커밋 시 `docs/` 소재 원본 삭제 금지(삭제됐으면 `git restore docs/`), `.omc/state/*` 제외.
