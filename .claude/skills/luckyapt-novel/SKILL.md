---
name: luckyapt-novel
description: >
  재미와 힐링이 있는 현대 웹소설 『럭키아파트』의 기획·집필·검수를 총괄하는 오케스트레이터.
  실제 카카오톡 단톡방 소재 분석, 세계관·인물·플롯 설계와 장면 설계, 회차 집필, 유머·드립·명대사 설계, 정합·개연 검수를 전문 에이전트 팀으로 조율한다.
  '럭키아파트' 또는 이 소설 작업(소재 분석/카톡 마이닝, 세계관/설정, 인물/캐릭터, 플롯/구성, 장면 설계,
  회차/에피소드 집필, 유머/드립/웃음/명대사 설계, 정합/개연/검수, 휴머나이즈/문체 윤문, 작품성 비평/평가)을 요청하면 반드시 사용할 것. 후속 작업도 포함:
  '럭키아파트 이어서', '다음 화 써줘', '○화 다시', '인물 보완', '설정 수정', '플롯 업데이트',
  '기획 재실행', '이전 결과 기반으로 개선', '소재 다시 분석', '비평해줘', '작품성 평가',
  '재미있는지/따뜻한지/매력 충분한지 봐줘', '전개 속도 어때', '편집자 시선으로' 등의 표현에도 트리거된다.
  단순 질문(예: 용어 뜻 묻기)은 직접 응답 가능.
---

# 럭키아파트 소설 집필 오케스트레이터

재미와 힐링이 있는 현대 웹소설 『럭키아파트』를 전문 에이전트 팀으로 기획·집필·검수한다.

## 작품 콘셉트 (고정 토대) — ★확정 캐논: `_workspace/12_canon_인물조직_확정.md` 우선
제목 『대기업 경리과장이 아파트에 위장취업했다』. **현대 직장/생활물 + 위장취업 코미디 + 힐링(유능한 프로 주인공의 현실 사이다, 초능력·마법 없음)** 웹소설.
- **로그라인:** 대기업(차도그룹) 재무회계 천재 경리과장(박한결, 33세 미혼 여성)이 계열 위탁관리사 '차도관리' 사장(둘째 차윤수)의 밀명으로 '행운 아파트' 관리사무소에 경리(위장명 박한율)로 위장취업해, 그 단지 입대의 회장이자 차도건설 부사장인 첫째 차윤상의 비리 증거를 캐다가 진실을 알아간다.
- **반전:** 밀명을 준 둘째 차윤수가 차기 회장직을 노리고 첫째를 모함한 것이고 실제 비리도 둘째(차도관리/위탁사) 쪽. 첫째 차윤상(입대의 회장)은 퉁명하지만 단지를 아끼는 따뜻한 사람 — 주인공이 알아가고 **자신을 보낸 둘째가 흑막**임을 깨달으며 첫째·주민들과 함께 행복한 아파트를 만든다.
- **위장 메커니즘:** 둘째(차도관리=위탁사 사장)가 인사권으로 주인공을 경리로 투입. 관리소장·직원도 차도관리(둘째) 소속 → 고용주=밀명자=흑막이 위장 긴장의 핵. 자금결재권·의결권은 첫째(입대의 회장)가 정직하게 행사.
- **톤:** 요절복통 코미디 + 감동 에피소드 교차. 재미 절반 + 힐링 절반. 사이다는 베테랑 경리의 실력·정직·끈기에서.
- **소재·고증:** 실제 '경리들모임' 단톡방 export(`docs/`)에서 경리 인물·말투·에피소드 채굴(source-miner). 관리사무소·관리비·입주자단체 실무 고증 정본 = `_workspace/08~11`.
- **시점·형식:** 밀착 3인칭 주인공 + 후반 한정 멀티 POV(확정). 아파트 주민은 앙상블 조연.

## 실행 모드: 하이브리드
- **기획 단계** → 파이프라인 (소재 분석 → 세계관/시점 결정 → 인물/관계 아크 → 플롯). source-miner는 기획 초입에 1회 필수로 돈다.
- **집필 단계** → 장면 설계 + 생성-검증 (`scene-director` 장면 설계 → `prose-writer` 집필 → `continuity-editor` 정합·개연 통합 검수 → 수정 → `humanizer` 휴머나이즈 윤문 → 최종).

에이전트 팀(`TeamCreate`)으로 구성하고, 산출물은 `_workspace/` 파일로 주고받는다.

### 모델 분배 (Opus / Sonnet) — 집필 보조는 Sonnet, 설계·비평은 Opus
> 원칙: **소설 집필의 기본 모델은 Sonnet, 중요한 설계·비평·대수정은 Opus.** 회차를 계속 쓰고 고치는 연재 작업에서는 Sonnet을 메인으로(빠르고 비용 효율), Opus를 고차 판단용으로 쓰는 조합이 가장 효율적이다(대략 Sonnet 60~70% / Opus 30~40%). 각 에이전트 정의 파일의 `model:` frontmatter가 기본값이며, 아래는 그 분배 근거다.

