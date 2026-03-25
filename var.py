import streamlit as st
import time

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
if muc_do == "Boy phố":
    kich_ban = [
        "Hiệp 1: Vít ga đầu ngõ - Jet jet!",
        "Hiệp 2: Đảo cánh phượng giữa phố đêm",
        "Hiệp 3: Var cực căng với các 'idol' khác",
        "Hiệp 4: Tăng tốc về đích, bỏ xa đối thủ",
        "Hiệp 5: Chốt kèo, nhận danh hiệu Trùm Boy Phố"
    ]
elif muc_do == "Phong cách Premium":
    kich_ban = [
        "Hiệp 1: Xuất hiện thanh lịch, lên đồ cực bảnh",
        "Hiệp 2: Di chuyển mượt mà trên các cung đường đẹp",
        # ... tiếp tục cho các hiệp khác
    ]
    
    # Giả lập AI đang phân tích
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    
    st.success(f"Đã phân tích xong phong cách: {st.session_state.muc_do}")
    if st.button("Xem kết quả"):
        go_to_step(5)

# --- BƯỚC 5: KẾT QUẢ ---
elif st.session_state.step == 5:
    st.header("Kết quả: 5 hiệp leo top")
    st.write(f"Trạng thái: Đang chuẩn bị var mức độ **{st.session_state.muc_do}**")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("Bắt đầu var"):
            st.toast("🚀 Đang lên số... Jet jet!")
    with col2:
        if st.button("Dừng var"):
            st.toast("🛑 Phanh gấp!")
    with col3:
        if st.button("Tiếp tục var"):
            st.toast("⏭️ Vào số lại ngay")
    with col4:
        if st.button("Kết thúc var"):
            st.balloons()
            st.success("Kèo var kết thúc rực rỡ!")
            if st.button("Làm lại kèo mới"):
                go_to_step(1)

# --- Xử lý lỗi bước (Phòng trường hợp session bị trống) ---
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Có lỗi xảy ra trong quá trình chọn bước.")
    if st.button("Quay lại trang chủ"):
        go_to_step(1)