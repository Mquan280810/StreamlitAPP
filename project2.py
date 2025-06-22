import streamlit as st
st.title("Điền) Thông Tin Giới Thiệu")
my_bar = st.progress(0)
quiz = ["Họ và Tên:", "Ngày Tháng Năm Sinh:", "Sở Thích:"]
answers = []
len_quiz = len(quiz)
for i in range(len_quiz):
	answer = st.text_input(quiz[i], "")
	if answer != "":
		answers.append(answer)
if st.button("Confirm"):
	if len(answers) == len_quiz:
		my_bar.progress(100)
		st.write("Bạn Đã Hoàn Thành Đầy Đủ Thông Tin ><")
		st.balloons()
	else:
		my_bar.progress(len(answers)/len_quiz)
		st.write("Bạn Chưa Hoàn Thành Đầy Đủ Thông Tin!")
	for i in range(len(answers)):
		st.write(quiz[i], answers[i])
