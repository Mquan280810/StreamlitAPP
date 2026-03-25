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
elif st.session_state.step == 5:
    st.header("🚀 Kết quả: 5 Hiệp Leo Top Toán Học")
    
    # Tạo vùng trống hiển thị nội dung var
    vung_var = st.empty()
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Sử dụng tham số key để tránh lỗi DuplicateElementId
    with col1:
        if st.button("Bắt đầu var", key="btn_start"):
            with vung_var.container():
                st.markdown("### 🔥 HIỆP 1: KHỞI ĐỘNG")
                st.write("Đối thủ tung chiêu: $x^2 - 4 = 0$. Bạn có 3 giây để 'vít ga' tìm x!")
                st.warning("Hành động: Đang check var đáp án...")
                
    with col2:
        if st.button("Dừng var", key="btn_stop"):
            vung_var.error("🛑 Đã phanh gấp! Đang giữ khoảng cách với đề bài.")
            
    with col3:
        if st.button("Tiếp tục var", key="btn_continue"):
            with vung_var.container():
                st.markdown("### 🔥 HIỆP tiếp theo: TĂNG TỐC")
                st.write("Đang vào số với phương trình chứa tham số $m$...")
                st.info("Hành động: AI đang quét sạch các nghiệm ảo!")
                
    with col4:
        if st.button("Kết thúc var", key="btn_finish"):
            st.balloons()
            # Xử lý tính điểm ngẫu nhiên dựa trên mức độ đã chọn từ Bước 3
            diem = random.randint(0, 100)
            
            with vung_var.container():
                st.success(f"🏆 Kèo var rực rỡ! Bạn đạt được **{diem} điểm**.")
                
                # Phân hạng theo yêu cầu của Angless
                if diem >= 80:
                    st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
                    st.write("Đẳng cấp của bạn là không thể bàn cãi!")
                elif 50 <= diem < 80:
                    st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
                    st.write("Điểm số rất ổn định, phong cách rất Premium.")
                else:
                    st.info("🐢 HẠNG: NGÔ LEO TOP")
                    st.write("Chưa có điểm rực rỡ. Cần nạp thêm xăng để leo top nhé!")
                
                if st.button("Làm lại kèo mới", key="btn_reset"):
                    st.session_state.step = 1
                    st.rerun()

# --- Xử lý lỗi bước (Phòng trường hợp session bị trống) ---
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Có lỗi xảy ra trong quá trình chọn bước.")
    if st.button("Quay lại trang chủ"):
        go_to_step(1)