def solution(clothes):
    kindOfClothes = list()
    add ,product_add = 0, 0
    product, pproduct = 1, 1
    for i in range(len(clothes)):
        kindOfClothes.append(clothes[i][1])
    closet = dict()
    for i in range(len(clothes)):
        c = list()
        for j in range(len(clothes)):
            if clothes[i][1] == kindOfClothes[j]:
                c.append(clothes[j][0])
        closet[kindOfClothes[i]] = c
    print(closet)
    for value in closet.values():
        add += len(value)
        product *= len(value)
        if len(closet) == 1:
            return add
        if len(closet) > 2:
            for v in closet.values():
                if value == v:
                    continue
                else:
                    pproduct = len(value)*len(v)
                print(value, v, pproduct)
                product_add += pproduct
    print(add, product, (product_add//2))
    return add+product+(product_add//2)
clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"], ["cardigan", "clothe"]]
print(solution(clothes))

# 정확도 39.1
