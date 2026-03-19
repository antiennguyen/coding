# 🎲 HƯỚNG DẪN CHƠI MONOPOLY ONLINE

## ✨ Tính Năng Chính

- ✅ **Đầy Đủ Luật Monopoly**: Mua bất động sản, thu tiền thuê, xây nhà/khách sạn
- 🌐 **Chơi Online Multiplayer**: Chơi cùng bạn bè trên máy khác nhau
- 🎨 **Giao Diện Đẹp**: Dùng Pygame với hiệu ứng và animation mượt mà
- 🏗️ **Thiết Kế OOP**: Code sạch và dễ bảo trì
- 🎴 **Thẻ Chance & Community Chest**: Hệ thống thẻ đầy đủ
- 📊 **Theo Dõi Trạng Thái**: Tiền, bất động sản, và tình trạng trò chơi

## 📁 Cấu Trúc Thư Mục

```
game/
├── core/                      # Lõi game logic
│   ├── game.py               # Bộ điều khiển game chính
│   ├── player.py             # Lớp Player
│   ├── board.py              # Bàn cờ
│   ├── property.py           # Quản lý bất động sản  
│   ├── dice.py               # Xúc xắc
│   ├── card.py               # Thẻ bài
│   └── utils.py              # Tiện ích
├── server/                    # Server cho multiplayer
│   └── monopoly_server.py    # Game server
├── client/                    # Client GUI
│   ├── game_client.py        # Network client
│   └── game_ui.py            # Giao diện Pygame
├── config.py                 # Cấu hình
├── test_game.py              # Test suite
├── quickstart.py             # Script khởi động nhanh
├── requirements.txt          # Dependencies
└── README.md & API.md & ADVANCED.md
```

## ⚙️ Cài Đặt

### Yêu Cầu Hệ Thống
- Python 3.8+
- pip (package manager)
- Windows, macOS hoặc Linux

### Bước 1: Cài Đặt Dependencies

Tất cả packages đã được cài đặt trong thư mục `.venv` của bạn.
Nếu cần cài lại:

```bash
cd game
pip install -r requirements.txt
```

### Bước 2: Chạy Test (tùy chọn)

```bash
python test_game.py
```

## 🚀 Cách Chơi

### Option 1: Chơi Trên Một Máy (Demo Mode)

**Terminal 1 - Khởi động Server:**
```bash
cd game
python server/monopoly_server.py 2
```

**Terminal 2 - Khởi động Client 1:**
```bash
python client/game_ui.py localhost 5000 "Player 1"
```

**Terminal 3 - Khởi động Client 2:**
```bash
python client/game_ui.py localhost 5000 "Player 2"
```

### Option 2: Chơi Online (Nhiều Máy Khác Nhau)

**Máy Chủ (Server Machine):**
```bash
python server/monopoly_server.py 2
# Lưu ý IP của máy hiện tại
```

**Máy 1 (Client):**
```bash
python client/game_ui.py <SERVER_IP> 5000 "Player 1"
```

**Máy 2 (Client):**
```bash
python client/game_ui.py <SERVER_IP> 5000 "Player 2"
```

Thay `<SERVER_IP>` bằng địa chỉ IP thực tế của máy server.

## 🎮 Điều Khiển Game

### Phím Tắt
- **SPACE**: Lăn xúc xắc
- **E**: Kết thúc lượt
- **ESC**: Thoát game
- **MOUSE**: Click trên bàn cờ để tương tác

### Nút Trong Giao Diện
- **Roll Dice**: Lăn xúc xắc để di chuyển
- **End Turn**: Kết thúc lượt của bạn
- **Buy Property**: Mua bất động sản (nếu có)

## 📖 Luật Game

### Mục Đích
Trở thành người giàu nhất bằng cách mua, cho thuê và buôn bán bất động sản.

### Cách Chơi

1. **Lăn Xúc Xắc**: Mỗi lượt, lăn hai xúc xắc để di chuyển
2. **Đáp Xuống Các Ô**:
   - **Bất động sản chưa có chủ**: Bạn có thể mua nó
   - **Chủ sở hữu khác**: Thanh toán tiền thuê
   - **Sở hữu của bạn**: Không có hành động
   - **Ô đặc biệt**: GO, Free Parking, Go to Jail, Tax

3. **Bất Động Sản**:
   - Mua những ô chưa được sở hữu
   - Xây nhà và khách sạn trên bộ màu đầy đủ
   - Thu tiền từ người chơi khác

4. **Nhà Tù**:
   - Đáp xuống "Go to Jail" hoặc rút thẻ
   - Lăn số đôi để thoát hoặc trả 50$

