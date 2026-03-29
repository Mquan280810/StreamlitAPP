import streamlit as st
import sqlite3

# --- PHẦN DATABASE (Giữ nguyên và thêm hàm cập nhật) ---
def create_connection():
    return sqlite3.connect('saving_data.db')

def update_saved_amount(username, amount_to_add):
    conn = create_connection()
    c = conn.cursor()
    # Cộng dồn số tiền mới vào số tiền cũ trong DB
    c.execute('''
        UPDATE saving_records 
        SET saved_amount = saved_amount + ? 
        WHERE username = ?
    ''', (amount_to_add, username))
    conn.commit()
    conn.close()

def get_user_goal(username):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT goal_name, total_amount, saved_amount FROM saving_records WHERE username = ?', (username,))
    data = c.fetchone()
    conn.close()
    return data

# ... (Các hàm create_tables, add_user, login_user giữ nguyên như file trước) ...

# ==========================================
# GIAO DIỆN CHÍNH (CẬP NHẬT PHẦN TIẾT KIỆM)
# ==========================================
def main_dashboard():
    active_user = st.session_state['user_active']
    st.title("💰 100 NGÀY TIẾT KIỆM TIỀN")
    
    goal_data = get_user_goal(active_user)

    if not goal_data:
        st.info("Hãy thiết lập mục tiêu đầu tiên của bạn ở thanh bên hoặc màn hình chính!")
        # (Phần code thiết lập mục tiêu cũ đặt ở đây)
    else:
        goal_name, total_needed, current_saved = goal_data
        
        # 1. Hiển thị thông tin mục tiêu (Metric)
        col1, col2, col3 = st.columns(3)
        col1.metric("Mục tiêu", goal_name)
        col2.metric("Cần đạt", f"{total_needed:,.0f} đ")
        col3.metric("Đã có", f"{current_saved:,.0f} đ", delta=f"+ {current_saved:,.0f}")

        # 2. THANH TIẾN ĐỘ (Phần quan trọng nhất)
        progress_percent = min(int((current_saved / total_needed) * 100), 100)
        st.write(f"### Tiến độ: {progress_percent}%")
        st.progress(progress_percent)

        st.divider()

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

    # Nút Đăng xuất
    if st.sidebar.button("Đăng xuất"):
        st.session_state['logged_in'] = False
        st.rerun()

# (Phần điều hướng auth_page() giữ nguyên)
if not st.session_state.get('logged_in', False):
    # Gọi hàm auth_page() cũ ở đây
    pass 
else:
    main_dashboard()