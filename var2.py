import streamlit as st
import random
import time

# --- 1. CẤU HÌNH & KHO DỮ LIỆU ---
st.set_page_config(page_title="Hệ Thống Var Leo Top", page_icon="🔥")

# Kho câu hỏi cố định cho 5 hiệp
KHO_CAU_HOI = [
    {"h": "Toán: $x^2 - 16 = 0$. Tìm x dương?", "d": "4", "p": 20},
    {"h": "Vật Lý: Đơn vị của lực (F) là gì?", "d": "Newton", "p": 20},
    {"h": "Tiếng Anh: 'Apple' tiếng Việt là gì?", "d": "Táo", "p": 10},
    {"h": "Toán: Căn bậc hai của 81 là mấy?", "d": "9", "p": 20},
    {"h": "Vật Lý: Công thức tính Vận tốc v = s / ?", "d": "t", "p": 30}
]

# Khởi tạo Session State (Bộ nhớ tạm của ứng dụng)
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'history_answers' not in st.session_state:
    st.session_state.history_answers = {}  # Lưu đáp án để có thể quay lại sửa
if 'hiep_hien_tai' not in st.session_state:
    st.session_state.hiep_hien_tai = 1

def go_to_step(next_step):
    st.session_state.step = next_step
    st.rerun()

# --- 2. GIAO DIỆN CHÍNH ---
st.title("⚡ Hệ Thống Var Premium - Angless")

# BƯỚC 1: CHÀO MỪNG
if st.session_state.step == 1:
    st.subheader("Chào mừng: Chan bố mày đi")
    if st.button("Sẵn sàng var", key="btn_step1"):
        go_to_step(2)

# BƯỚC 2: CHỦ ĐỀ
elif st.session_state.step == 2:
    st.subheader("Chủ đề: Những cách leo top trong màn đêm của những boy phố, jet jet")
    if st.button("Sẵn sàng leo top", key="btn_step2"):
        go_to_step(3)

# BƯỚC 3: CHỌN MỨC ĐỘ
elif st.session_state.step == 3:
    st.subheader("Chọn mức độ var")
    st.session_state.muc_do = st.radio(
        "Chọn phong cách của bạn:",
        ["Vừa, nhẹ nhàng", "Phong cách Premium", "Boy phố"],
        key="radio_level"
    )
    if st.button("Xác nhận mức độ", key="btn_step3"):
        go_to_step(4)

# BƯỚC 4: XỬ LÝ (AI)
elif st.session_state.step == 4:
    st.info("AI đang quét dữ liệu boy phố...")
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i + 1)
    st.success("Xử lý xong! Đã lên số sẵn sàng.")
    if st.button("Tiến vào 5 hiệp var", key="btn_step4"):
        go_to_step(5)

# BƯỚC 5: KẾT QUẢ & VAR (CÓ QUAY LẠI CÂU CŨ)
elif st.session_state.step == 5:
    st.header("🚀 Đấu Trường 5 Hiệp Leo Top")
    
    # Hiển thị hiệp hiện tại
    idx = st.session_state.hiep_hien_tai - 1
    cau = KHO_CAU_HOI[idx]
    
    st.subheader(f"Hiệp {st.session_state.hiep_hien_tai}/5")
    st.markdown(f"**Thử thách:** {cau['h']}")
    
    # Lấy lại đáp án cũ từ bộ nhớ history nếu có
    dap_an_cu = st.session_state.history_answers.get(st.session_state.hiep_hien_tai, "")
    user_input = st.text_input("Nhập/Sửa đáp án của bạn:", value=dap_an_cu, key=f"input_hiep_{st.session_state.hiep_hien_tai}")
    
    # Lưu đáp án ngay vào bộ nhớ khi người dùng nhập
    st.session_state.history_answers[st.session_state.hiep_hien_tai] = user_input

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⬅️ Câu trước", key="btn_back"):
            if st.session_state.hiep_hien_tai > 1:
                st.session_state.hiep_hien_tai -= 1
                st.rerun()
                
    with col2:
        if st.button("Câu tiếp ➡️", key="btn_next"):
            if st.session_state.hiep_hien_tai < 5:
                st.session_state.hiep_hien_tai += 1
                st.rerun()
            else:
                st.warning("Đã hết hiệp! Nhấn Kết thúc để xem hạng.")

    with col4:
        if st.button("Kết thúc var", key="btn_finish"):
            st.balloons()
            # Tính điểm tổng từ các đáp án đã lưu
            tong = 0
            for i in range(1, 6):
                ans = st.session_state.history_answers.get(i, "").strip().lower()
                real = KHO_CAU_HOI[i-1]['d'].lower()
                if ans == real:
                    tong += KHO_CAU_HOI[i-1]['p']
            
            st.markdown("---")
            st.header(f"📊 Tổng kết: {tong} điểm")
            
            # Phân hạng
            if tong >= 80:
                st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
            elif 50 <= tong < 80:
                st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
            else:
                st.info("🐢 HẠNG: NGÔ LEO TOP")
            
            # NÚT RESET SẠCH VỀ BƯỚC 1
            if st.button("Làm lại kèo mới (Reset sạch)", key="redo_all"):
                st.session_state.clear()
                st.rerun()

# BƯỚC 6: XỬ LÝ LỖI CHỌN
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Lỗi điều hướng!")
    if st.button("Quay lại đầu", key="btn_error"):
        go_to_step(1)