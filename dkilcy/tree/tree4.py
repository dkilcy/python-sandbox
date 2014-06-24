


tree_dict = {"id":10, "children":[] }

print type(tree_dict)
print tree_dict["id"]
print tree_dict["children"]

tree_dict["children"].append({"id":20, "children":[]})

print tree_dict