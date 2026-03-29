import streamlit as st
import sqlite3

# --- PHẦN 1: XỬ LÝ DỮ LIỆU (SQLITE) ---
def db_query(query, params=(), fetch=False, commit=False):
    conn = sqlite3.connect('saving_data.db')
    c = conn.cursor()
    c.execute(query, params)
    data = c.fetchone() if fetch else None
    if commit: conn.commit()
    conn.close()
    return data

# Khởi tạo bảng
db_query('CREATE TABLE IF NOT EXISTS users (u TEXT PRIMARY KEY, p TEXT)', commit=True)
db_query('CREATE TABLE IF NOT EXISTS goals (u TEXT, name TEXT, target REAL, saved REAL DEFAULT 0)', commit=True)

# --- PHẦN 2: GIAO DIỆN ĐĂNG NHẬP / ĐĂNG KÝ ---
st.set_page_config("Saving Pro 6", "💰")

if 'user' not in st.session_state:
    st.title("🔐 Hệ thống E-BIKE SAVING")
    tab1, tab2 = st.tabs(["Đăng Nhập", "Đăng Ký"])
    
    with tab1:
        u, p = st.text_input("Tài khoản"), st.text_input("Mật khẩu", type="password")
        if st.button("Vào hệ thống"):
            res = db_query('SELECT u FROM users WHERE u=? AND p=?', (u, p), fetch=True)
            if res: st.session_state.user = u; st.rerun()
            else: st.error("Sai thông tin!")
            
    with tab2:
        nu, np = st.text_input("Tên đăng ký"), st.text_input("Mật khẩu mới", type="password")
        if st.button("Tạo tài khoản"):
            try:
                db_query('INSERT INTO users VALUES (?,?)', (nu, np), commit=True)
                st.success("Xong! Hãy đăng nhập.")
            except: st.error("Tên đã tồn tại!")

# --- PHẦN 3: DASHBOARD CHÍNH ---
else:
    user = st.session_state.user
    st.title("💰 100 NGÀY TIẾT KIỆM")
    if st.sidebar.button("Đăng xuất"): del st.session_state.user; st.rerun()

    data = db_query('SELECT name, target, saved FROM goals WHERE u=?', (user,), fetch=True)

    if not data:
        st.subheader("🎯 Thiết lập mục tiêu")
        name = st.text_input("Mục tiêu của bạn là gì?")
        target = st.number_input("Số tiền cần (VNĐ)", min_value=0, step=10000)
        if st.button("🚀 Bắt đầu"):
            db_query('INSERT INTO goals (u, name, target) VALUES (?,?,?)', (user, name, target), commit=True)
            st.balloons(); st.rerun()
    else:
        name, target, saved = data
        percent = min(int((saved/target)*100), 100)
        
        st.info(f"🚩 Mục tiêu: **{name}**")
        st.metric("Tiến độ", f"{saved:,.0f} / {target:,.0f} VNĐ", f"{percent}%")
        st.progress(percent)

        if percent >= 100:
            st.success("🎊 HOÀN THÀNH XUẤT SẮC!")
            st.snow()
            if st.button("🔄 Tiết kiệm mục tiêu khác"):
                db_query('DELETE FROM goals WHERE u=?', (user,), commit=True)
                st.rerun()
        else:
            st.subheader("💵 Nhập tiền hôm nay")
            amt = st.number_input("Số tiền (VNĐ)", min_value=1000, step=1000)
            if st.button("✅ Xác nhận"):
                db_query('UPDATE goals SET saved = saved + ? WHERE u=?', (amt, user), commit=True)
                st.balloons(); st.rerun()