- **Opus (고차 설계·구조·캐릭터 판단·비평):** `story-architect`(세계관·구조·복선 설계), `plot-architect`(전체 플롯·장기 떡밥·후킹·절단면), `character-designer`(인물 동기·대사 톤·미세 어긋남), `critic`(작품성 비평 = 편집장/스토리 닥터).
- **Sonnet (집필·윤문·검수·분석·웃음 생산 — 반복 실무):** `prose-writer`(회차 초안·대량 생산), `humanizer`(문체 윤문·대량 수정), `scene-director`(장면 설계도 실무), `continuity-editor`(회차별 정합 검수 반복), `source-miner`(대용량 카톡 분석), `humor-designer`(웃음 라인 생산·변주).
- **Opus 오버라이드(호출 시 `model: "opus"` 지정):** 기본 Sonnet인 에이전트라도 **(a) 결정적 회차의 장면 설계(scene-director), (b) 캐논·구조가 걸린 중대 정합 검수(continuity-editor), (c) 웃음 엔진 초기 설계나 핵심 러닝 개그 결정화(humor-designer)** 처럼 고차 판단이 필요하면 그 호출에 한해 Opus로 올린다. 반대로 단순·반복 작업은 기본 모델을 그대로 쓴다. 모델은 작업 성격에 맞춰 호출 단위로 조정한다.

## 에이전트 구성 (10)
- **상시 코어(7):** story-architect, character-designer, plot-architect, scene-director, prose-writer, continuity-editor, humanizer.
- **필요 호출(3):** source-miner(소재 분석 — 프로젝트 초기 1회 필수, 이후 소재 재분석 요청 시), humor-designer(웃음·드립·명대사 설계 — 인물 확정 후 1회 + 결정적 웃음 회차 요청 시), critic(작품성 비평 — 평가 요청 시).
- rubycarrier 대비 제거: research-specialist(범죄 고증)·culture-researcher·logic-auditor. **논리/개연 검수는 continuity-editor가 정합과 함께 흡수**한다. quote-designer는 힐링/유머 장르에 맞춰 **humor-designer로 재정의**(명대사보다 재미·드립 중심)했다.

## Phase 0: 컨텍스트 확인 (항상 먼저)
1. `_workspace/` 존재 여부와 내용을 확인한다.
   - **미존재** → 초기 실행(Phase 1, source-miner부터).
   - **존재 + 부분 수정 요청**(예: "3화 다시", "○○ 인물 보완") → 부분 재실행. 해당 에이전트만 재호출.
   - **존재 + 새 콘셉트/새 소재 입력** → 기존 `_workspace/`를 `_workspace_prev/`로 옮기고 새 실행.
   - **존재 + 이어쓰기**("다음 화") → 마지막 회차 다음부터 집필 단계 진입.
2. 판별 결과를 사용자에게 한 줄로 알리고 진행한다.

## Phase 1: 기획 (파이프라인)
**실행 모드: 에이전트 팀 (파이프라인)**
1. `TeamCreate`로 팀 구성: source-miner, story-architect, character-designer, plot-architect.
2. `TaskCreate`로 의존성 있는 작업 등록:
   - T0: 카톡 소재 분석 (source-miner) → `_workspace/00_source_personas.md`, `00_source_episodes.md`, `00_source_relationship_map.md`, `00_source_voice_patterns.md`
   - T1: 세계관 바이블 + **시점·형식 결정 옵션** (story-architect, T0 의존) → `_workspace/01_worldbible_setting.md`
   - T2: 인물 시트·관계도·캐릭터 아크 (character-designer, T0·T1 의존) → `_workspace/02_characters_sheet.md`
   - T3: 플롯·회차 구성 (plot-architect, T2 의존) → `_workspace/03_plot_structure.md`
   - T-humor: 웃음 엔진 설계 — 인물별 웃음 문법·러닝 개그·명대사 토대 (humor-designer, T2·T3 의존, 권장) → `_workspace/05_humor_lines.md`
3. 팀원은 `SendMessage`로 충돌·요청을 직접 조율한다. 각 단계 산출물 완료 시 다음 에이전트에 통지.
4. **시점·형식은 사용자 결정 사항이다.** story-architect가 옵션(1인칭/3인칭, 단일/군상극)을 제시하면 사용자에게 확인받은 뒤 인물·플롯을 확정한다.
5. 산출물이 완료되면 기획안을 요약 보고하고 집필 진입 여부를 확인한다.

