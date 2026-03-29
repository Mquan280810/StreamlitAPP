import streamlit as st
import sqlite3
import pandas as pd

# ==========================================
# PHẦN 1: QUẢN LÝ DATABASE (Giữ nguyên & thêm hàm Update)
# ==========================================
def create_connection():
    return sqlite3.connect('saving_data.db')

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)')
    c.execute('''
        CREATE TABLE IF NOT EXISTS saving_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            goal_name TEXT,
            total_amount REAL,
            saved_amount REAL DEFAULT 0,
            FOREIGN KEY(username) REFERENCES users(username)
        )
    ''')
    conn.commit()
    conn.close()

# Hàm mới: Cập nhật số tiền tiết kiệm (Cộng dồn)
def update_saving(username, amount):
    conn = create_connection()
    c = conn.cursor()
    c.execute('UPDATE saving_records SET saved_amount = saved_amount + ? WHERE username = ?', (amount, username))
    conn.commit()
    conn.close()

# Các hàm bổ trợ khác giữ nguyên logic của bạn
def add_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users(username, password) VALUES (?,?)', (username, password))
        conn.commit()
        return True
    except: return False
    finally: conn.close()

def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

def get_user_goal(username):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT goal_name, total_amount, saved_amount FROM saving_records WHERE username = ?', (username,))
    data = c.fetchone()
    conn.close()
    return data

def set_user_goal(username, goal, total):
    conn = create_connection()
    c = conn.cursor()
    c.execute('INSERT INTO saving_records(username, goal_name, total_amount) VALUES (?,?,?)', (username, goal, total))
    conn.commit()
    conn.close()

# ==========================================
# PHẦN 2: GIAO DIỆN (Làm lại phần Dashboard điền tiền)
# ==========================================
st.set_page_config(page_title="Saving Pro 6", page_icon="💰", layout="centered")
create_tables()

if 'logged_in' not in st.session_state: st.session_state['logged_in'] = False
if 'user_active' not in st.session_state: st.session_state['user_active'] = ""

def auth_page():
    col_h1, col_h2 = st.columns([10, 2])
    with col_h1: st.markdown("<h2 style='color: green;'>E-BIKE - SAVING</h2>", unsafe_allow_html=True)
    with col_h2: st.markdown("<b>Đăng nhập/Đăng ký</b>", unsafe_allow_html=True)
    st.markdown("---")
    auth_mode = st.tabs(["🔐 Đăng Nhập", "📝 Đăng Ký"])
    
    with auth_mode[0]:
        u = st.text_input("Tài khoản", key="l_u")
        p = st.text_input("Mật khẩu", type="password", key="l_p")
        if st.button("Đăng nhập"):
            if login_user(u, p):
                st.session_state['logged_in'], st.session_state['user_active'] = True, u
                st.rerun()
            else: st.error("Sai tài khoản!")
            
    with auth_mode[1]:
        nu = st.text_input("Tài khoản mới", key="r_u")
        np = st.text_input("Mật khẩu mới", type="password", key="r_p")
        cp = st.text_input("Xác nhận mật khẩu", type="password", key="r_c")
        if st.button("Đăng ký"):
            if np == cp and add_user(nu, np): st.success("Xong! Qua tab Đăng nhập nhé.")
            else: st.error("Lỗi đăng ký!")

# --- LÀM LẠI PHẦN DASHBOARD ĐIỀN TIỀN ---
def main_dashboard():
    user = st.session_state['user_active']
    st.title(f"💰 100 NGÀY TIẾT KIỆM")
    
    goal_data = get_user_goal(user)

    if not goal_data:
        st.subheader("🎯 Thiết lập mục tiêu")
        g = st.text_input("Bạn tiết kiệm để làm gì?")
        t = st.number_input("Số tiền mục tiêu (VNĐ)", min_value=0, step=10000)
        if st.button("Bắt đầu hành trình"):
            if g and t > 0:
                set_user_goal(user, g, t)
                st.balloons()
                st.rerun()
    else:
        name, total, saved = goal_data
        percent = min(int((saved / total) * 100), 100)

        # Hiển thị thông số
        c1, c2 = st.columns(2)
        c1.metric("Mục tiêu", name)
        c2.metric("Đã tiết kiệm", f"{saved:,.0f} / {total:,.0f} VNĐ")

        st.write(f"### Tiến độ: {percent}%")
        st.progress(percent)

        st.divider()

        # PHẦN ĐIỀN SỐ TIỀN TIẾT KIỆM (Mục tiêu chính)
        st.subheader("💵 Nhập số tiền tiết kiệm hôm nay")
        with st.container():
            amount = st.number_input("Nhập số tiền (VNĐ):", min_value=1000, step=1000, key="add_money")
            if st.button("Xác nhận gửi tiền vào quỹ"):
                update_saving(user, amount)
                st.success(f"Đã thêm {amount:,.0f} VNĐ! Cố gắng lên!")
                st.balloons()
                st.rerun()

    if st.sidebar.button("Đăng xuất"):
        st.session_state['logged_in'] = False
        st.rerun()

# Điều hướng chính
if not st.session_state['logged_in']: auth_page()
else: main_dashboard()