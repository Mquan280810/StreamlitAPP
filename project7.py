import streamlit as st
with st.form ('Order do uong'):
	drinks = ('Tra sua truyen thong','trua sua matcha',' tra sua trai cay')
	option_drink = st.selectbox('ban muon loai do uong gi?', drinks)
	sugars = ('duong trang', 'duong nau', 'khong them duong')
	option_sugar = st.selectbox('ban thich them loai duong nao?', sugars)
	nums = st.slider('so luong ban muon dat:', 0, 10, 0)
	bill = {'loai do uong': option_drink, 'loai duong:': option_sugar, 'so luong:': nums}
	submitted = st.form_submit_button("xac nhan")
	if submitted:
		st.write('ban da chon:')
		for x,y in bill.items():
			st.write(x,y)
print_bill = st.checkbox('in hoa don')
if print_bill:
	ans = ''
	for x in bill:
		ans += str(x) + '' + str(bill[x]) + '\n'
		st.download_button('in hoa don', ans)