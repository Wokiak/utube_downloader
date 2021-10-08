link = input("Put your link here: ")
	action = input("What do u want to do ? Download high quality video(mp4) or only audio(mp3)? ")
	age_req = input("Does video has age requirements ? Yes/no :  ")
	if age_req == 'yes' or age_req == 'y' :
		if action == 'mp4' or action == 'video' or action == "1" :
			mp4 = 'youtube-dl -f "bestvideo[height<= '
			quality = input('''Choose quality of video : \n1080p \n720p \n480p \n360p \n240p \n144p ''')
			cmd = mp4 + quality + ']"+140 --all-subs --cookies youtube.com_cookies.txt --merge-output-format mp4 ' + link
			os.system(cmd)



		if action == "mp3" or action == 'music' or action == 'audio' or action == "2" :
			mp3 = 'youtube-dl -x --all-subs --cookies youtube.com_cookies.txt --audio-format mp3 '
			cmd = mp3 + link
			os.system(cmd)
	else :
		if action == 'mp4' or action == 'video' or action == "1" :
			mp4 = 'youtube-dl -f "bestvideo[height<= '
			quality = input('''Choose quality of video : \n1080p \n720p \n480p \n360p \n240p \n144p ''')
			cmd = mp4 + quality + ']"+140 --merge-output-format mp4 ' + link
			os.system(cmd)



		if action == "mp3" or action == 'music' or action == 'audio' or action == "2" :
			mp3 = 'youtube-dl -x --audio-format mp3 '
			cmd = mp3 + link
			os.system(cmd)