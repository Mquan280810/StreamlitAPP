import streamlit as st
import time
import random

#

# Thiết lập cấu hình trang
st.set_page_config(page_title="Hệ Thống Var Premium", page_icon="⚡")

# Khởi tạo session state để quản lý các bước
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'muc_do' not in st.session_state:
    st.session_state.muc_do = ""

# --- Bước 6: Hàm xử lý lỗi điều hướng (Logic check) ---
def go_to_step(next_step):
    st.session_state.step = next_step

# Giao diện chính
st.title("🔥 Hệ Thống Var - Team Gugugaga")

# --- BƯỚC 1: CHÀO MỪNG ---
if st.session_state.step == 1:
    st.subheader("Chào mừng: Chan bố mày đi")
    if st.button("Sẵn sàng var"):
        go_to_step(2)

# --- BƯỚC 2: CHỦ ĐỀ ---
elif st.session_state.step == 2:
    st.subheader("Chủ đề: Những cách leo top trong màn đêm của những boy phố, jet jet")
    if st.button("Sẵn sàng leo top"):
        go_to_step(3)

# --- BƯỚC 3: CHỌN MỨC ĐỘ ---
elif st.session_state.step == 3:
    st.subheader("Chọn mức độ var")
    muc_do = st.radio(
        "Chọn phong cách của bạn:",
        ["Vừa, nhẹ nhàng", "Phong cách Premium", "Boy phố"]
    )
    if st.button("Xác nhận mức độ"):
        st.session_state.muc_do = muc_do
        go_to_step(4)

# --- BƯỚC 4: XỬ LÝ (AI) ---
elif st.session_state.step == 4:
    st.info("Đang xử lý...")
    progress_bar = st.progress(0)

# Ví dụ logic xử lý mức độ
#if muc_do == "Boy phố":
  #  kich_ban = [
   # 
    # Giả lập AI đang phân tích
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    
    st.success(f"Đã phân tích xong phong cách: {st.session_state.muc_do}")
    if st.button("Xem kết quả"):
        go_to_step(5)

# --- BƯỚC 5: KẾT QUẢ ---
KHO_CAU_HOI = [
    {"h": "Toán: $x^2 - 16 = 0$. Tìm x dương?", "d": "4", "p": 20},
    {"h": "Vật Lý: Đơn vị của lực (F) là gì?", "d": "Newton", "p": 20},
    {"h": "Tiếng Anh: 'Apple' tiếng Việt là gì?", "d": "Táo", "p": 10},
    {"h": "Toán: Căn bậc hai của 81 là mấy?", "d": "9", "p": 20},
    {"h": "Vật Lý: Công thức tính Vận tốc v = s / ?", "d": "t", "p": 30}
]

elif st.session_state.step == 5:
    st.header("🚀 Đấu Trường Leo Top: 5 Hiệp Var Khốc Liệt")

    # Khởi tạo điểm và danh sách câu hỏi nếu mới vào bước 5
    if 'tong_diem' not in st.session_state:
        st.session_state.tong_diem = 0
        st.session_state.hiep_hien_tai = 1
        st.session_state.cau_hien_tai = random.choice(KHO_CAU_HOI)
        st.session_state.da_tra_loi = False

    vung_var = st.empty()

    with vung_var.container():
        st.subheader(f"🔥 Hiệp {st.session_state.hiep_hien_tai}/5")
        st.markdown(f"**Thử thách:** {st.session_state.cau_hien_tai['h']}")
        
        user_input = st.text_input("Nhập đáp án của bạn:", key=f"input_hiep_{st.session_state.hiep_hien_tai}")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("Bắt đầu var (Gửi)", key="btn_check"):
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
        if st.button("Tiếp tục var (Hiệp tới)", key="btn_next"):
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

            # Phân hạng theo yêu cầu
            if tong >= 80:
                st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
            elif 50 <= tong < 80:
                st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
            else:
                st.info("🐢 HẠNG: NGÔ LEO TOP")

            if st.button("Làm lại kèo mới"):
                # Reset sạch sẽ session
                for key in ['tong_diem', 'hiep_hien_tai', 'cau_hien_tai', 'da_tra_loi']:
                    del st.session_state[key]
                st.session_state.step = 1
                st.rerun()
# --- Xử lý lỗi bước (Phòng trường hợp session bị trống) ---
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Có lỗi xảy ra trong quá trình chọn bước.")
    if st.button("Quay lại trang chủ"):
        go_to_step(1)