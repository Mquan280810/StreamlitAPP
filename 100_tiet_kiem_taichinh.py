import streamlit as st
import sqlite3
import pandas as pd

# ==========================================
# PHẦN 1: QUẢN LÝ DATABASE (Kỹ năng Pro 6)
# ==========================================
def create_connection():
    # Tạo hoặc kết nối đến file db
    conn = sqlite3.connect('saving_data.db')
    return conn

def create_tables():
    conn = create_connection()
    c = conn.cursor()
    # Tạo bảng User
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY, 
            password TEXT
        )
    ''')
    # Tạo bảng Dữ liệu Tiết Kiệm (Liên kết với User)
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

# --- Các hàm xử lý User ---
def add_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    try:
        c.execute('INSERT INTO users(username, password) VALUES (?,?)', (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError: # Tên user đã tồn tại
        return False
    finally:
        conn.close()

def login_user(username, password):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username =? AND password =?', (username, password))
    data = c.fetchall()
    conn.close()
    return data

# --- Các hàm xử lý Dữ liệu Tiết kiệm (Pro 6) ---
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
    # Kiểm tra xem user đã có mục tiêu chưa
    if get_user_goal(username):
        st.warning("Bạn đã có mục tiêu rồi!")
    else:
        c.execute('INSERT INTO saving_records(username, goal_name, total_amount) VALUES (?,?,?)', (username, goal, total))
        conn.commit()
        st.success("Thiết lập mục tiêu thành công!")
    conn.close()

# ==========================================
# PHẦN 2: CẤU HÌNH & GIAO DIỆN (Pro 4 -> Pro 6)
# ==========================================
st.set_page_config(page_title="Saving Pro 6", page_icon="💰", layout="centered")

# Khởi tạo DB
create_tables()

# Khởi tạo session_state để lưu trạng thái đăng nhập
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if 'user_active' not in st.session_state:
    st.session_state['user_active'] = ""

# --- Giao diện Đăng ký / Đăng nhập (Theo phác thảo) ---
def auth_page():
    # Thanh ngang phía trên (Fake header giống ảnh)
    col_h1, col_h2 = st.columns([10, 2])
    with col_h1:
        st.markdown("<h2 style='color: green;'>E-BIKE - SAVING</h2>", unsafe_allow_html=True)
    with col_h2:
        st.markdown("<b>Đăng nhập/Đăng ký</b>", unsafe_allow_html=True)
    st.markdown("---")

    # Tabs cho Đăng nhập và Đăng ký
    auth_mode = st.tabs(["🔐 Đăng Nhập", "📝 Đăng Ký"])

    # --- TAB ĐĂNG NHẬP (Giống ảnh 1) ---
    with auth_mode[0]:
        st.write("### Đăng nhập (Log in)")
        username = st.text_input("Tài khoản", key="login_user")
        password = st.text_input("Mật khẩu", type="password", key="login_pass")
        
        # Căn giữa nút bấm
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        if st.button("Đăng nhập", key="btn_login"):
            if login_user(username, password):
                st.session_state['logged_in'] = True
                st.session_state['user_active'] = username
                st.success(f"Chào mừng {username}!")
                st.balloons()
                st.rerun()
            else:
                st.error("Tài khoản hoặc mật khẩu không chính xác!")
        st.markdown("</div>", unsafe_allow_html=True)

    # --- TAB ĐĂNG KÝ (Giống ảnh 2) ---
    with auth_mode[1]:
        st.write("### Đăng ký (Sign up)")
        new_username = st.text_input("Tạo tài khoản mới", key="reg_user")
        new_password = st.text_input("Tạo mật khẩu", type="password", key="reg_pass")
        confirm_pass = st.text_input("Xác nhận mật khẩu", type="password", key="reg_confirm")
        
        # Căn giữa nút bấm
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        if st.button("Đăng ký", key="btn_reg"):
            if not new_username or not new_password:
                st.error("Vui lòng điền đầy đủ thông tin!")
            elif new_password != confirm_pass:
                st.error("Mật khẩu xác nhận không khớp!")
            else:
                if add_user(new_username, new_password):
                    st.success("Đăng ký thành công! Hãy chuyển sang tab Đăng nhập.")
                else:
                    st.warning("Tên tài khoản đã tồn tại!")
        st.markdown("</div>", unsafe_allow_html=True)

# --- GIAO DIỆN CHÍNH (DASHBOARD) SAU KHI ĐĂNG NHẬP ---
def main_dashboard():
    active_user = st.session_state['user_active']
    
    st.title(f"💰 100 NGÀY TIẾT KIỆM TIỀN VÌ MỤC TIÊU")
    st.write(f"Chào mừng **{active_user}** tới hành trình 100 ngày kỷ luật!")

    # Lấy dữ liệu riêng của User
    goal_data = get_user_goal(active_user)

    if not goal_data:
        # User chưa có mục tiêu -> Thiết lập
        with st.expander("⚡️ THIẾT LẬP MỤC TIÊU MỚI (Lần đầu)", expanded=True):
            st.write("Hãy đặt ra mục tiêu tài chính của bạn!")
            muc_tieu = st.text_input("Mục tiêu của bạn là gì? (Ví dụ: Mua laptop mới)")
            so_tien_can = st.number_input("Tổng số tiền cần đạt được (VNĐ):", min_value=0, step=10000)
            
            if st.button("Xác nhận bắt đầu hành trình"):
                if muc_tieu and so_tien_can > 0:
                    set_user_goal(active_user, muc_tieu, so_tien_can)
                    st.balloons()
                    st.rerun()
                else:
                    st.error("Vui lòng điền tên mục tiêu và số tiền!")
    else:
        # User đã có mục tiêu -> Hiển thị Dashboard (Pro 6)
        goal_name, total_needed, current_saved = goal_data
        
        # Tính toán phần trăm progress
        if total_needed > 0:
            progress_percent = int((current_saved / total_needed) * 100)
        else:
            progress_percent = 0

        # Hiển thị Progress (Pro 4 command)
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Mục tiêu", goal_name)
            st.metric("Tổng tiền cần", f"{total_needed:,.0f} VNĐ")
        with col2:
            st.metric("Đã tiết kiệm", f"{current_saved:,.0f} VNĐ")
            st.write("### Tiến độ:")
            st.progress(min(progress_percent, 100))
            st.write(f"{progress_percent}% hoàn thành")

            # 3. PHẦN NHẬP SỐ TIỀN TIẾT KIỆM (Mới thêm)
        st.subheader("📥 Cập nhật tiết kiệm hôm nay")
        with st.form("saving_form"):
            amount_input = st.number_input("Số tiền bạn vừa tiết kiệm được (VNĐ):", min_value=1000, step=1000)
            submit_save = st.form_submit_state = st.form_submit_button("Xác nhận tiết kiệm")
            
            if submit_save:
                if current_saved + amount_input > total_needed:
                    st.warning("Số tiền này sẽ vượt quá mục tiêu! Chúc mừng bạn!")
                
                update_saved_amount(active_user, amount_input)
                st.success(f"Đã cộng thêm {amount_input:,.0f} VNĐ vào quỹ!")
                st.balloons()
                st.rerun() # Load lại để cập nhật thanh tiến độ ngay lập tức

    # Nút Đăng xuất ở thanh bên
    if st.sidebar.button("Đăng xuất"):
        st.session_state['logged_in'] = False
        st.session_state['user_active'] = ""
        st.rerun()

# ==========================================
# PHẦN 3: ĐIỀU HƯỚNG CHÍNH
# ==========================================
if not st.session_state['logged_in']:
    auth_page()
else:
    main_dashboard()