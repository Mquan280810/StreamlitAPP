import streamlit as st
import random
import time

# --- 1. CẤU HÌNH & DỮ LIỆU ---
st.set_page_config(page_title="Hệ Thống Var Leo Top", page_icon="🔥")

# Kho câu hỏi cố định để tính điểm chính xác cho 5 hiệp
KHO_CAU_HOI = [
    {"h": "Toán: $x^2 - 16 = 0$. Tìm x dương?", "d": "4", "p": 20},
    {"h": "Vật Lý: Đơn vị của lực (F) là gì?", "d": "Newton", "p": 20},
    {"h": "Tiếng Anh: 'Apple' tiếng Việt là gì?", "d": "Táo", "p": 10},
    {"h": "Toán: Căn bậc hai của 81 là mấy?", "d": "9", "p": 20},
    {"h": "Vật Lý: Công thức tính Vận tốc v = s / ?", "d": "t", "p": 30}
]

# Khởi tạo Session State
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'history_answers' not in st.session_state:
    st.session_state.history_answers = {}  # Lưu đáp án người dùng nhập
if 'hiep_hien_tai' not in st.session_state:
    st.session_state.hiep_hien_tai = 1
if 'tong_diem' not in st.session_state:
    st.session_state.tong_diem = 0

def go_to_step(next_step):
    st.session_state.step = next_step
    st.rerun()

# --- 2. GIAO DIỆN CHÍNH ---
st.title("⚡ Hệ Thống Var Premium - Angless")

# --- BƯỚC 1: CHÀO MỪNG ---
if st.session_state.step == 1:
    st.subheader("Chào mừng: Chan bố mày đi")
    if st.button("Sẵn sàng var", key="btn_s1"):
        go_to_step(2)

# --- BƯỚC 2: CHỦ ĐỀ ---
elif st.session_state.step == 2:
    st.subheader("Chủ đề: Cách leo top đêm khuya của boy phố, jet jet")
    if st.button("Sẵn sàng leo top", key="btn_s2"):
        go_to_step(3)

# --- BƯỚC 3: CHỌN MỨC ĐỘ ---
elif st.session_state.step == 3:
    st.subheader("Chọn mức độ var")
    st.session_state.muc_do = st.radio(
        "Chọn phong cách của bạn:",
        ["Vừa, nhẹ nhàng", "Phong cách Premium", "Boy phố"],
        key="radio_muc_do"
    )
    if st.button("Xác nhận mức độ", key="btn_s3"):
        go_to_step(4)

# --- BƯỚC 4: XỬ LÝ (AI) ---
elif st.session_state.step == 4:
    st.info("AI đang phân tích chiến thuật leo top...")
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i + 1)
    st.success("Đang xử lý xong! Sẵn sàng vào việc.")
    if st.button("Bắt đầu hiệp đấu", key="btn_s4"):
        go_to_step(5)

# --- BƯỚC 5: KẾT QUẢ & VAR ---
elif st.session_state.step == 5:
    st.header("🚀 5 Hiệp Leo Top Khốc Liệt")
    
    # Hiển thị câu hỏi dựa trên hiệp hiện tại
    idx = st.session_state.hiep_hien_tai - 1
    cau = KHO_CAU_HOI[idx]
    
    st.subheader(f"Hiệp {st.session_state.hiep_hien_tai}/5")
    st.markdown(f"**Thử thách:** {cau['h']}")
    
    # Lấy lại đáp án cũ nếu đã nhập
    cu = st.session_state.history_answers.get(st.session_state.hiep_hien_tai, "")
    user_input = st.text_input("Nhập đáp án của bạn:", value=cu, key=f"inp_{st.session_state.hiep_hien_tai}")
    
    # Lưu đáp án ngay khi nhập để không bị mất khi chuyển câu
    st.session_state.history_answers[st.session_state.hiep_hien_tai] = user_input

    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⬅️ Câu trước", key="btn_prev"):
            if st.session_state.hiep_hien_tai > 1:
                st.session_state.hiep_hien_tai -= 1
                st.rerun()
                
    with col2:
        if st.button("Câu tiếp ➡️", key="btn_next"):
            if st.session_state.hiep_hien_tai < 5:
                st.session_state.hiep_hien_tai += 1
                st.rerun()
            else:
                st.warning("Đã hết 5 hiệp! Nhấn Kết thúc để check var.")

    with col4:
        if st.button("Kết thúc var", key="btn_finish"):
            st.balloons()
            # Tính điểm tổng kết
            tong = 0
            for i in range(1, 6):
                ans = st.session_state.history_answers.get(i, "").strip().lower()
                real = KHO_CAU_HOI[i-1]['d'].lower()
                if ans == real:
                    tong += KHO_CAU_HOI[i-1]['p']
            
            st.markdown("---")
            st.header(f"📊 Tổng điểm: {tong}")
            
            # Phân hạng
            if tong >= 80:
                st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
            elif 50 <= tong < 80:
                st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
            else:
                st.info("🐢 HẠNG: NGÔ LEO TOP")
            
            # Làm lại kèo mới quay lại Bước 3
            if st.button("Làm lại kèo mới", key="btn_reset_3"):
                st.session_state.history_answers = {}
                st.session_state.hiep_hien_tai = 1
                go_to_step(3)

# --- BƯỚC 6: XỬ LÝ LỖI ---
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Lỗi điều hướng hệ thống!")
    if st.button("Quay lại", key="btn_err"):
        go_to_step(1)