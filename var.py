import streamlit as st
import random
import time

# --- CẤU HÌNH HỆ THỐNG ---
st.set_page_config(page_title="Hệ Thống Var Leo Top", page_icon="⚡")

# Kho câu hỏi dùng chung cho Bước 5
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
if 'tong_diem' not in st.session_state:
    st.session_state.tong_diem = 0
if 'hiep_hien_tai' not in st.session_state:
    st.session_state.hiep_hien_tai = 1
if 'cau_hien_tai' not in st.session_state:
    st.session_state.cau_hien_tai = random.choice(KHO_CAU_HOI)
if 'da_tra_loi' not in st.session_state:
    st.session_state.da_tra_loi = False

def go_to_step(next_step):
    st.session_state.step = next_step
    st.rerun()

# --- GIAO DIỆN CHÍNH ---
st.title("🔥 Hệ Thống Var - Team Gugugaga")

# BƯỚC 1: CHÀO MỪNG
if st.session_state.step == 1:
    st.subheader("Chào mừng: Chan bố mày đi")
    if st.button("Sẵn sàng var", key="start_1"):
        go_to_step(2)

# BƯỚC 2: CHỦ ĐỀ
elif st.session_state.step == 2:
    st.subheader("Chủ đề: Những cách leo top trong màn đêm của những boy phố, jet jet")
    if st.button("Sẵn sàng leo top", key="start_2"):
        go_to_step(3)

# BƯỚC 3: CHỌN MỨC ĐỘ
elif st.session_state.step == 3:
    st.subheader("Chọn mức độ var")
    st.session_state.muc_do = st.radio(
        "Chọn phong cách của bạn:",
        ["Vừa, nhẹ nhàng", "Phong cách Premium", "Boy phố"],
        key="radio_level"
    )
    if st.button("Xác nhận mức độ", key="start_3"):
        go_to_step(4)

# BƯỚC 4: XỬ LÝ (AI)
elif st.session_state.step == 4:
    st.info("Đang xử lý hệ thống var...")
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        progress_bar.progress(percent_complete + 1)
    st.success("Hệ thống đã sẵn sàng cho 5 hiệp leo top!")
    if st.button("Tiến vào đấu trường", key="start_4"):
        go_to_step(5)

# BƯỚC 5: KẾT QUẢ & VAR
elif st.session_state.step == 5:
    st.header("🚀 Đấu Trường Leo Top: 5 Hiệp Var Khốc Liệt")
    
    vung_var = st.empty()
    
    with vung_var.container():
        st.subheader(f"🔥 Hiệp {st.session_state.hiep_hien_tai}/5")
        st.markdown(f"**Thử thách:** {st.session_state.cau_hien_tai['h']}")
        user_input = st.text_input("Nhập đáp án của bạn:", key=f"input_hiep_{st.session_state.hiep_hien_tai}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Bắt đầu var (Gửi)", key=f"btn_check_{st.session_state.hiep_hien_tai}"):
            if not user_input:
                st.warning("⚠️ Đừng múa máy, điền đáp án đi bạn ơi!")
            elif user_input.lower() == st.session_state.cau_hien_tai['d'].lower():
                if not st.session_state.da_tra_loi:
                    st.session_state.tong_diem += st.session_state.cau_hien_tai['p']
                    st.session_state.da_tra_loi = True
                st.success(f"✅ Quá gắt! +{st.session_state.cau_hien_tai['p']} điểm.")
            else:
                st.error(f"❌ Xòe rồi! Đáp án đúng là: {st.session_state.cau_hien_tai['d']}")
                st.session_state.da_tra_loi = True

    with col3:
        if st.button("Tiếp tục var", key=f"btn_next_{st.session_state.hiep_hien_tai}"):
            if st.session_state.hiep_hien_tai < 5:
                st.session_state.hiep_hien_tai += 1
                st.session_state.cau_hien_tai = random.choice(KHO_CAU_HOI)
                st.session_state.da_tra_loi = False
                st.rerun()
            else:
                st.info("🏁 Đã hết 5 hiệp! Nhấn 'Kết thúc' để xem hạng.")

    with col4:
        if st.button("Kết thúc var", key="btn_finish_final"):
            st.balloons()
            tong = st.session_state.tong_diem
            st.markdown("---")
            st.header(f"📊 Tổng điểm tích lũy: {tong} điểm")

            if tong >= 80:
                st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
                st.write("Đúng là boy phố học Toán, khét lẹt!")
            elif 50 <= tong < 80:
                st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
                st.write("Phong cách Premium, xử lý rất ổn định.")
            else:
                st.info("🐢 HẠNG: NGÔ LEO TOP")
                st.write("Cố gắng ở hiệp sau nhé!")

            if st.button("Làm lại kèo mới", key="btn_reset_game"):
                for key in ['tong_diem', 'hiep_hien_tai', 'cau_hien_tai', 'da_tra_loi']:
                    del st.session_state[key]
                go_to_step(1)

# BƯỚC 6: XỬ LÝ LỖI ĐIỀU HƯỚNG
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Hệ thống gặp lỗi chọn bước!")
    if st.button("Quay lại trang chủ", key="error_back"):
        go_to_step(1)