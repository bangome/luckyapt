#!/usr/bin/env python3
"""럭키아파트 반복 패턴 정량 스캔 (07 §0-B·§0-C 보조 도구).

사용법:
  python3 pattern_check.py <chapters_dir> [--last N] [--target ep_052]

동작: 대상 회차(기본 최근 5화 + --target 지정 화)에 대해
  1) 분량 측정 — 메타 헤더(<!-- -->) 제외, 공백 제외 자수. 가드 5,200~5,800.
  2) 워치리스트 표현 카운트 — 07 워치리스트 핵심 표현의 화당 빈도.
  3) 회차 간 반복 n-그램 — 2화 이상에서 반복되는 4어절+ 구절 상위 목록.
  4) 엔딩 지문 — 각 화 마지막 3문장(엔딩 유형 겹침을 사람이 판단할 재료).
  5) 오프닝 지문 — 각 화 첫 2문장(오프닝 유형 반복 판단 재료).
판단은 도구가 아니라 humanizer/continuity-editor가 한다. 이 출력은 재료다.
"""
import re, sys, glob, os
from collections import Counter, defaultdict

WATCHLIST = [
    "한 박자", "손이 멈췄", "펜이 멈췄", "눈이 멈췄", "마음이 멈췄",
    "이상하게", "처음으로", "정확히", "그제야", "문득", "괜히", "어느새",
    "왈칵", "코끝이 시큰", "따뜻했다", "마음이 놓였다", "봄볕", "형광등",
]
PROPS = ["믹스커피", "보온병", "삶은 계란", "도시락", "슬리퍼", "화단"]

def body_of(path):
    t = open(path, encoding="utf-8").read()
    b = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)
    b = re.sub(r"^#.*$", "", b, flags=re.M)  # 회차 제목 줄 제외
    return b.strip()

def sents(text):
    return [s.strip() for s in re.split(r"(?<=[.!?다])\s+", text) if s.strip()]

def main():
    args = sys.argv[1:]
    cdir = args[0] if args else "_workspace/chapters"
    last = 5
    target = None
    if "--last" in args: last = int(args[args.index("--last") + 1])
    if "--target" in args: target = args[args.index("--target") + 1]
    files = sorted(glob.glob(os.path.join(cdir, "ep_*.md")))
    picked = files[-last:]
    if target:
        tf = [f for f in files if target in f]
        picked = sorted(set(picked + tf))
    if not picked:
        print("no chapter files found"); return

    print("=== 1) 분량 (공백 제외, 헤더 제외 / 가드 5,200~5,800) ===")
    bodies = {}
    for f in picked:
        b = body_of(f); bodies[f] = b
        n = len(re.sub(r"\s", "", b))
        flag = "OK" if 5200 <= n <= 5800 else ("MISS-UNDER" if n < 5200 else "MISS-OVER")
        print(f"  {os.path.basename(f)[:40]:42s} {n:5d}  {flag}")

    print("\n=== 2) 워치리스트 표현·소품 (화당 빈도, 0은 생략) ===")
    for f in picked:
        hits = {w: bodies[f].count(w) for w in WATCHLIST + PROPS if bodies[f].count(w)}
        if hits:
            print(f"  {os.path.basename(f)[:30]}: " + ", ".join(f"{k}×{v}" for k, v in sorted(hits.items(), key=lambda x: -x[1])))

    print("\n=== 3) 회차 간 반복 4어절+ 구절 (2화 이상 등장) ===")
    ngram_files = defaultdict(set)
    for f in picked:
        words_per_sent = [s.split() for s in sents(bodies[f])]
        for ws in words_per_sent:
            for i in range(len(ws) - 3):
                g = " ".join(ws[i:i + 4])
                if len(g) >= 10:
                    ngram_files[g].add(os.path.basename(f))
    rep = [(g, fs) for g, fs in ngram_files.items() if len(fs) >= 2]
    for g, fs in sorted(rep, key=lambda x: -len(x[1]))[:20]:
        print(f"  [{len(fs)}화] {g}  ({', '.join(sorted(f[:10] for f in fs))})")
    if not rep: print("  (반복 구절 없음)")

    print("\n=== 4) 엔딩 지문 (마지막 3문장 — 유형 겹침 판단 재료) ===")
    for f in picked:
        tail = " / ".join(sents(bodies[f])[-3:])
        print(f"  {os.path.basename(f)[:30]}: {tail[:150]}")

    print("\n=== 5) 오프닝 지문 (첫 2문장 — 오프닝 유형 반복 판단 재료) ===")
    for f in picked:
        head = " / ".join(sents(bodies[f])[:2])
        print(f"  {os.path.basename(f)[:30]}: {head[:150]}")

if __name__ == "__main__":
    main()