## Phase 2: 집필 (장면 설계 + 생성-검증 루프)
**실행 모드: 장면 설계 → 생성-검증**
회차 단위로 반복한다(웹소설 연재).
> ★**흡입력 운용 정본 = `_workspace/06_engagement_brief.md`.** 모든 회차는 이 브리프의 **5박자 구조**(현장 소동→한율 오판/문화충격→숫자 이상징후(손 멈춤)→작은 해결/패배(사이다·관계·추리 보상 중 ≥1)→다음화 잔가시), **회차 체크리스트 6항**, **엔딩 5타입 순환**(사이다·코미디·서스펜스·감동·반전, 한 타입 반복 금지), **사건 A/B/C/D형**, **금지 항목**(물음표만 쌓기·회계 설명 과잉·회장 오독 단조로움·저녁 사무소 엔딩 반복·한율 수동화)을 준수한다. scene-director·prose-writer·continuity-editor·humanizer 전 단계의 공통 기준이다. 한 줄 검수: "한율은 오늘도 숫자 하나를 바로잡아 사람 하나를 구하지만, 그 정확함 때문에 더 깊이 엮이고 위장한 자신도 조금씩 드러난다."
1. plot-architect의 해당 회차 시놉시스를 확인한다.
2. scene-director가 해당 회차의 장면 설계도 작성 → `_workspace/scene_plans/scene_ep_{n}.md`
   - 일상·감정 회차도 장소/동선/정서적 압박(오해·서운함·말 못 한 마음)이 약하면 호출한다.
3. prose-writer가 회차를 집필 → `_workspace/chapters/ep_{n}_{제목}.md`
   - 반드시 `03_plot_structure.md`, `02_characters_sheet.md`, `00_source_voice_patterns.md`(말투 자산), `05_humor_lines.md`(웃음·드립·명대사), **`06_engagement_brief.md`(★5박자·체크리스트·엔딩 순환·한율/조연 운용)**, `07_author_voice.md`(작가 페르소나·과용어 워치리스트), `scene_ep_{n}.md`, 이전 회차를 함께 참고한다.
   - 결정적 웃음 회차거나 러닝 개그 변주·콜백이 필요한데 `05_humor_lines.md`에 마땅한 라인이 없으면 humor-designer에 해당 회차 라인을 요청한다.
4. continuity-editor가 정합·개연 통합 검수 → `_workspace/reviews/review_ep_{n}.md` (설정·시점·떡밥 콜백·문체·한국어 화계/호칭 + 감정선·관계 변화 개연성 + **`06_engagement_brief.md` 흡입력 검수: 체크리스트 6항(표면사건·바로잡는 숫자·손해본 사람·들킬 뻔한 지점·온기·다음화 질문) 충족, 엔딩 타입이 직전 회차들과 안 겹치는지, 금지 항목(물음표만 쌓기·회계 설명 과잉·회장 오독 단조·저녁 사무소 엔딩 반복·한율 수동화) 위반 여부**).
5. 치명/중대 지적이 있으면 prose-writer가 수정(최대 1회 재시도). 구조 문제면 plot-architect, 장면 문제면 scene-director에 되돌린다. 재실패 시 지적을 남긴 채 사용자에게 보고.
6. humanizer가 휴머나이즈 윤문: 정합이 끝난 회차를 'AI 티 제거 + 작가 페르소나' 기준으로 다듬는다 → `_workspace/07_author_voice.md`·`_workspace/reviews/humanize_ep_{n}.md` 갱신, 본문에 표현·리듬 라인 에디트 적용(사실·구조 불변).
7. 통과한 회차는 사용자 지정 출력 경로(기본 `manuscript/`)로 복사한다. `_workspace/`의 중간본은 보존.

## 에이전트 호출 원칙
- **source-miner**는 프로젝트 초기 1회 필수(모든 인물·에피소드의 원천). 이후엔 새 소재 추가나 "소재 다시 분석" 요청 시에만 재호출.
- **humor-designer**는 인물 확정 후 1회 호출해 웃음 엔진(인물별 웃음 문법·러닝 개그·명대사 토대)을 깔고, 이후엔 결정적 웃음 회차·러닝 개그 변주/콜백·"더 웃기게" 요청 시 호출한다. 매 회차 강제로 끼우지 않는다 — 일상 유머는 prose-writer가 `05_humor_lines.md` 자산으로 직접 처리하고, humor-designer는 설계가 필요한 지점에만 든다. critic이 "재미·유머 약하다"고 위임하면 호출된다.
- **critic**은 매 회차 검수 루프(continuity·humanizer)와 별개의 작품성 비평 레인이다. 집필 파이프라인에 상시 끼우지 않고, 사용자가 비평·평가·"재미있는지/따뜻한지/매력 충분한지" 등을 요청할 때만 호출한다. 비평 범위(부분/부/전체)를 받아 `_workspace/reviews/critique_{scope}.md`를 산출하고, 개선 항목을 담당 에이전트(character-designer·plot-architect·scene-director·prose-writer·humanizer 등)에 위임 표시한다. 범위가 크면 차원별/구간별로 분할 호출 후 종합한다(`model: "opus"`).

