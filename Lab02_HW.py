#1
a = 7
b = 5
c = a - b
print (c)

#2
city = "Hà Nội"
year = 2025
print("Thành phố:", city, "- Năm:",year)

#3
n = 4
t = 0
for i in range(1,n+1):
    t += i
print(t)
#Sau mỗi lần lặp for với i=1,2,3,4, t từ 0 sẽ được cộng với các giá trị i sau mỗi lần lặp
#Sau khi lặp lần cuối (t += 4), in kết quả cuối cùng của t = 10 = 0+1+2+3+4

#4
numbers = [1,2,3,4]
for x in numbers:
    if x % 2 == 0:
        print("X là số chẵn")
    else:
        print("X là số lẻ")
#Lệnh lặp for sẽ xét duyệt if-else cho từng giá trị trong list để xem đó là số lẻ hay chẵn

#5
animals = ["cat", "dog", "elephant"]
count = 0
for x in animals:
    count += 1
print("Số lượng phần tử trong danh sách là:", count)
#Với mỗi lần lặp for, số count sẽ được cộng thêm 1, và số lần lặp = số phần tử trong list
#Khi print số count cũng sẽ in ra số phần tử trong list

#6
#Chương trình này đang hiển thị một menu cho người dùng với tiêu đề "AI Prediction System" và ba lựa chọn:
#Phân tích cảm xúc (Sentiment analysis)
#Dự báo thời tiết (Weather forecast)
#Thoát (Exit)
#Sau đó, chương trình yêu cầu người dùng chọn một tùy chọn bằng cách nhập vào số tương ứng.
#Đây là phần giao diện nhập liệu cho một chương trình dự đoán sử dụng AI.

#7
num = input("Nhập số: ")
if int(num) % 2 == 0:
    print("Số chẵn")
else:
    print("Số lẻ")
#Ở dòng 2 của đoạn mã do AI tạo, dấu "=" cần phải được thay bằng dấu "=="

#8
for i in range(3):
    print("AI đang học lần",i + 1)
print("Huấn luyện xong!")
#Lệnh for sẽ lặp lại lệnh print 3 lần với mỗi giá trị i = 0,1,2; mỗi lần print sẽ có số lần AI học tương ứng với i + 1, do i bắt đầu từ 0.
#Sau khi vòng lặp kết thúc => AI đã học xong => In "Huấn luyện xong!"

#9 
for x in ["cat", "dog", "fish"]:
    print("Dự đoán con vật:",x)
#Lệnh for sẽ lặp lại từng giá trị xong list để nhét vào chuỗi string trong print

#10
#Ở dòng 1, đoạn code thiếu hai dấu "(" ở đầu và dấu ")" ở cuối
#Ở dòng 4, đoạn code bị thừa một dấu ")" ở cuối
#Ở dòng 3,5, đoạn code bị thiếu một dấu ")" ở cuối
#Bonus: Ở dòng 5, nên sử dụng dấu " " thay vì ' ' để giữ tính đồng bộ