def sol(preorder,inorder):
    ret = []

    def print_postorder(preorder, inorder):
        n = len(preorder)
        if n == 0:
            return
        root = preorder[0]

        i = inorder.index(root)
        print_postorder(preorder[1 : i + 1], inorder[:i])
        print_postorder(preorder[i + 1 :], inorder[i + 1 :])
        ret.append(root)

    print_postorder(preorder, inorder)
    print(*ret)

test_case = int(input())

for _ in range(test_case):
    num_node = int(input())
    preorder = [int(x) for x in input().split()]
    inorder = [int(x) for x in input().split()]
    sol(preorder, inorder)