5. **Phá sản**: 
   - Nếu không trả được nợ, bạn thua cuộc
   - Người chơi cuối cùng còn lại là người thắng!

## 💰 Giá Trị Bất Động Sản

| Loại | Mô Tả | Giá |
|------|-------|-----|
| Streets | Từ Mediterranean ($60) đến Boardwalk ($400) | Khác nhau |
| Railroads | 4 đường sắt | $200 mỗi cái |
| Utilities | 2 tiện ích | $150 mỗi cái |
| Houses | 50% giá bất động sản | Khác nhau |
| Hotels | 50% giá bất động sản | Khác nhau |

**Tiền Đi Qua GO**: $200
**Thuế Nhập Thu**: $200
**Thuế Xa Xỉ**: $75

## 🏛️ Kiến Trúc Thiết Kế OOP

### Các Lớp Chính

**Player** - Quản lý người chơi
- Tiền tệ, bất động sản, vị trí, tình trạng nhà tù

**Property** - Quản lý bất động sản  
- Mua, bán, thế chấp
- Đếm nhà/khách sạn
- Tính tiền thuê

**Board** - Quản lý bàn cờ
- 40 ô trên bàn
- Bộ thẻ Chance và Community Chest
- Tìm kiếm bất động sản

**MonopolyGame** - Bộ điều khiển trò chơi
- Quản lý lượt chơi
- Kiểm soát luật
- Đồng bộ hóa trạng thái

**GameClient** - Client mạng
- Kết nối đến server
- Gửi/nhận tin nhắn
- Queue tin nhắn

## 🌐 Thiết Kế Multiplayer

### Kiến Trúc Server-Client
- **Socket TCP**: Giao tiếp đáng tin cậy
- **JSON Protocol**: Định dạng tin nhắn độc lập với nền tảng
- **Real-time Updates**: Broadcast trạng thái cho tất cả client
- **Validation**: Kiểm tra hành động hợp pháp

### Đồng Bộ Game
- Server giữ trạng thái chính
- Client hiển thị state và gửi hành động  
- Không có game logic phía client (ngăn cheat)
- Cập nhật state qua broadcast

## 🔧 Cách Mở Rộng Game

### Thêm Hiệu Ứng Âm Thanh

1. Đặt file audio vào `assets/sounds/`
2. Sử dụng pygame.mixer trong `game_ui.py`:

```python
pygame.mixer.init()
sound = pygame.mixer.Sound("assets/sounds/diceroll.wav")
sound.play()
```

### Thêm Hiệu Ứng Hình Ảnh

File `ADVANCED.md` có các ví dụ về:
- Hệ thống Particle
- Animation Custom
- Theme tùy chỉnh
- ...

### Thêm AI Opponents

Xem `ADVANCED.md` để biết cách tạo lớp AIPlayer với chiến lược thông minh.

## 🐛 Troubleshooting

### Lỗi "Connection refused"
- Đảm bảo server đang chạy
- Kiểm tra firewall
- Xác minh kết nối mạng

### Pygame không tìm thấy
```bash
pip install --upgrade pygame
```

### Game chậm
- Đóng các ứng dụng khác
- Kiểm tra cấu hình màn hình
- Đảm bảo 60 FPS

## 📚 Tài Liệu Thêm

- **README.md**: Hướng dẫn chi tiết
- **API.md**: Tài liệu API đầy đủ
- **ADVANCED.md**: Tính năng nâng cao và mở rộng

## 🎯 Các Tính Năng Sắp Tới

- [ ] Hồ sơ người chơi và thống kê
- [ ] Ghi lại và phát lại game
- [ ] Ứng dụng di động
- [ ] Đối thủ AI
- [ ] Theme bàn cờ tùy chỉnh
- [ ] Âm thanh và nhạc nền
- [ ] Cải thiện giao diện buôn bán
- [ ] Chế độ giải đấu
- [ ] Chat trong game
- [ ] Lưu/tải game

## ✅ Kiểm Tra Cài Đặt

Để xác minh cài đặt thành công:

```bash
cd game
python test_game.py
```

Nếu tất cả test đều PASS ✓, bạn đã sẵn sàng chơi!

## 📞 Hỗ Trợ

Nếu gặp vấn đề:
1. Xem file README.md
2. Kiểm tra API.md
3. Xem docstring trong source code
4. Kiểm tra lại cấu hình network

## 🎉 Sẵn Sàng Chơi!

```bash
cd game
python server/monopoly_server.py 2
```

Mở terminal khác và chạy:
```bash
python client/game_ui.py localhost 5000 "Your Name"
```

**Chúc bạn chơi vui!** 🎲✨
