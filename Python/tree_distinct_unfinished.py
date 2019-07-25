

tree2 = (1, 
    (2, (1, None, None), (2, None, None)), (2, (4, None, None), (1, None, None)))

# tree3 = (1, None, (2, (1, None, None), (1, (4, None, None), None)))


# Check if the current node is empty or null.
# Display the data part of the root (or current node).
# Traverse the left subtree by recursively calling the pre-order function.
# Traverse the right subtree by recursively calling the pre-order function.

def traverse_tree(tree):
  # while 

  path = []
  current_leaf = tree[0]
  current_side = 'ROOT'
  print(current_side, current_leaf )
  
  current_leaf = tree[1]
  current_side = 'left B'
  print(current_side, current_leaf )

  current_leaf = tree[1][1]
  current_side = 'left C'
  print(current_side, current_leaf )

  current_leaf = tree[1][1][1]
  current_side = 'left D'
  print(current_side, current_leaf )

  if current_leaf == None:
    path.append(tree[0])
    print(path)
  else:
    traverse_tree[1:]


traverse_tree(tree2)
