import streamlit as st
import time
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Hệ Thống Var Premium", page_icon="🔥", layout="centered")

# --- HÀM PHÁT ÂM THANH & HIỆU ỨNG RUNG ---
def play_audio(url):
    md = f"""
        <audio autoplay="true" style="display:none;">
        <source src="{url}" type="audio/mp3">
        </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

def apply_shake_effect():
    # Đoạn CSS này tạo hiệu ứng rung lắc nhẹ cho toàn bộ trang web
    shake_css = """
    <style>
    @keyframes shake {
      0% { transform: translate(1px, 1px) rotate(0deg); }
      10% { transform: translate(-1px, -2px) rotate(-1deg); }
      20% { transform: translate(-3px, 0px) rotate(1deg); }
      30% { transform: translate(3px, 2px) rotate(0deg); }
      40% { transform: translate(1px, -1px) rotate(1deg); }
      50% { transform: translate(-1px, 2px) rotate(-1deg); }
      60% { transform: translate(-3px, 1px) rotate(0deg); }
      70% { transform: translate(3px, 1px) rotate(-1deg); }
      80% { transform: translate(-1px, -1px) rotate(1deg); }
      90% { transform: translate(1px, 2px) rotate(0deg); }
      100% { transform: translate(1px, -2px) rotate(-1deg); }
    }
    .stApp {
      animation: shake 0.5s;
      animation-iteration-count: infinite;
    }
    </style>
    """
    st.markdown(shake_css, unsafe_allow_html=True)

# --- KHO DỮ LIỆU CÂU HỎI ---
KHO_THUONG = [
    {"h": "Boy phố đi xe gì để leo top đêm nhanh nhất?", "d": "wave"},
    {"h": "Phong cách 'Jet Jet' thường đi kèm với bộ đồ hãng nào?", "d": "adidas"},
    {"h": "Khi leo top bị 'vẩy', hành động đầu tiên là gì?", "d": "var"},
    {"h": "Mức độ Premium cần đạt bao nhiêu điểm uy tín?", "d": "100"},
    {"h": "Tên Team của bạn là gì? (Team...)", "d": "Gugugaga"},
]

KHO_PREMIUM = [
    {"h": "Toán: Đạo hàm của sin(x) là gì?", "d": "cosx, cos(x), cos"},
    {"h": "Lý: Đơn vị của điện trở là gì?", "d": "ohm"},
    {"h": "Hóa: Ký hiệu hóa học của Vàng là gì?", "d": "Au"},
    {"h": "Anh: Quá khứ phân từ của 'Go' là gì?", "d": "gone, Gone"},
    {"h": "Toán: Căn bậc hai của 144 là bao nhiêu?", "d": "12"},
    {"h": "Lý: Công thức tính vận tốc v = s / ?", "d": "t, T, v = s/t"},
    {"h": "Hóa: Khí nào chiếm tỉ lệ cao nhất trong không khí?", "d": "Nito, N, Nitrogen"},
    {"h": "Anh: Trái nghĩa với 'Fast' là gì?", "d": "slow"},
    {"h": "Toán: Số Pi xấp xỉ bằng bao nhiêu (2 chữ số thập phân)?", "d": "3.14"},
    {"h": "Lý: Ai là người phát hiện ra định luật vạn vật hấp dẫn?", "d": "Newton"},
]

# --- KHỞI TẠO SESSION STATE ---
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'muc_do' not in st.session_state:
    st.session_state.muc_do = ""
if 'hiep_hien_tai' not in st.session_state:
    st.session_state.hiep_hien_tai = 1
if 'history_answers' not in st.session_state:
    st.session_state.history_answers = {}
if 'questions_to_use' not in st.session_state:
    st.session_state.questions_to_use = []

# --- GIAO DIỆN ---
st.title("🔥 HỆ THỐNG VAR - LEO TOP ĐÊM")

# --- BƯỚC 1: CHÀO MỪNG ---
if st.session_state.step == 1:
    st.header("Bước 1: Chào mừng")
    st.markdown("### 🗣️ 'Chan bố mày đi'")
    if st.button("🚀 Sẵn sàng var", use_container_width=True):
        st.session_state.step = 2
        st.rerun()

# --- BƯỚC 2: CHỦ ĐỀ ---
elif st.session_state.step == 2:
    st.header("Bước 2: Chủ đề")
    st.info("💡 Những cách leo top trong màn đêm của những boy phố, jet jet 🏍️")
    if st.button("🏁 Sẵn sàng leo top", use_container_width=True):
        st.session_state.step = 3
        st.rerun()

# --- BƯỚC 3: CHỌN MỨC ĐỘ ---
elif st.session_state.step == 3:
    st.header("Bước 3: Chọn mức độ")
    muc_do_chon = st.radio("Chọn phong cách của bạn:", ["Vừa, nhẹ nhàng", "Phong cách Premium", "Boy phố"])
    if st.button("Xác nhận mức độ", use_container_width=True):
        st.session_state.muc_do = muc_do_chon
        if muc_do_chon == "Phong cách Premium":
            temp_qs = KHO_PREMIUM.copy()
            random.shuffle(temp_qs)
            st.session_state.questions_to_use = temp_qs
        else:
            st.session_state.questions_to_use = KHO_THUONG
        st.session_state.step = 4
        st.rerun()

# --- BƯỚC 4: XỬ LÝ (AI) ---
elif st.session_state.step == 4:
    st.header("Bước 4: Hệ thống AI đang xử lý")
    with st.status("Đang chuẩn bị kịch bản và nhạc sàn...", expanded=True) as status:
        time.sleep(1.5)
        status.update(label="Hệ thống đã sẵn sàng!", state="complete")
    if st.button("Vào trận Var"):
        # Phát nhạc Vinahouse nếu là Boy Phố/Vừa
        if st.session_state.muc_do in ["Vừa, nhẹ nhàng", "Boy phố"]:
            play_audio("https://www.myinstants.com/media/sounds/vibe-vinahouse.mp3") 
        st.session_state.step = 5
        st.rerun()

# --- BƯỚC 5: KẾT QUẢ & ĐIỀN ĐÁP ÁN ---
elif st.session_state.step == 5:
    # Áp dụng hiệu ứng rung liên tục cho TẤT CẢ các mức độ, bao gồm cả Premium
    apply_shake_effect()

    total_qs = len(st.session_state.questions_to_use)
    diem_moi_cau = 100 / total_qs 
    
    st.header(f"🚀 {total_qs} Hiệp Leo Top")
    
    if 'show_result' not in st.session_state:
        st.session_state.show_result = False

    if not st.session_state.show_result:
        idx = st.session_state.hiep_hien_tai - 1
        cau = st.session_state.questions_to_use[idx]
        st.subheader(f"Hiệp {st.session_state.hiep_hien_tai}/{total_qs}")
        st.write(f"**Chế độ:** {st.session_state.muc_do}")
        st.write(f"**Thử thách:** {cau['h']}")
        
        ans_cu = st.session_state.history_answers.get(st.session_state.hiep_hien_tai, "")
        user_in = st.text_input("Điền câu trả lời:", value=ans_cu, key=f"i_{st.session_state.hiep_hien_tai}")
        st.session_state.history_answers[st.session_state.hiep_hien_tai] = user_in

        c1, c2, c3 = st.columns([1, 1, 2])
        with c1:
            if st.button("⬅️ Trước"):
                st.session_state.hiep_hien_tai = max(1, st.session_state.hiep_hien_tai - 1)
                st.rerun()
        with c2:
            if st.button("Sau ➡️"):
                st.session_state.hiep_hien_tai = min(total_qs, st.session_state.hiep_hien_tai + 1)
                st.rerun()
        with c3:
            if st.button("🏁 Kết thúc & Tính điểm"):
                st.session_state.show_result = True
                st.rerun()

    else:
        st.header("📊 Kết Quả Var Cuối Cùng")
        tong_diem = 0.0
        for i, c in enumerate(st.session_state.questions_to_use):
            user_ans = st.session_state.history_answers.get(i+1, "").strip().lower()
            if user_ans == c['d'].lower():
                tong_diem += diem_moi_cau

        tong_diem = round(tong_diem)
        st.subheader(f"Tổng điểm đạt được: {tong_diem}/100")

        # --- PHÂN HẠNG VÀ ÂM THANH ---
        if tong_diem >= 80:
            st.error("💎 HẠNG: CHIẾN THẦN LEO TOP (CAO NHẤT)")
            st.balloons()
            play_audio("https://www.myinstants.com/media/sounds/victory-sound-effect.mp3") 
        elif 50 <= tong_diem <= 70:
            st.warning("⚔️ HẠNG: CHIẾN TƯỚNG LEO TOP (HẠNG ỔN)")
        else:
            st.info("🐢 HẠNG: NGÔ LEO TOP (HẠNG CUỐI)")
            play_audio("https://www.myinstants.com/media/sounds/fail-sound-effect.mp3")

        if st.button("🔥 LÀM LẠI KÈO MỚI", use_container_width=True):
            st.session_state.clear()
            st.rerun()

# --- BƯỚC 6: XỬ LÝ LỖI ---
if st.session_state.step > 5:
    st.session_state.step = 1
    st.rerun()