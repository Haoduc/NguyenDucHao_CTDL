class _Node:
    # Lớp _Node biểu diễn một nút trong danh sách liên kết
    __slots__ = '_element', '_next'

    def __init__(self, element, next):
        # Khởi tạo một nút với một phần tử và tham chiếu đến nút tiếp theo
        self._element = element
        self._next = next 

class LinkedList:
    def __init__(self):
        # Khởi tạo danh sách liên kết với head (đầu), tail(đuôi) ban đầu là None và size ban đầu là 0
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        # Phương thức trả về kích thước (số lượng phần tử) của danh sách
        return self._size

    def isempty(self):
        # Phương thức kiểm tra xem danh sách có rỗng không
        return self._size == 0

    def addlast(self, e):
        # Phương thức thêm một phần tử mới vào cuối danh sách
        newest = _Node(e, None)
        if self.isempty():
            # Nếu danh sách rỗng, làm cho head trỏ đến nút mới
            self._head = newest
        else:
            # Nếu không, tham chiếu của tail trỏ đến nút mới
            self._tail._next = newest
        # Tail được cập nhật để trỏ đến nút mới
        self._tail = newest
        # Kích thước danh sách tăng lên
        self._size += 1

    def display(self):
        # Phương thức hiển thị các phần tử trong danh sách
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next
        print()

# Tạo một đối tượng LinkedList
L = LinkedList()

# Thêm các phần tử vào danh sách và hiển thị
L.addlast(7)
L.addlast(4)
L.addlast(12)
L.display()
print('Size:', len(L))

# Thêm thêm phần tử và hiển thị lại
L.addlast(8)
L.addlast(3)
L.display()
print('Size:', len(L))
