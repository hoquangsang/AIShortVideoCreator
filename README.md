# **AI Short Video Creator** 
Nền tảng tạo video ngắn theo xu hướng bằng trí tuệ nhân tạo.

> 🎯 Mục tiêu
- Tạo video ngắn học thuật, truyền thông, giải trí, lan tỏa kiến thức.
- Hỗ trợ sinh viên, người học thực hành với công nghệ AI đa phương tiện hiện đại.

> ⚙️ Chức năng chính
- **F1:** Gợi ý chủ đề theo xu hướng (API trend, từ khóa)
- **F2:** Sinh kịch bản video tự động (AI LLM)
- **F3:** Tạo giọng đọc AI (Text-to-Speech)
- **F4:** Tạo video tự động (ghép ảnh, voice, phụ đề)
- **F5:** Chỉnh sửa cơ bản (hiệu ứng chữ, sticker, nhạc nền)
- **F6:** Xuất video (.mp4)
- **F7:** Quản lý video đã tạo

> 🚀 Công nghệ sử dụng
- **Backend:** Python (FastAPI)
- **Frontend:** ReactJS/Next.js

---
## 🗂️ Cấu trúc thư mục

```plaintext
project/
│
├── backend/
│   └── ...
│
├── frontend/
│   └── ...
```
---

## ▶️ Hướng dẫn chạy dự án

### 0. **Yêu cầu hệ thống**

* **Python** >= 3.9
* **Node.js** >= 18.x (khuyến nghị dùng LTS)

### 1. **Khởi chạy Backend (FastAPI)**
> Di chuyển tới thư mục Backend
```bash
cd backend
```

> Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

> Chạy server:
```bash
python run.py
```
- Tài liệu API (Swagger UI): [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2. **Khởi chạy Frontend (React)**
> Di chuyển tới thư mục Frontend
```bash
cd frontend
```

> Cài đặt dependencies:
```bash
npm install
```

> Chạy ứng dụng:
```bash
npm run dev
```
- Truy cập tại: [http://localhost:5173](http://localhost:5173)

---

## 📢 Liên hệ & Đóng góp
Dự án được viết lại dựa trên **lab môn học Thiết kế Phần mềm – HCMUS** của team.