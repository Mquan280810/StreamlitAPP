import streamlit as st
import random
import time

# --- CẤU HÌNH HỆ THỐNG ---
st.set_page_config(page_title="Hệ Thống Var Leo Top", page_icon="⚡")

# Kho câu hỏi dùng chung cho Bước 5
KHO_CAU_HOI = [
    {"h": "Toán: $x^2 - 16 = 0$. Tìm x dương?", "d": "4, x=4, x = 4", "p": 20},
    {"h": "Vật Lý: Đơn vị của lực (F) là gì?", "d": "Newton, N", "p": 20},
    {"h": "Tiếng Anh: 'Apple' tiếng Việt là gì?", "d": "Táo, Qủa Táo, táo, Qủa táo, quả táo", "p": 10},
    {"h": "Toán: Căn bậc hai của 81 là mấy?", "d": "9", "p": 20},
    {"h": "Vật Lý: Công thức tính Vận tốc v = s / ?", "d": "t, v=s/t, v = s / t", "p": 30}
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
    st.header("🚀 5 Hiệp Leo Top")
    
    # Khởi tạo trạng thái hiển thị kết quả nếu chưa có
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False

    # Nếu chưa nhấn kết thúc, hiển thị bộ câu hỏi
    if not st.session_state.show_result:
        idx = st.session_state.hiep_hien_tai - 1
        cau = KHO_CAU_HOI[idx]
        st.subheader(f"Hiệp {st.session_state.hiep_hien_tai}/5")
        st.write(f"Thử thách: {cau['h']}")
        
        ans_cu = st.session_state.history_answers.get(st.session_state.hiep_hien_tai, "")
        user_in = st.text_input("Đáp án:", value=ans_cu, key=f"i_{st.session_state.hiep_hien_tai}")
        st.session_state.history_answers[st.session_state.hiep_hien_tai] = user_in

        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            if st.button("⬅️ Trước", key="btn_p"):
                if st.session_state.hiep_hien_tai > 1:
                    st.session_state.hiep_hien_tai -= 1
                    st.rerun()
        with c2:
            if st.button("Sau ➡️", key="btn_n"):
                if st.session_state.hiep_hien_tai < 5:
                    st.session_state.hiep_hien_tai += 1
                    st.rerun()
        with c3:
            if st.button("🏁 Kết thúc var", key="btn_f"):
                st.session_state.show_result = True
                st.rerun()

    # MÀN HÌNH HIỂN THỊ HẠNG (Sau khi đã bấm Kết thúc)
    else:
        st.balloons()
        tong = 0
        for i, c in enumerate(KHO_CAU_HOI):
            if st.session_state.history_answers.get(i+1, "").strip().lower() == c['d'].lower():
                tong += c['p']
        
        st.header(f"📊 Tổng kết: {tong} điểm")
        
        if tong >= 80: st.error("💎 HẠNG: CHIẾN THẦN LEO TOP")
        elif tong >= 50: st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP")
        else: st.info("🐢 HẠNG: NGÔ LEO TOP")
        
        st.markdown("---")
        # Nút này bây giờ nằm độc lập, bấm phát là clear sạch sẽ
        if st.button("🔥 LÀM LẠI KÈO MỚI (VỀ BƯỚC 1)", key="redo_final"):
            st.session_state.clear()
            st.rerun()

# BƯỚC 6: XỬ LÝ LỖI ĐIỀU HƯỚNG
if st.session_state.step not in [1, 2, 3, 4, 5]:
    st.error("Hệ thống gặp lỗi chọn bước!")
    if st.button("Quay lại trang chủ", key="error_back"):
        go_to_step(1)