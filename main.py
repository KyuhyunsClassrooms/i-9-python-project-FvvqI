# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20522
# 프로젝트 주제: 스타트업 투자 유치 자격 진단기

# AI 활용 자유 주제 파이썬 미니 프로젝트
# 이름 또는 학번: 20522
# 프로젝트 주제: 스타트업 투자 유치 자격 진단기

# ============================================================
# 필수 조건 검증 완료
# 1. 2차원 리스트 사용 (investors)
# 2. 함수 3개 이상 분리 (show_intro, input_startup_data, check_investment_eligibility, print_diagnostic_report)
# 3. 조건문 사용 (if-else 예외 처리 및 조건 대조)
# 4. 반복문 사용 (while 입력 루프, for 리스트 순회)
# 5. 실행 결과 출력 완료
# ============================================================


# ------------------------------------------------------------
# 1. 데이터 준비: 2차원 리스트
# ------------------------------------------------------------
# [투자사 이름, 최소 매출액(만원), 최소 특허 수(개), 최소 팀원 수(명)]
# ------------------------------------------------------------
investors = [
    ["A앤젤스", 1000, 0, 2],
    ["B벤처스", 5000, 1, 3],
    ["C인베스트", 15000, 2, 5],
    ["D파트너스", 50000, 3, 10]
]


# ------------------------------------------------------------
# 2. 함수 정의
# ------------------------------------------------------------

def show_intro():
    """프로그램 제목과 안내를 출력한다."""
    print("=" * 45)
    print("AI 활용 자유 주제 파이썬 미니 프로젝트")
    print("주제: 스타트업 투자 유치 자격 진단기")
    print("=" * 45)


def input_startup_data():
    """사용자로부터 스타트업의 지표를 안전하게 입력받는다 (음수 예외 처리)."""
    print("----- [스타트업 정보 입력] -----")
    
    while True:
        revenue = int(input("1. 연간 총 매출액을 입력하세요 (단위: 만원): "))
        if revenue >= 0:
            break
        print("경고: 매출액은 음수일 수 없습니다. 다시 입력해 주세요.\n")
        
    while True:
        patent = int(input("2. 보유한 기술 특허 개수를 입력하세요 (단위: 개): "))
        if patent >= 0:
            break
        print("경고: 특허 개수는 음수일 수 없습니다. 다시 입력해 주세요.\n")
        
    while True:
        team = int(input("3. 현재 상시 팀원 수를 입력하세요 (단위: 명): "))
        if team >= 0:
            break
        print("경고: 팀원 수는 음수일 수 없습니다. 다시 입력해 주세요.\n")
        
    return [revenue, patent, team]


def check_investment_eligibility(investor_list, startup_data):
    """2차원 리스트를 반복 순회하며 투자 조건을 대조하고 필터링한다."""
    user_revenue = startup_data[0]
    user_patent = startup_data[1]
    user_team = startup_data[2]
    
    eligible_investors = [] # 자격이 통과된 투자사들을 담을 빈 리스트
    
    for investor in investor_list:
        name = investor[0]
        min_revenue = investor[1]
        min_patent = investor[2]
        min_team = investor[3]
        
        # 조건문: 매출, 특허, 팀원 조건이 모두 투자사 기준 '이상'인지 판단한다.
        if user_revenue >= min_revenue and user_patent >= min_patent and user_team >= min_team:
            eligible_investors.append(investor)
            
    return eligible_investors


def print_diagnostic_report(startup_data, eligible_list):
    """최종 진단 결과를 화면에 보기 좋게 출력한다."""
    print("\n=======================================")
    print("       스타트업 투자 자격 진단 결과       ")
    print("=======================================")
    print(f"■ 입력된 스타트업 정보")
    print(f" - 매출액: {startup_data[0]}만 원")
    print(f" - 특허 수: {startup_data[1]}개")
    print(f" - 팀원 수: {startup_data[2]}명")
    print("---------------------------------------")
    
    # 예외 상황 처리: 만족하는 투자사가 하나도 없을 때
    if len(eligible_list) == 0:
        print("[진단 결과] 현재 조건으로 신청 가능한 투자사가 없습니다.")
        print("추천 조언: 매출액을 높이거나 특허 기술을 확보하여 조건을 보완하세요!")
    else:
        print("[진단 결과] 다음 투자사에 투자 신청이 가능합니다!\n")
        for inv in eligible_list:
            print(f"▶ {inv[0]} (최소매출: {inv[1]}만원, 최소특허: {inv[2]}개, 최소팀원: {inv[3]}명)")
            
    print("=======================================")


def main():
    show_intro()
    my_startup = input_startup_data()
    results = check_investment_eligibility(investors, my_startup)
    print_diagnostic_report(my_startup, results)


# ------------------------------------------------------------
# 3. 프로그램 실행
# ------------------------------------------------------------
if __name__ == "__main__":
    main()