## 데이터 전달 프로토콜
- **태스크 기반**(조율) + **파일 기반**(산출물) + **메시지 기반**(실시간 소통) 조합.
- 파일명 컨벤션: `_workspace/{단계번호}_{산출물}.md`, 소재는 `_workspace/00_source_*.md`, 웃음·드립·명대사는 `_workspace/05_humor_lines.md`, **흡입력 운용 정본은 `_workspace/06_engagement_brief.md`, 작가 페르소나·과용어 워치리스트는 `_workspace/07_author_voice.md`**, 회차는 `_workspace/chapters/ep_{n}_*.md`, 장면 설계도는 `_workspace/scene_plans/scene_ep_{n}.md`, 검수는 `_workspace/reviews/*.md`.
- 최종 원고만 `manuscript/`에 출력. 중간 산출물은 삭제하지 않는다.
- **반환 규약(공통):** 모든 전문 에이전트는 산출물을 약속된 파일에 쓴 뒤, **최종 응답 메시지에 핵심 요약(산출·발견·변경 + 파일 경로)을 함께 반환**한다. 에이전트가 '완료'만 반환하면 오케스트레이터는 해당 산출 파일을 읽어 결과를 확인한다 — 빈 회신으로 결과가 유실되지 않게.

## 에러 핸들링
- 에이전트 실패 시 1회 재시도, 재실패하면 해당 산출물 없이 진행하고 보고서에 누락을 명시한다.
- 설정·인물·플롯 간 상충 데이터는 삭제하지 않고 출처를 병기해 사용자 판단을 구한다.
- 회차가 정서 묘사만 있고 사건·관계 진전이 약하면 prose-writer 문제가 아니라 scene-director 단계 누락 가능성을 먼저 점검한다.
- source-miner 산출물에 실명·식별정보가 남아 있으면 가명화·각색 후 사용한다(실화 → 허구 변환). 개인정보를 본문에 그대로 옮기지 않는다.

## 팀 크기
기획 4~5명(source-miner·story-architect·character-designer·plot-architect + 권장 humor-designer). 집필 4명(scene-director·prose-writer·continuity-editor·humanizer) + 필요 시 humor-designer/critic. 한 세션에 한 팀만 활성화되므로, 기획 팀 완료 후 `TeamDelete` → 집필 팀 `TeamCreate`로 재구성한다. Phase 전환 시 산출물이 파일로 보존되어 연결이 끊기지 않는다.

## 테스트 시나리오
- **정상 흐름:** "럭키아파트 기획 만들어줘" → Phase 0(초기 판별) → Phase 1(소재 분석 → 세계관·시점 옵션 제시·결정 → 인물 → 플롯) → 기획 요약 보고 → (승인) → Phase 2 scene plan·1화 집필·검수·윤문·출력.
- **소재 활용 흐름:** "단톡방에서 라식 얘기 에피소드 살려줘" → source-miner의 `00_source_episodes.md`에서 해당 씨앗 확인 → plot-architect 회차 배치 → scene-director 장면화 → prose-writer 집필.
- **에러 흐름:** "5화 써줘"인데 플롯에 5화 시놉시스가 없음 → prose-writer가 plot-architect에 구체화 요청 → 보강 → scene-director 장면 설계 → 집필. 재시도 실패 시 "5화 구성이 비어 있어 집필 불가, 플롯 보강 필요" 보고.
- **후속 흐름:** "3화 톤이 너무 가라앉았어, 더 웃기게" → Phase 0가 부분 재실행 판별 → humor-designer가 3화용 펀치라인·드립 보강(`05_humor_lines.md`) → prose-writer가 해당 라인 반영 재집필 → continuity-editor 재검수 → humanizer 윤문.
- **웃음 설계 흐름:** "단톡방 러닝 개그 하나 만들어줘" 또는 "○○ 캐릭터 웃음 포인트 잡아줘" → humor-designer 호출 → `00_source_voice_patterns.md`·`02_characters_sheet.md` 기반으로 인물 웃음 문법·러닝 개그·콜백 설계 → `05_humor_lines.md` 갱신 → prose-writer가 해당 회차에 심음.
- **비평 흐름:** "1~10화 재미있는지, 캐릭터 매력·따뜻함·전개 속도 봐줘" → critic 호출(범위=ep_001~010) → `critique` rubric으로 차원별 평가 → `_workspace/reviews/critique_ep_001_010.md` 산출 → 강점·치명/권장 약점·위임 요약 보고. 개선 항목은 담당 에이전트로 후속 연결.
