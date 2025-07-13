import streamlit as st
appertizer = [' banh mi nuong pho mai', 'sup hanh tay phap', 'salad caesar', 'goi cuon', 'banh mi bo toi']
main = ['pizza', ' pad thai', ' steak', 'moussaka', 'pealla']
dessert = ['cheesecak', 'tiramisu', 'creme brulee', ' panna cotta', 'trifle']

with st.form('thuc don yeu thich'):
	options1 = st.multiselect('mon khai vi ua thich cua ban?', appertizer)
	options2 = st.multiselect('mon chinh ua thich?', main)
	options3 = st.multiselect('mon trang mieng ua thich la?', dessert)
	submitted = st.form_submit_button('Submit')
	if submitted:
		st.write('cac lua chon cua ban la:')
		st.write('**1. mon khai vi:**')
		if len(options1) == 0:
			st.write('ban chua chon mon khai vi')
		else:
			for i in range(len(options1)):
				sr.write(options1[i])
		st.write('**2. mon chinh:**')
		if len(options2) == 0:
			st.write('ban chua chon mon chinh')
		else:
			for i in range(len(options2)):
				sr.write(options2[i])
		st.write('**3. mon trang mieng:**')
		if len(options3) == 0:
			st.write('ban chua chon mon trang mieng')
		else:
			for i in range(len(option3)):
				sr.write(options3[i])