# import cv2 as cv

# def fuction(name):
#     print("hi!", name)

# my_name = "Mena"
# fuction(my_name)

# cnt = 0
# while True:
#     cnt += 1
#     fuction(my_name + str(cnt))
#     if cnt >= 5:
#         break

# img = cv.imread("Img\python.png")
# cv.imshow("Img", img)
# cv.waitKey(0)

# tracking objects
# class MyObject:
#     def __init__(self, arg ="Mena "):
#         self.arg = arg

#     def get_arg(self):
#         return self.arg

# obj = MyObject("Lalo")
# obj2 =MyObject()
# print(obj.get_arg())
# print(obj2.get_arg())

# List
my_list = [5]
my_list.append(8)
my_list.append(12)

for item in my_list:
    print(item)