import streamlit as st
import random
import time

# --- 1. DỮ LIỆU CÂU HỎI (Team Gugugaga) ---
KHO_CAU_HOI = [
    {"h": "Toán: $x^2 - 16 = 0$. Tìm x dương?", "d": "4", "p": 20},
    {"h": "Vật Lý: Đơn vị của lực (F) là gì?", "d": "Newton", "p": 20},
    {"h": "Tiếng Anh: 'Apple' tiếng Việt là gì?", "d": "Táo", "p": 10},
    {"h": "Toán: Căn bậc hai của 81 là mấy?", "d": "9", "p": 20},
    {"h": "Vật Lý: Công thức tính Vận tốc v = s / ?", "d": "t", "p": 30}
]

# --- 2. KHỞI TẠO SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'history_answers' not in st.session_state:
    st.session_state.history_answers = {}
if 'hiep_hien_tai' not in st.session_state:
    st.session_state.hiep_hien_tai = 1
if 'show_result' not in st.session_state:
    st.session_state.show_result = False

def go_to_step(s):
    st.session_state.step = s
    st.rerun()

# --- 3. GIAO DIỆN CHÍNH ---
st.title("⚡ Hệ Thống Var Premium - Angless")

# BƯỚC 1: CHÀO MỪNG
if st.session_state.step == 1:
    st.subheader("Chào mừng: Chan bố mày đi")
    if st.button("Sẵn sàng var", key="btn_s1"): go_to_step(2)

# BƯỚC 2: CHỦ ĐỀ
elif st.session_state.step == 2:
    st.subheader("Chủ đề: Leo top đêm khuya phong cách boy phố")
    if st.button("Sẵn sàng leo top", key="btn_s2"): go_to_step(3)

# BƯỚC 3: MỨC ĐỘ
elif st.session_state.step == 3:
    st.subheader("Chọn mức độ var")
    st.session_state.muc_do = st.radio("Phong cách:", ["Vừa", "Premium", "Boy phố"], key="r_lv")
    if st.button("Xác nhận", key="btn_s3"): go_to_step(4)

# BƯỚC 4: XỬ LÝ
elif st.session_state.step == 4:
    st.info("AI đang quét dữ liệu hệ thống...")
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i + 1)
    st.success("Hệ thống đã sẵn sàng cho 5 hiệp leo top!")
    if st.button("Vào đấu trường", key="btn_s4"): go_to_step(5)

# BƯỚC 5: KẾT QUẢ & RESET SẠCH
elif st.session_state.step == 5:
    st.header("🚀 5 Hiệp Leo Top Khốc Liệt")
    
    # CHẾ ĐỘ 1: ĐANG TRẢ LỜI CÂU HỎI
    if not st.session_state.show_result:
        idx = st.session_state.hiep_hien_tai - 1
        cau = KHO_CAU_HOI[idx]
        st.subheader(f"Hiệp {st.session_state.hiep_hien_tai}/5")
        st.write(f"Thử thách: {cau['h']}")
        
        # Ô nhập liệu lấy từ lịch sử (Cho phép sửa đáp án)
        ans_cu = st.session_state.history_answers.get(st.session_state.hiep_hien_tai, "")
        user_in = st.text_input("Đáp án của bạn:", value=ans_cu, key=f"i_{st.session_state.hiep_hien_tai}")
        st.session_state.history_answers[st.session_state.hiep_hien_tai] = user_in

        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            if st.button("⬅️ Trước", key="btn_back"):
                if st.session_state.hiep_hien_tai > 1:
                    st.session_state.hiep_hien_tai -= 1
                    st.rerun()
        with c2:
            if st.button("Sau ➡️", key="btn_next"):
                if st.session_state.hiep_hien_tai < 5:
                    st.session_state.hiep_hien_tai += 1
                    st.rerun()
        with c3:
            if st.button("🏁 Kết thúc var", key="btn_finish"):
                st.session_state.show_result = True
                st.rerun()

    # CHẾ ĐỘ 2: HIỂN THỊ HẠNG VÀ RESET
    else:
        st.balloons()
        tong = 0
        for i, c in enumerate(KHO_CAU_HOI):
            user_ans = st.session_state.history_answers.get(i+1, "").strip().lower()
            if user_ans == c['d'].lower():
                tong += c['p']
        
        st.header(f"📊 Tổng kết: {tong} điểm")
        
        # Phân hạng theo yêu cầu
        if tong >= 80: st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
        elif tong >= 50: st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
        else: st.info("🐢 HẠNG: NGÔ LEO TOP")
        
        st.markdown("---")
        # NÚT RESET SẠCH VỀ BƯỚC 1
        if st.button("🔥 LÀM LẠI KÈO MỚI (RESET SẠCH)", key="redo_all"):
            st.session_state.clear() # Xóa toàn bộ dữ liệu session
            st.rerun() # Khởi động lại ứng dụng từ đầu

# --- XỬ LÝ LỖI ĐIỀU HƯỚNG ---
if st.session_state.step not in [1, 2, 3, 4, 5]:
    if st.button("Quay lại trang chủ"):
        st.session_state.clear()
        st.rerun()