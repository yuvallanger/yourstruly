from bottle import route, run, request, get, post

import youtube_dl

SETTINGS = {
	'skip_download': True,
	'ignore_errors': True,
}

downloader = youtube_dl.YoutubeDL(SETTINGS)

@get('/')
def yt_get():
	return '''
		<form action="/" method="post">
			URL: <input name="videocode" type="text" />
			<input value="yt" type="submit" />
		</form>
	'''

@post('/')
def yt_post():
	video_code = request.forms.get('videocode')
	return downloader.extract_info(video_code).get('url', 'nope')

run(host='localhost', post=8080)
