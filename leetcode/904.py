class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        window_start = 0
        basket = {}
        max_fruit = 0
        for i in range(len(tree)):
            right_fruit = tree[i]
            if right_fruit not in basket:
                basket[right_fruit] = 0
            basket[right_fruit] += 1

            while len(basket) > 2:
                left_fruit = tree[window_start]
                basket[left_fruit] -= 1
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                window_start += 1
            max_fruit = max(max_fruit, i - window_start + 1)
        return max_fruit
