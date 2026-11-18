# Buổi 6 - Docker, Testing, CI
# Môi trường
- OS: Windows 11
- Docker version: Docker version 29.9.3
- Python / Node version: Python 3.14.7
# Kết quả local
+) Backend
- pytest backend/tests -q: .. [100%] 2 passed in 6.68s
+) Frontend
- npm test: 
- npm run build: PASS
- Phiên bản Vite: 7.1.7
- Số modules được chuyển đổi: 33.
- Build hoàn thành trong 348 ms.
+) Docker
- docker compose up --build: Build trong 2,8s 
## Một luồng tích hợp đã kiểm tra
- Request: Frontend => Nginx => FastAPI => PostgreSQL
## Debug / AI
+) Lỗi gặp phải:
- Docker không kết nối DockerAPI
- Bằng chứng đã xem: Thông báo The system cannot find the file specified.
- Window chặn pytest.exe
- Bằng chứng đã xem: PowerShell hiển thị lỗi ApplicationFailedException.
- Nếu dùng AI: gợi ý nào đã dùng và đã xác minh thế nào?
-> Tìm ra nguyên nhân lỗi và đề xuất cách kiểm tra + giải quyết