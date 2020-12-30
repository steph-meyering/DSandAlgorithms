# def convert_to_linked_list(root):
#   head, _ = dfs(root)
#   return head

# def dfs(root):
#   if root is None:
#     return None, None
#   head, prev = dfs(root.left)
#   next, tail = dfs(root.right)
#   root.left = prev
#   root.right = next
#   if head is None:
#     head = root
#   if tail is None:
#     tail = root
#   return head, tail

def convert_to_linked_list(root):
  in_order = []
  dfs(root, in_order)
  for i in range(len(in_order)):
    if i == 0:
      in_order[i].left = None
    else:
      in_order[i].left = in_order[i-1]
    if i == len(in_order) - 1:
      in_order[i].right = None
    else:
      in_order[i].right = in_order[i+1]
  return in_order[0]

def dfs(root, arr):
  if root:
    dfs(root.left, arr)
    arr.append(root)
    dfs(root.right, arr)

