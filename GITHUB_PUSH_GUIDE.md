# 📤 HƯỚNG DẪN ĐẢY LÊN GITHUB

## 🔧 BƯỚC 1: CÀI ĐẶT GIT (Nếu chưa có)

### Windows
1. Tải Git từ: https://git-scm.com/download/win
2. Chạy installer và follow hướng dẫn
3. Restart PowerShell/CMD
4. Kiểm tra: `git --version`

### Sau khi cài Git

```bash
# Cấu hình Git
git config --global user.name "Your Name"
git config --global user.email "your.email@gmail.com"
```

---

## 🌐 BƯỚC 2: TẠO REPOSITORY TRÊN GITHUB

1. Truy cập https://github.com/new
2. Đặt tên repo: `monopoly-game` hoặc `game-monopoly-online`
3. Chọn "Public" (để chia sẻ)
4. **KHÔNG** chọn "Initialize with README"
5. Click "Create repository"
6. Copy URL (dạng: `https://github.com/YourUsername/monopoly-game.git`)

---

## 📝 BƯỚC 3: PUSH LÊN GITHUB (SAU KHI CÀI GIT)

Chạy các lệnh sau trong PowerShell hoặc CMD:

```powershell
# Vào thư mục game
cd "C:\Users\Admin\Downloads\Assignment\game"

# Khởi tạo git repository
git init

# Thêm tất cả files
git add .

# Commit lần đầu
git commit -m "feat: Monopoly online game with OOP architecture, multiplayer networking, and Pygame GUI"

# Thêm remote repository
git remote add origin https://github.com/YOUR_USERNAME/monopoly-game.git

# Tạo main branch (nếu cần)
git branch -M main

# Đẩy lên GitHub
git push -u origin main
```

**Lưu ý**: Thay `YOUR_USERNAME` bằng username GitHub của bạn

---

## 🔐 BƯỚC 4: XỬ LÝ AUTHENTICATION (NẾU CẦN)

### Cách 1: Personal Access Token (Khuyến Khích)

1. Vào GitHub → Settings → Developer settings → Personal access tokens
2. Click "Generate new token"
3. Chọn scopes: `repo`, `workflow`
4. Sao chép token
5. Khi git hỏi password, paste token này

### Cách 2: SSH Key

```bash
# Tạo SSH key
ssh-keygen -t ed25519 -C "your.email@gmail.com"

# Thêm vào SSH agent
ssh-add ~/.ssh/id_ed25519

# Copy public key
cat ~/.ssh/id_ed25519.pub
```

Sau đó thêm SSH key vào GitHub:
- Settings → SSH and GPG keys → Add key

---

## ✅ BƯỚC 5: KIỂM TRA

```bash
# Xem status
git status

# Xem remote
git remote -v

# Xem commit log
git log
```

---

## 🎮 BƯỚC 6: CHẠY GAME

```powershell
# Vào thư mục
cd "C:\Users\Admin\Downloads\Assignment\game"

# Terminal 1 - Server
python server/monopoly_server.py 2

# Terminal 2 - Client 1
python client/game_ui.py localhost 5000 "Player 1"

# Terminal 3 - Client 2
python client/game_ui.py localhost 5000 "Player 2"
```

---

## 📤 UPDATES TRONG TƯƠNG LAI

Sau khi cài đặt lần đầu, để cập nhật:

```bash
git add .
git commit -m "Update: description of changes"
git push origin main
```

---

## 🆘 TROUBLESHOOTING

### Lỗi "Git not found"
- Cài Git từ git-scm.com
- Restart PowerShell

### Lỗi Authentication
- Dùng Personal Access Token (khuyến khích)
- Hoặc setup SSH key

### Lỗi "origin" đã tồn tại
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/monopoly-game.git
```

### Muốn xóa .venv khỏi git
```bash
git rm -r --cached .venv
git commit -m "Remove virtual environment"
```

---

## 💡 TIPS

1. **README.md** - GitHub sẽ hiển thị file này trên trang repo
2. **LICENSE** - Thêm file LICENSE nếu muốn open source
3. **.gitignore** - Đã tạo sẵn (bỏ qua __pycache__, .venv, vv)
4. **Commits rõ ràng** - Dùng meaningful commit messages

---

## 📊 REPO STRUCTURE TRÊN GITHUB

```
monopoly-game/
├── README.md                (Hướng dẫn chính)
├── INSTALL_VN.md            (Hướng dẫn Tiếng Việt)
├── API.md                   (Tài liệu API)
├── ADVANCED.md              (Tính năng nâng cao)
├── requirements.txt         (Dependencies)
├── config.py                (Cấu hình)
├── test_game.py             (Test suite)
├── examples.py              (Ví dụ)
├── quickstart.py            (Quick start)
│
├── core/                    (Game logic)
│   ├── game.py
│   ├── player.py
│   ├── board.py
│   ├── property.py
│   ├── dice.py
│   ├── card.py
│   └── utils.py
│
├── server/                  (Network server)
│   └── monopoly_server.py
│
├── client/                  (GUI client)
│   ├── game_client.py
│   └── game_ui.py
│
└── assets/                  (Game assets)
```

---

## 🎯 NEXT STEPS

1. **Cài Git** (nếu chưa có)
2. **Tạo GitHub repo**
3. **Chạy lệnh push bên trên**
4. **Share link GitHub repo với bạn bè!**

---

**Chúc bạn thành công!** 🚀
