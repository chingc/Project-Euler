from eulerpyramid import EulerPyramid

pyramid = EulerPyramid.build_pyramid("problem18.txt")
path = pyramid.get_highest_path()
print("--- Problem 18 ---")
print("Path:", path)
print("Cost:", sum(path))

pyramid = EulerPyramid.build_pyramid("problem67.txt")
path = pyramid.get_highest_path()
print("--- Problem 67 ---")
print("Path:", path)
print("Cost:", sum(path))
