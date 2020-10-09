# programmers coding test practice:
# Summer/Winter Coding(~2018) - 스킬트리
# 파일명 구분을 위해 사용자 정의 함수명을 바꿨습니다.

def skill_solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        
        # skill에 없는 스킬만으로 구성된 트리는 지우고,
        # 나머지 가능한 트리만 저장할 tree 리스트를 생성합니다.
        tree = [] 
        for sk in skill_tree:
            if sk in skill:
                tree.append(sk)
                
        possibility = True
        for i in range(len(tree)):
            if tree[i] != skill[i]:
                possibility = False
                break
            
        if possibility:
            answer += 1
            
    return answer